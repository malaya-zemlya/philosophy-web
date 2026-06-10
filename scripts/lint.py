#!/usr/bin/env python3
"""
lint.py — deterministic integrity check + backlink index for the philosophy web.

No model calls. Run on every commit (see scripts/pre-commit). It:
  - parses frontmatter of every web/**/*.md node
  - verifies every edge target id exists (dangling-edge detection)
  - flags missing `author`, likely non-atomic claims, and contested claims with
    no attacking argument
  - computes backlinks (the reverse edges we deliberately never store by hand)
  - renders `[[id]]` body/transcript shorthand into clickable `[slug](relpath)` links and refreshes
    existing ones (derived data, like the backlinks — never hand-maintained); pass --check to
    report would-be changes without writing
  - writes web/INDEX.md

Requires PyYAML:  pip install pyyaml
Exits nonzero if dangling edges or duplicate ids are found.
"""
import sys, pathlib, re
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

import weblinks   # shared id<->path + link rendering (scripts/weblinks.py)

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
TRANSCRIPTS = ROOT / "transcripts"
PATTERNS = ROOT / "patterns"   # argument-pattern reference library (not web nodes)

def pattern_ids():
    """Valid `pattern:` values = patterns/*.md filenames (minus _README)."""
    if not PATTERNS.is_dir():
        return set()
    return {p.stem for p in PATTERNS.glob("*.md") if p.name != "_README.md"}

# `pattern` is a reference into patterns/, NOT a graph edge — kept out of EDGE_KEYS so it is
# never resolved as a node id or counted as a backlink.

# edge name -> True if it may hold a list (vs scalar). We accept either form anyway.
EDGE_KEYS = ["uses_concept", "presupposes", "premise", "concludes", "supports",
             "attacks", "responds_to", "answers", "commits_to", "rejects", "holds"]

# Per-type legal OUTGOING edges. Authoritative; keep schemas/<type>.md in sync with this.
LEGAL_EDGES = {
    "concept":   {"uses_concept", "presupposes"},
    "claim":     {"uses_concept", "presupposes", "answers"},
    "argument":  {"premise", "concludes", "supports", "attacks", "responds_to",
                  "uses_concept", "presupposes"},
    "question":  {"uses_concept"},
    "position":  {"commits_to", "rejects", "answers", "uses_concept", "presupposes"},
    "source":    set(),
    "character": {"commits_to", "rejects", "holds", "uses_concept"},
}
# Types that must carry at least one edge from the given set (else malformed).
REQUIRES_ONE_OF = {
    "argument": {"concludes", "supports", "attacks", "responds_to"},
    "position": {"commits_to", "rejects", "answers"},
}

FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

def parse(path):
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"  ! YAML error in {path.relative_to(ROOT)}: {e}")
        return None

def as_list(v):
    if v is None: return []
    return v if isinstance(v, list) else [v]

def render_links(id_to_path, check):
    """Render `[[id]]` -> `[slug](relpath)` and refresh existing web links across bodies and
    transcripts. Returns (changed_files, reports). Frontmatter is never touched."""
    id_set = set(id_to_path)
    changed, reports = [], []
    files = sorted(WEB.rglob("*.md")) + (sorted(TRANSCRIPTS.rglob("*.md"))
                                         if TRANSCRIPTS.is_dir() else [])
    for path in files:
        if path.name in ("INDEX.md", "README.md"):
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = weblinks.split_frontmatter(text)
        new_body, body_reports = weblinks.render_body(body, path, ROOT, id_to_path)
        rel = path.relative_to(ROOT)
        for r in body_reports:
            reports.append(f"{r}  ({rel})")
        for bare in set(weblinks.bare_ids_in(new_body, id_set)):
            reports.append(f"bare id '{bare}' in body — wrap as [[{bare}]]  ({rel})")
        if new_body != body:
            changed.append(rel)
            if not check:
                path.write_text(fm + new_body, encoding="utf-8")
    return changed, reports


