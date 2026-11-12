#!/usr/bin/env python3
"""
similar.py — semantic similarity search over the philosophy web (OpenAI embeddings).

Complements the lexical tools (`grep -ri`, `make find`): grep matches surface phrases, this
matches ideas, so "dispositionalism" finds "meaning is a pattern of use". It exists chiefly to
serve the grep-before-create rule (CLAUDE.md rule 1) — catching near-duplicates that hide behind
a different vocabulary — plus see-also discovery and rough-idea search.

Corpus: content nodes (claim, argument, concept, position, question) + sources. Characters,
the test fixture, and transcripts are excluded — the web is the searchable distillate.

The cache (embeddings/web.jsonl, committed like INDEX.md and graph/web.svg) holds one JSON line
per node: id, a content hash, model/dims, and the vector. Only changed nodes re-embed, so git
diffs stay small. Reading the cache needs no API key — `similar.py query --id <node>` and
`dupes` work keyless on any clone; only `embed` and free-text queries call OpenAI.

SEP: the local Stanford Encyclopedia mirror (sep/, see sep/README.md) is a second, read-only
corpus, embedded per section so a hit points at `<entry-url>#<anchor>`. Its cache lives in the
gitignored sep/data/embeddings/ (one <slug>.npy + <slug>.json per entry; copyrighted source,
~37M tokens, never committed). `query` shows web hits first, then a separate block of SEP hits;
`dupes` and lint's staleness advisory stay web-only.

Key: OPENAI_API_KEY from the environment, else from a gitignored `.env` at the repo root.

Usage (prefer the make targets):
  make embed                      # uv run python scripts/similar.py embed
  make similar Q="rough idea"     # ... query --q "rough idea" [--k 10] [--type claim]
  make similar ID=claim-foo       # ... query --id claim-foo   (keyless)
  make dupes MIN=0.85             # ... dupes --min 0.85       (keyless)
  make sep-embed                  # ... sep-embed [--slugs a b] (embed/refresh the SEP mirror)
  make similar Q=... SEP=only     # ... query --sep only|none|include (default include)
"""
import argparse
import hashlib
import json
import os
import pathlib
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import weblinks                 # MDLINK_RE, WIKILINK_RE, split_frontmatter
from lint import parse, as_list  # frontmatter parse (no side effects; graph.py does the same)

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
CACHE = ROOT / "embeddings" / "web.jsonl"

MODEL = "text-embedding-3-large"
DIMS = 1024                     # Matryoshka truncation; the API renormalizes
EMBED_TYPES = {"claim", "argument", "concept", "position", "question", "source"}
SKIP_DIRS = {"characters", "test"}
BATCH = 96                      # inputs per API request
MAX_CHARS = 32_000              # ~8k tokens, the embedding-model input ceiling

SEP_JSONL = ROOT / "sep" / "data" / "sep.jsonl"
SEP_CACHE = ROOT / "sep" / "data" / "embeddings"
SEP_CHUNK = 6_000               # chars per SEP chunk (~1.5k tokens); split at paragraph breaks
SEP_WORKERS = 4                 # concurrent entries during sep-embed


# ---------------------------------------------------------------- corpus

def corpus():
    """id -> {fm, path, text, hash} for every embeddable node."""
    nodes = {}
    for path in sorted(WEB.rglob("*.md")):
        if path.name in ("INDEX.md", "README.md") or path.parent.name in SKIP_DIRS:
            continue
        fm = parse(path)
        if not fm or fm.get("type") not in EMBED_TYPES or not fm.get("id"):
            continue
        text = embed_text(fm, path)
        nodes[fm["id"]] = {"fm": fm, "path": path, "text": text, "hash": text_hash(text)}
    return nodes


def embed_text(fm, path):
    """The text a node is embedded as: headword + title + tags + body, with rendered links
    reduced to plain text and the derived `### See also` section stripped (it would inflate
    similarity between merely-adjacent nodes)."""
    _, body = weblinks.split_frontmatter(path.read_text(encoding="utf-8"))
    body = body.split("\n### See also")[0]
    body = weblinks.MDLINK_RE.sub(lambda m: m.group(1), body)                    # [label](x.md) -> label
    body = weblinks.WIKILINK_RE.sub(
        lambda m: m.group(2)[1:] if m.group(2) else m.group(1), body)            # [[id|alias]] -> alias
    parts = [str(fm.get("headword", "")), str(fm.get("title", "")),
             ", ".join(as_list(fm.get("tags"))), body.strip()]
    return "\n".join(p for p in parts if p)[:MAX_CHARS]


