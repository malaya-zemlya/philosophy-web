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

Key: OPENAI_API_KEY from the environment, else from a gitignored `.env` at the repo root.

Usage (prefer the make targets):
  make embed                      # uv run python scripts/similar.py embed
  make similar Q="rough idea"     # ... query --q "rough idea" [--k 10] [--type claim]
  make similar ID=claim-foo       # ... query --id claim-foo   (keyless)
  make dupes MIN=0.85             # ... dupes --min 0.85       (keyless)
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


def embed_texts(texts):
    """Embed a list of strings via the OpenAI API; returns list of vectors."""
    from openai import OpenAI  # lazy: keyless paths must not require the package at import time
    client = OpenAI(api_key=api_key())
    vecs = []
    for i in range(0, len(texts), BATCH):
        resp = client.embeddings.create(model=MODEL, dimensions=DIMS, input=texts[i:i + BATCH])
        vecs += [d.embedding for d in sorted(resp.data, key=lambda d: d.index)]
    return vecs


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
    _staleness_warning(nodes)
    ids, mat = _matrix(nodes, cache, args.type)
    if args.id:
        rec = cache.get(args.id)
        if not rec:
            raise SystemExit(f"'{args.id}' has no cached embedding "
                             f"(unknown id, excluded type, or not yet embedded — try `make embed`)")
        q = np.array(rec["vec"], dtype=np.float32)
    else:
        q = np.array(embed_texts([args.q])[0], dtype=np.float32)
    q /= np.linalg.norm(q)
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
    d = sub.add_parser("dupes", help="same-type pairs above a similarity threshold (keyless)")
    d.add_argument("--min", type=float, default=0.85, help="similarity threshold (default 0.85)")
    d.add_argument("--type", choices=sorted(EMBED_TYPES), help="check only one node type")
    args = ap.parse_args()
    if args.cmd == "query" and bool(args.q) == bool(args.id):
        ap.error("query needs exactly one of --q or --id")
    {"embed": cmd_embed, "query": cmd_query, "dupes": cmd_dupes}[args.cmd](args)


if __name__ == "__main__":
    main()