def main():
    check = "--check" in sys.argv[1:]
    nodes = {}          # id -> dict(fm, path)
    problems = []
    dup_ids = []
    valid_patterns = pattern_ids()

    for path in sorted(WEB.rglob("*.md")):
        if path.name in ("INDEX.md", "README.md"):
            continue
        fm = parse(path)
        if fm is None:
            problems.append(f"no/!parseable frontmatter: {path.relative_to(ROOT)}")
            continue
        nid = fm.get("id")
        if not nid:
            problems.append(f"missing id: {path.relative_to(ROOT)}")
            continue
        if nid in nodes:
            dup_ids.append(nid)
        nodes[nid] = {"fm": fm, "path": path}

    # edge integrity + backlinks + per-type schema enforcement
    backlinks = {nid: [] for nid in nodes}   # target -> list of (source_id, edge)
    illegal = []
    for nid, n in nodes.items():
        fm = n["fm"]
        ntype = fm.get("type")
        if not fm.get("author"):
            problems.append(f"missing author: {nid}")
        if ntype not in LEGAL_EDGES:
            problems.append(f"unknown type '{ntype}': {nid}")
        # Heuristic only: an 'and' inside the predicate (one proposition about a
        # conjoint standard/pair) is fine — confirm with `atomicity: verified` in
        # frontmatter after a human check, and the warning is suppressed.
        if (ntype == "claim" and " and " in str(fm.get("title", "")).lower()
                and fm.get("atomicity") != "verified"):
            problems.append(f"possibly non-atomic claim (contains 'and'): {nid}")
        # `pattern` (optional, arguments only): must name a file in patterns/
        pat = fm.get("pattern")
        if pat:
            if ntype != "argument":
                problems.append(f"pattern on non-argument type '{ntype}': {nid}")
            elif valid_patterns and pat not in valid_patterns:
                problems.append(f"unknown pattern '{pat}' (see patterns/): {nid}")
        # required-one-of edge for argument/position
        present_edges = {e for e in EDGE_KEYS if fm.get(e)}
        need = REQUIRES_ONE_OF.get(ntype)
        if need and not (present_edges & need):
            problems.append(f"{ntype} targets nothing (needs one of {sorted(need)}): {nid}")
        for edge in EDGE_KEYS:
            targets = as_list(fm.get(edge))
            if targets and ntype in LEGAL_EDGES and edge not in LEGAL_EDGES[ntype]:
                illegal.append(f"ILLEGAL edge '{edge}' on type '{ntype}': {nid}")
            for tgt in targets:
                if tgt not in nodes:
                    problems.append(f"DANGLING edge {nid} --{edge}--> {tgt} (no such id)")
                else:
                    backlinks[tgt].append((nid, edge))
    problems = illegal + problems

    # contested claims with no incoming attack
    for nid, n in nodes.items():
        if n["fm"].get("type") == "claim" and n["fm"].get("status") == "contested":
            if not any(e == "attacks" for _, e in backlinks[nid]):
                problems.append(f"contested claim with no attacking argument: {nid}")

    # render/refresh clickable body+transcript links (derived data, like backlinks below)
    id_to_path = {nid: n["path"].relative_to(ROOT).as_posix() for nid, n in nodes.items()}
    changed_links, link_reports = render_links(id_to_path, check)
    problems += link_reports

    # write INDEX.md (ids rendered as clickable links into the nodes they name)
    index_path = WEB / "INDEX.md"
    def link(nid):
        rel = weblinks.id_to_relpath(nid, index_path, ROOT, id_to_path)
        return f"[{nid}]({rel})" if rel else nid
    lines = ["# INDEX (generated by scripts/lint.py — do not edit by hand)\n"]
    for nid in sorted(nodes):
        fm = nodes[nid]["fm"]
        lines.append(f"## {link(nid)}")
        lines.append(f"- type: {fm.get('type')} | author: {fm.get('author')} | status: {fm.get('status','asserted')}")
        bl = backlinks[nid]
        if bl:
            lines.append("- backlinks:")
            for src, edge in sorted(bl):
                lines.append(f"  - {link(src)} --{edge}-->")
        lines.append("")
    index_text = "\n".join(lines)
    if not check:
        index_path.write_text(index_text, encoding="utf-8")

    # report
    print(f"nodes: {len(nodes)}   edges checked across {len(EDGE_KEYS)} types")
    if dup_ids:
        print("DUPLICATE IDS:", ", ".join(sorted(set(dup_ids))))
    if changed_links:
        verb = "would re-render" if check else "re-rendered"
        print(f"{verb} links in {len(changed_links)} file(s):")
        for rel in changed_links:
            print(f"  ~ {rel}")
    if problems:
        print(f"\n{len(problems)} issue(s):")
        for p in problems:
            print("  -", p)
    else:
        print("no issues.")
    print("would rewrite web/INDEX.md (--check)" if check else "wrote web/INDEX.md")

    fatal = (bool(dup_ids)
             or any(p.startswith(("DANGLING", "ILLEGAL", "dangling", "unknown")) for p in problems)
             or (check and bool(changed_links)))
    sys.exit(1 if fatal else 0)

if __name__ == "__main__":
    main()
