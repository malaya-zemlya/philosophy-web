#!/usr/bin/env python3
"""
weblinks.py — shared link logic for the philosophy web.

Cross-references live in two layers:
  - frontmatter EDGES cite nodes by bare id (machine layer; lint resolves these).
  - body / transcript prose cites nodes with the `[[id]]` shorthand, which is RENDERED into a
    clickable relative Markdown link `[slug](relpath)`. The rendered link is derived data — like
    backlinks/INDEX, it is computed by tooling, never hand-maintained.

This module is the single source of truth for: id<->path math, frontmatter/body splitting,
wrapping bare ids into `[[id]]` (one-time migration), and rendering/refreshing the clickable
links (run on every lint). Both scripts/lint.py and scripts/migrate_links.py import it so the two
can never drift.

The id's slug usually matches the filename (id `claim-foo` -> `web/claims/foo.md`), but NOT
always: a file may be renamed while its `id:` stays stable (that's the whole point of ids — see
`claim-phenomenal-residue`, which lives in `phenomenal-states-not-exhausted-by-role.md`). So link
targets are resolved through the REAL id->path map built by scanning frontmatter (the same map
lint uses for edges), never computed from the id string. The slug is used only as link *text*.
"""
import os
import re
import pathlib

TYPES = ["concept", "claim", "argument", "question", "position", "source", "character"]

# Splits a file into (frontmatter-with-fences, body). Files without frontmatter (transcripts)
# come back as ("", whole-text) so the whole thing is treated as body.
_FM_SPLIT_RE = re.compile(r"^(---\n.*?\n---)(.*)$", re.DOTALL)

# `[[id]]` or `[[id|alias label]]`
WIKILINK_RE = re.compile(r"\[\[([a-z]+-[a-z0-9-]+)(\|[^\]]+)?\]\]")
# `[label](target.md)` — only `.md` targets are candidates for refresh
MDLINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")
# spans that must NOT be touched when wrapping bare ids: existing wiki/md links and inline code
_PROTECT_RE = re.compile(r"\[\[[^\]]*\]\]|\[[^\]]*\]\([^)]*\)|`[^`]*`")
# a hyphenated lowercase token that could be an id (membership is checked against the real id set)
_ID_TOKEN_RE = re.compile(r"(?<![\w-])([a-z]+-[a-z0-9-]+)(?![\w-])")
# does a link target look like it points at a web node dir (<type>s/)?
_WEBISH_RE = re.compile(r"(?:^|/)(?:%s)s/" % "|".join(TYPES))


def split_frontmatter(text):
    m = _FM_SPLIT_RE.match(text)
    if m:
        return m.group(1), m.group(2)
    return "", text


def id_parts(nid):
    """('claim-substrate-independence') -> ('claim', 'substrate-independence'); else (None, None)."""
    if "-" not in nid:
        return None, None
    t, slug = nid.split("-", 1)
    return (t, slug) if t in TYPES else (None, None)


def slug_of(nid):
    _, slug = id_parts(nid)
    return slug if slug is not None else nid


def build_id_to_path(root):
    """Scan web/ frontmatter -> {id: path-relative-to-root (POSIX)}. The authoritative id->path
    map (mirrors lint's `nodes[id]['path']`); handles files whose name differs from their slug."""
    root = pathlib.Path(root)
    web = root / "web"
    id_to_path = {}
    for path in web.rglob("*.md"):
        if path.name == "INDEX.md":
            continue
        fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
        for line in fm.splitlines():
            if line.startswith("id:"):
                id_to_path[line.split(":", 1)[1].strip()] = path.relative_to(root).as_posix()
                break
    return id_to_path


def id_to_relpath(nid, src_path, root, id_to_path):
    """Relative link target from the citing file to the node's REAL file (POSIX separators)."""
    rel_from_root = id_to_path.get(nid)
    if rel_from_root is None:
        return None
    target = pathlib.Path(root) / rel_from_root
    return os.path.relpath(target, pathlib.Path(src_path).parent).replace(os.sep, "/")


def node_id_from_target(target, src_path, root, path_to_id):
    """Recover a node id from a link target by resolving it to a real file under web/.

    Returns the id of the node the link points at, or None if it resolves to no known node.
    """
    resolved = (pathlib.Path(src_path).parent / target).resolve()
    try:
        rel = resolved.relative_to(pathlib.Path(root).resolve()).as_posix()
    except ValueError:
        return None
    return path_to_id.get(rel)


def wrap_bare_ids(body, id_set):
    """Migration step: wrap bare/parenthesised id mentions in `[[ ]]`, skipping protected spans.

    Only strings that EXACTLY equal a real node id are wrapped, so there are no false positives.
    Idempotent: ids already inside `[[…]]`, `](…)`, or `` ` ` `` are left alone.
    """
    def wrap_plain(text):
        return _ID_TOKEN_RE.sub(
            lambda m: f"[[{m.group(1)}]]" if m.group(1) in id_set else m.group(0), text)

    out, last = [], 0
    for m in _PROTECT_RE.finditer(body):
        out.append(wrap_plain(body[last:m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(wrap_plain(body[last:]))
    return "".join(out)


def bare_ids_in(body, id_set):
    """Unwrapped, unlinked id mentions in body prose (skips protected spans). For lint warnings."""
    found, last = [], 0
    for m in _PROTECT_RE.finditer(body):
        found += [t for t in _ID_TOKEN_RE.findall(body[last:m.start()]) if t in id_set]
        last = m.end()
    found += [t for t in _ID_TOKEN_RE.findall(body[last:]) if t in id_set]
    return found


def render_body(body, src_path, root, id_to_path):
    """Expand `[[id]]` -> `[slug](relpath)` and refresh existing web links. Returns (body, reports).

    Idempotent. A custom alias (`[[id|label]]`, or a hand-written non-slug label) is preserved;
    only its path is refreshed. Targets resolve through the real id->path map (rename-safe).
    """
    reports = []
    path_to_id = {p: i for i, p in id_to_path.items()}

    def expand(m):
        nid = m.group(1)
        alias = m.group(2)[1:].strip() if m.group(2) else None
        if nid not in id_to_path:
            reports.append(f"unknown [[{nid}]] in body")
            return m.group(0)
        label = alias if alias else slug_of(nid)
        return f"[{label}]({id_to_relpath(nid, src_path, root, id_to_path)})"

    body = WIKILINK_RE.sub(expand, body)

    def refresh(m):
        label, target = m.group(1), m.group(2)
        nid = node_id_from_target(target, src_path, root, path_to_id)
        if nid is None:
            if _WEBISH_RE.search(target):
                reports.append(f"dangling body link [{label}]({target})")
            return m.group(0)
        new_label = slug_of(nid) if label in (slug_of(nid), nid) else label
        return f"[{new_label}]({id_to_relpath(nid, src_path, root, id_to_path)})"

    body = MDLINK_RE.sub(refresh, body)
    return body, reports