def text_hash(text):
    return hashlib.sha256(f"{MODEL}@{DIMS}\n{text}".encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------- cache

def load_cache():
    """id -> {hash, vec} from embeddings/web.jsonl (empty dict if absent)."""
    if not CACHE.is_file():
        return {}
    cache = {}
    for line in CACHE.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rec = json.loads(line)
            cache[rec["id"]] = rec
    return cache


def save_cache(cache):
    CACHE.parent.mkdir(exist_ok=True)
    lines = [json.dumps({"id": nid, "hash": rec["hash"], "model": MODEL, "dims": DIMS,
                         "vec": [round(x, 5) for x in rec["vec"]]},
                        separators=(",", ":"))
             for nid, rec in sorted(cache.items())]
    CACHE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cache_status(nodes=None):
    """(missing, stale, orphaned) id lists — corpus vs cache. Keyless; used by lint's advisory."""
    nodes = nodes if nodes is not None else corpus()
    cache = load_cache()
    missing = sorted(nid for nid in nodes if nid not in cache)
    stale = sorted(nid for nid, n in nodes.items()
                   if nid in cache and cache[nid]["hash"] != n["hash"])
    orphaned = sorted(nid for nid in cache if nid not in nodes)
    return missing, stale, orphaned


# ---------------------------------------------------------------- OpenAI

def api_key():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        env = ROOT / ".env"
        if env.is_file():
            for line in env.read_text(encoding="utf-8").splitlines():
                k, _, v = line.partition("=")
                if k.strip() == "OPENAI_API_KEY":
                    key = v.strip().strip("'\"")
    if not key:
        raise SystemExit("OPENAI_API_KEY not set (env var, or a line in .env at the repo root)")
    return key


def openai_client():
    from openai import OpenAI  # lazy: keyless paths must not require the package at import time
    return OpenAI(api_key=api_key(), max_retries=8)


def embed_texts(texts, client=None):
    """Embed a list of strings via the OpenAI API; returns list of vectors."""
    client = client or openai_client()
    vecs = []
    for i in range(0, len(texts), BATCH):
        resp = client.embeddings.create(model=MODEL, dimensions=DIMS, input=texts[i:i + BATCH])
        vecs += [d.embedding for d in sorted(resp.data, key=lambda d: d.index)]
    return vecs


# ---------------------------------------------------------------- SEP corpus

def _split(text, limit):
    """Split text into pieces <= limit chars, preferring paragraph boundaries."""
    out, cur = [], ""
    for para in text.split("\n\n"):
        while len(para) > limit:                      # a single oversized paragraph
            if cur:
                out.append(cur)
                cur = ""
            out.append(para[:limit])
            para = para[limit:]
        if cur and len(cur) + 2 + len(para) > limit:
            out.append(cur)
            cur = para
        else:
            cur = f"{cur}\n\n{para}" if cur else para
    if cur.strip():
        out.append(cur)
    return out


def sep_chunks(rec):
    """[{anchor, label, text}] for one SEP record: the preamble, then each non-empty section
    (prefixed with entry title and section path), split into SEP_CHUNK-sized pieces."""
    chunks = []
    title = rec["title"]

    def add(anchor, label, body):
        for i, piece in enumerate(_split(body.strip(), SEP_CHUNK)):
            chunks.append({"anchor": anchor, "label": label + (f" (part {i + 1})" if i else ""),
                           "text": f"{title} — {label}\n\n{piece}"[:MAX_CHARS]})

    if rec.get("preamble", "").strip():
        add("", "introduction", rec["preamble"])
    path = {}
    for sec in rec.get("sections", []):
        lvl = sec.get("level", 1)
        path = {k: v for k, v in path.items() if k < lvl}
        path[lvl] = f"{sec.get('number', '')} {sec.get('title', '')}".strip()
        if sec.get("markdown", "").strip():
            add(sec.get("anchor", ""), " › ".join(path[k] for k in sorted(path)), sec["markdown"])
    return chunks


def sep_records(slugs=None):
    if not SEP_JSONL.is_file():
        raise SystemExit(f"no SEP mirror at {SEP_JSONL.relative_to(ROOT)} — see sep/README.md")
    want = set(slugs) if slugs else None
    with SEP_JSONL.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                if want is None or rec["slug"] in want:
                    yield rec


def _sep_hash(chunks):
    return text_hash("\x00".join(c["text"] for c in chunks))


def cmd_sep_embed(args):
    import numpy as np
    from concurrent.futures import ThreadPoolExecutor, as_completed
    SEP_CACHE.mkdir(parents=True, exist_ok=True)
    todo, fresh = [], 0
    for rec in sep_records(args.slugs):
        chunks = sep_chunks(rec)
        if not chunks:
            continue
        h = _sep_hash(chunks)
        meta_p = SEP_CACHE / f"{rec['slug']}.json"
        if meta_p.is_file() and (SEP_CACHE / f"{rec['slug']}.npy").is_file() \
                and json.loads(meta_p.read_text(encoding="utf-8")).get("hash") == h:
            fresh += 1
            continue
        todo.append((rec, chunks, h))
    if args.limit:
        todo = todo[:args.limit]
    est = sum(len(c["text"]) for _, chunks, _ in todo for c in chunks) / 4 / 1e6
    print(f"SEP: {fresh} entries fresh, {len(todo)} to embed (~{est:.1f}M tokens)", flush=True)
    if not todo:
        return
    client = openai_client()

    def work(item):
        rec, chunks, h = item
        vecs = np.array(embed_texts([c["text"] for c in chunks], client), dtype=np.float32)
        vecs /= np.linalg.norm(vecs, axis=1, keepdims=True)
        np.save(SEP_CACHE / f"{rec['slug']}.npy", vecs.astype(np.float16))
        meta = {"slug": rec["slug"], "url": rec["url"], "title": rec["title"], "hash": h,
                "model": MODEL, "dims": DIMS,
                "chunks": [{"anchor": c["anchor"], "label": c["label"]} for c in chunks]}
        (SEP_CACHE / f"{rec['slug']}.json").write_text(json.dumps(meta), encoding="utf-8")
        return rec["slug"]

    done = 0
    with ThreadPoolExecutor(SEP_WORKERS) as pool:
        for fut in as_completed([pool.submit(work, it) for it in todo]):
            fut.result()
            done += 1
            if done % 25 == 0 or done == len(todo):
                print(f"  {done}/{len(todo)} entries", flush=True)
    print(f"SEP cache: {SEP_CACHE.relative_to(ROOT)}  (resumable — rerun to continue)")


def load_sep():
    """(labels, unit-normalized float32 matrix) over every cached SEP chunk, or (None, None)."""
    import numpy as np
    if not SEP_CACHE.is_dir():
        return None, None
    labels, mats = [], []
    for meta_p in sorted(SEP_CACHE.glob("*.json")):
        vec_p = meta_p.with_suffix(".npy")
        if not vec_p.is_file():
            continue
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
        if meta.get("model") != MODEL or meta.get("dims") != DIMS:
            continue
        mats.append(np.load(vec_p))
        labels += [(meta["slug"], meta["title"], meta["url"], c["anchor"], c["label"])
                   for c in meta["chunks"]]
    if not mats:
        return None, None
    mat = np.concatenate(mats).astype(np.float32)
    mat /= np.linalg.norm(mat, axis=1, keepdims=True)
    return labels, mat


def _print_sep_hits(q, k):
    import numpy as np
    labels, mat = load_sep()
    if labels is None:
        print("(SEP not embedded — run `make sep-embed`)", file=sys.stderr)
        return
    scores = mat @ q
    seen = set()
    print(f"\n— SEP ({len({l[0] for l in labels})} entries embedded; best section per entry) —")
    for i in np.argsort(-scores):
        slug, title, url, anchor, label = labels[i]
        if slug in seen:
            continue
        seen.add(slug)
        print(f"{float(scores[i]):.3f}  sep:{slug}  — {title} › {label}  "
              f"({url}{'#' + anchor if anchor else ''})")
        if len(seen) >= k:
            break


# ---------------------------------------------------------------- commands

def cmd_embed(_args):
    nodes = corpus()
    cache = load_cache()
    missing, stale, orphaned = cache_status(nodes)
    todo = missing + stale
    if todo:
        vecs = embed_texts([nodes[nid]["text"] for nid in todo])
        for nid, vec in zip(todo, vecs):
            cache[nid] = {"hash": nodes[nid]["hash"], "vec": vec}
    for nid in orphaned:
        del cache[nid]
    if todo or orphaned:
        save_cache(cache)
    print(f"embedded {len(todo)} node(s) ({len(missing)} new, {len(stale)} changed), "
          f"pruned {len(orphaned)} — cache covers {len(cache)}/{len(nodes)} nodes "
          f"({CACHE.relative_to(ROOT)})")


def _matrix(nodes, cache, type_filter=None):
    """(ids, unit-normalized numpy matrix) for every cached node, optionally one type."""
    import numpy as np
    ids = [nid for nid in nodes
           if nid in cache and (not type_filter or nodes[nid]["fm"].get("type") == type_filter)]
    if not ids:
        raise SystemExit("embedding cache is empty — run `make embed` first")
    mat = np.array([cache[nid]["vec"] for nid in ids], dtype=np.float32)
    mat /= np.linalg.norm(mat, axis=1, keepdims=True)
    return ids, mat


def _staleness_warning(nodes):
    missing, stale, _ = cache_status(nodes)
    if missing or stale:
        print(f"note: {len(missing)} node(s) unembedded, {len(stale)} stale — "
              f"results may miss recent edits; run `make embed`\n", file=sys.stderr)


def _print_hit(score, nid, nodes):
    fm = nodes[nid]["fm"]
    head = fm.get("headword") or fm.get("title") or ""
    rel = nodes[nid]["path"].relative_to(ROOT)
    print(f"{score:.3f}  {nid}  — {head}  ({rel})")


def cmd_query(args):
    import numpy as np
    nodes = corpus()
    cache = load_cache()
    if args.id:
        rec = cache.get(args.id)
        if not rec:
            raise SystemExit(f"'{args.id}' has no cached embedding "
                             f"(unknown id, excluded type, or not yet embedded — try `make embed`)")
        q = np.array(rec["vec"], dtype=np.float32)
    else:
        q = np.array(embed_texts([args.q])[0], dtype=np.float32)
    q /= np.linalg.norm(q)
    if args.sep != "only":
        _staleness_warning(nodes)
        ids, mat = _matrix(nodes, cache, args.type)
        scores = mat @ q
        order = np.argsort(-scores)
        shown = 0
        for i in order:
            if ids[i] == args.id:
                continue  # a node is trivially most similar to itself
            _print_hit(float(scores[i]), ids[i], nodes)
            shown += 1
            if shown >= args.k:
                break
    if args.sep != "none":
        _print_sep_hits(q, args.sep_k if args.sep != "only" else args.k)


def cmd_dupes(args):
    import numpy as np
    nodes = corpus()
    cache = load_cache()
    if not cache:
        raise SystemExit("embedding cache is empty — run `make embed` first")
    _staleness_warning(nodes)
    types = [args.type] if args.type else sorted(EMBED_TYPES)
    pairs = []
    for t in types:
        ids = [nid for nid in nodes if nid in cache and nodes[nid]["fm"].get("type") == t]
        if len(ids) < 2:
            continue
        mat = np.array([cache[nid]["vec"] for nid in ids], dtype=np.float32)
        mat /= np.linalg.norm(mat, axis=1, keepdims=True)
        sim = mat @ mat.T
        for i, j in zip(*np.where(np.triu(sim, k=1) >= args.min)):
            pairs.append((float(sim[i, j]), ids[i], ids[j]))
    if not pairs:
        print(f"no same-type pairs at or above {args.min:.2f}")
        return
    for score, a, b in sorted(pairs, reverse=True):
        print(f"{score:.3f}  {a}  ~  {b}")
    print(f"\n{len(pairs)} pair(s) ≥ {args.min:.2f} — candidates for /reconcile, not verdicts")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("embed", help="refresh embeddings/web.jsonl (needs OPENAI_API_KEY)")
    q = sub.add_parser("query", help="nearest nodes to free text (--q) or an existing node (--id)")
    q.add_argument("--q", help="free-text query (needs OPENAI_API_KEY)")
    q.add_argument("--id", help="node id — nearest neighbors from the cache, keyless")
    q.add_argument("--k", type=int, default=10, help="results to show (default 10)")
    q.add_argument("--type", choices=sorted(EMBED_TYPES), help="restrict hits to one node type")
    q.add_argument("--sep", choices=["include", "only", "none"], default="include",
                   help="also search the local SEP mirror (default include)")
    q.add_argument("--sep-k", type=int, default=5, help="SEP entries to show alongside web hits")
    d = sub.add_parser("dupes", help="same-type pairs above a similarity threshold (keyless)")
    d.add_argument("--min", type=float, default=0.85, help="similarity threshold (default 0.85)")
    d.add_argument("--type", choices=sorted(EMBED_TYPES), help="check only one node type")
    e = sub.add_parser("sep-embed", help="embed/refresh the SEP mirror into sep/data/embeddings/")
    e.add_argument("--slugs", nargs="*", help="only these SEP entry slugs")
    e.add_argument("--limit", type=int, help="embed at most N stale entries this run")
    args = ap.parse_args()
    if args.cmd == "query" and bool(args.q) == bool(args.id):
        ap.error("query needs exactly one of --q or --id")
    {"embed": cmd_embed, "query": cmd_query, "dupes": cmd_dupes, "sep-embed": cmd_sep_embed}[args.cmd](args)


if __name__ == "__main__":
    main()
