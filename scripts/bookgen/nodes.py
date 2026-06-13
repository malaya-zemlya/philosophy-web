"""Load web nodes and resolve a user selection into an ordered list of node ids."""
import os
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional

import weblinks  # sibling top-level script: split_frontmatter, slug_of

from .config import CONTENT_TYPES, FM_RE, ROOT, SKIP_FILES, WEB

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml  "
             "(or: uv run --with pyyaml python scripts/book.py)")


@dataclass
class Node:
    """One web node, as far as the typesetter cares."""
    id: str
    type: str
    title: str
    author: Optional[str]
    status: str
    body: str
    path: str   # absolute path to the .md file

    @property
    def relpath(self) -> str:
        return os.path.relpath(self.path, ROOT).replace(os.sep, "/")


def load_nodes() -> Dict[str, Node]:
    """Scan web/ -> {id: Node}. Bodies keep `[[id]]` shorthand and rendered links alike; both are
    resolved at render time against the full set."""
    nodes: Dict[str, Node] = {}
    for dirpath, _, files in os.walk(WEB):
        for name in files:
            if not name.endswith(".md") or name in SKIP_FILES:
                continue
            path = os.path.join(dirpath, name)
            text = open(path, encoding="utf-8").read()
            m = FM_RE.match(text)
            if not m:
                continue
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError as e:
                print(f"  ! YAML error in {os.path.relpath(path, ROOT)}: {e}", file=sys.stderr)
                continue
            nid = fm.get("id")
            if not nid:
                continue
            _, body = weblinks.split_frontmatter(text)
            nodes[nid] = Node(
                id=nid, type=fm.get("type", "node"),
                title=str(fm.get("title", weblinks.slug_of(nid))),
                author=fm.get("author"), status=fm.get("status", "asserted"),
                body=body.strip("\n"), path=path)
    return nodes


def _slug_index(nodes: Dict[str, Node]):
    """Build the lookup tables resolve_token needs: relpath -> id, and slug -> [ids]."""
    by_path: Dict[str, str] = {}
    by_slug: Dict[str, List[str]] = {}
    for nid, n in nodes.items():
        by_path[n.relpath] = nid
        by_slug.setdefault(weblinks.slug_of(nid), []).append(nid)
    return by_path, by_slug


def resolve_token(tok: str, nodes: Dict[str, Node], by_path, by_slug) -> Optional[str]:
    """A selection token -> node id (or None). Accepts a full id, a .md path, or a bare slug."""
    if tok in nodes:
        return tok
    if tok.endswith(".md") or "/" in tok or os.sep in tok:
        ap = tok if os.path.isabs(tok) else os.path.join(ROOT, tok)
        return by_path.get(os.path.relpath(ap, ROOT).replace(os.sep, "/"))
    hits = by_slug.get(tok)
    if hits and len(hits) == 1:
        return hits[0]
    if hits:
        print(f"  ! ambiguous '{tok}' -> {hits}; qualify with the full id", file=sys.stderr)
    return None


def select_ids(nodes: Dict[str, Node], *, tokens: Iterable[str] = (),
               types: Iterable[str] = (), include_all: bool = False,
               limit: Optional[int] = None) -> List[str]:
    """Resolve explicit tokens and/or type filters into an ordered, de-duplicated id list.

    With neither tokens nor types, defaults to all CONTENT_TYPES (as does include_all)."""
    by_path, by_slug = _slug_index(nodes)
    tokens = list(tokens)
    types = list(types)
    chosen: List[str] = []
    seen = set()

    def add(nid: Optional[str]) -> None:
        if nid and nid not in seen:
            seen.add(nid)
            chosen.append(nid)

    for tok in tokens:
        nid = resolve_token(tok, nodes, by_path, by_slug)
        if nid is None:
            print(f"  ! no node for '{tok}' — skipped", file=sys.stderr)
        else:
            add(nid)

    if include_all or (not tokens and not types):
        types = types + CONTENT_TYPES
    if types:
        wanted = set(types)
        for nid in sorted(nodes):
            if nodes[nid].type in wanted:
                add(nid)

    return chosen[:limit] if limit else chosen
