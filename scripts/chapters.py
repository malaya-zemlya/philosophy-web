#!/usr/bin/env python3
"""Book chapters: the hand-ordered grouping of web nodes into the encyclopedia's chapters.

A chapter is an *editorial* object, not a web node: it asserts nothing and owns no graph edge, so
it lives in `book/chapters/<NN>-<slug>.md`, outside `web/`. Each file has frontmatter

    id: chapter-<slug>
    type: chapter
    kind: front | body | back        # front matter, a numbered chapter, or an appendix
    title: <Chapter title>
    entries:                          # hand-ordered, basic -> advanced
      - concept-x                     # a top-level entry
      - argument-y:                   # an entry with its claims set as sub-entries under it
          - claim-a
          - claim-b

and a Markdown body that is the chapter's introduction (`[[id]]` links allowed; lint renders them).
Chapters print in (kind, filename) order: front, then body, then back.

Every encyclopedia-style content node belongs in exactly one chapter (its "home"); everywhere else
it is reached by cross-reference. Only a claim may be nested, and only under an argument whose
premise/conclusion it is or a position that commits to / rejects it.

CLI (prefer the make targets):
    uv run python scripts/chapters.py check            # validate (lint runs this too)
    uv run python scripts/chapters.py unplaced         # content nodes not yet in any chapter
    uv run python scripts/chapters.py suggest <id>     # which chapter + neighbours fit a node
"""
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "book" / "chapters"
WEB = ROOT / "web"
KINDS = ("front", "body", "back")
CONTENT_TYPES = {"concept", "claim", "argument", "question", "position"}
FM_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


@dataclass
class Chapter:
    id: str
    kind: str
    title: str
    path: Path
    body: str
    # (top-level id, [nested claim ids]) in printed order
    entries: List[Tuple[str, List[str]]] = field(default_factory=list)

    @property
    def all_ids(self) -> List[str]:
        return [x for top, kids in self.entries for x in [top] + kids]


def _as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def load_chapters(root: Path = ROOT) -> Tuple[List[Chapter], List[str]]:
    """Parse book/chapters/*.md -> (chapters in print order, parse errors)."""
    d = root / "book" / "chapters"
    chapters, errors = [], []
    if not d.is_dir():
        return chapters, errors
    for path in sorted(d.glob("*.md")):
        if path.name.startswith(("_", "README")):
            continue
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        m = FM_RE.match(text)
        if not m:
            errors.append(f"CHAPTER no frontmatter: {rel}")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"CHAPTER YAML error in {rel}: {e}")
            continue
        kind = fm.get("kind", "body")
        if kind not in KINDS:
            errors.append(f"CHAPTER unknown kind '{kind}' (front|body|back): {rel}")
        entries = []
        for item in _as_list(fm.get("entries")):
            if isinstance(item, str):
                entries.append((item, []))
            elif isinstance(item, dict) and len(item) == 1:
                (top, kids), = item.items()
                entries.append((str(top), [str(k) for k in _as_list(kids)]))
            else:
                errors.append(f"CHAPTER malformed entry {item!r} (an id, or one `id: [claims]`): {rel}")
        chapters.append(Chapter(id=str(fm.get("id") or path.stem), kind=kind,
                                title=str(fm.get("title") or path.stem), path=path,
                                body=text[m.end():].strip("\n"), entries=entries))
    chapters.sort(key=lambda c: (KINDS.index(c.kind) if c.kind in KINDS else 9, c.path.name))
    return chapters, errors


def load_web(root: Path = ROOT) -> Dict[str, dict]:
    """id -> frontmatter for every web node (just what validation needs)."""
    out = {}
    for path in (root / "web").rglob("*.md"):
        m = FM_RE.match(path.read_text(encoding="utf-8"))
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        if fm.get("id"):
            out[fm["id"]] = fm
    return out


def nesting_ok(child: str, parent: str, web: Dict[str, dict]) -> bool:
    """Is there an edge licensing `child` to print as a sub-entry of `parent`?"""
    p = web.get(parent, {})
    if p.get("type") == "argument":
        return child in _as_list(p.get("premise")) + _as_list(p.get("concludes"))
    if p.get("type") == "position":
        return child in _as_list(p.get("commits_to")) + _as_list(p.get("rejects"))
    return False


def home_of(chapters: List[Chapter]) -> Dict[str, Tuple[Chapter, Optional[str]]]:
    """id -> (its chapter, its parent id or None)."""
    out = {}
    for ch in chapters:
        for top, kids in ch.entries:
            out.setdefault(top, (ch, None))
            for k in kids:
                out.setdefault(k, (ch, top))
    return out


def validate(chapters: List[Chapter], web: Dict[str, dict]) -> Tuple[List[str], List[str]]:
    """-> (errors, warnings). Errors: dangling ids, double placement, illegal nesting.
    Warnings: nesting without a licensing edge, encyclopedia content nodes in no chapter."""
    errors, warnings = [], []
    seen: Dict[str, str] = {}
    ids_seen: Dict[str, str] = {}
    for ch in chapters:
        rel = ch.path.relative_to(ROOT)
        if ch.id in ids_seen:
            errors.append(f"CHAPTER duplicate chapter id '{ch.id}': {rel} and {ids_seen[ch.id]}")
        ids_seen[ch.id] = str(rel)
        for top, kids in ch.entries:
            for x in [top] + kids:
                if x not in web:
                    errors.append(f"CHAPTER dangling entry '{x}' (no such node): {rel}")
                elif x in seen:
                    errors.append(f"CHAPTER '{x}' placed twice: {seen[x]} and {rel}")
                else:
                    seen[x] = str(rel)
            for k in kids:
                if k in web and web[k].get("type") != "claim":
                    errors.append(f"CHAPTER only claims may be nested; '{k}' is a "
                                  f"{web[k].get('type')}: {rel}")
                elif k in web and top in web and not nesting_ok(k, top, web):
                    warnings.append(f"chapter nesting without an edge: '{k}' under '{top}' "
                                    f"(not its premise/conclusion/commitment): {rel}")
    unplaced = unplaced_ids(chapters, web)
    if unplaced:
        warnings.append(f"{len(unplaced)} encyclopedia node(s) in no book chapter "
                        f"(`make chapters-unplaced`; place with `make chapter-suggest ID=…`): "
                        + ", ".join(unplaced[:8]) + (" …" if len(unplaced) > 8 else ""))
    return errors, warnings


def unplaced_ids(chapters: List[Chapter], web: Dict[str, dict]) -> List[str]:
    placed = {x for ch in chapters for x in ch.all_ids}
    return sorted(i for i, fm in web.items()
                  if fm.get("type") in CONTENT_TYPES and fm.get("style") == "encyclopedia"
                  and i not in placed)


# --- suggest: where a new node fits (embedding centroid of each chapter's members) ----------
def _vectors(root: Path = ROOT):
    import numpy as np
    vec = {}
    p = root / "embeddings" / "web.jsonl"
    for line in p.open(encoding="utf-8"):
        r = json.loads(line)
        v = np.array(r["vec"], dtype=float)
        vec[r["id"]] = v / (np.linalg.norm(v) or 1.0)
    return vec


def suggest(nid: str, chapters: List[Chapter], web: Dict[str, dict], k: int = 3) -> str:
    import numpy as np
    vec = _vectors()
    if nid not in vec:
        return f"'{nid}' has no embedding yet — run `make embed` first."
    v = vec[nid]
    lines = []
    # structural hint: chapters of the nodes this one points at
    fm = web.get(nid, {})
    homes = home_of(chapters)
    targets = [t for e in ("premise", "concludes", "attacks", "supports", "responds_to",
                           "answers", "commits_to", "rejects", "uses_concept")
               for t in _as_list(fm.get(e))]
    linked = sorted({homes[t][0].path.name for t in targets if t in homes})
    if linked:
        lines.append("edges point into: " + ", ".join(linked))
    if fm.get("type") == "claim":
        parents = [i for i, f in web.items() if nesting_ok(nid, i, web)]
        if parents:
            lines.append("could nest under: " + ", ".join(parents))
    scored = []
    for ch in chapters:
        mem = [x for x in ch.all_ids if x in vec and x != nid]
        if not mem:
            continue
        c = np.mean([vec[x] for x in mem], 0)
        c /= np.linalg.norm(c)
        nearest = max(mem, key=lambda x: float(v @ vec[x]))
        scored.append((float(v @ c), ch, nearest))
    scored.sort(key=lambda t: -t[0])
    for s, ch, near in scored[:k]:
        lines.append(f"{s:.3f}  {ch.path.relative_to(ROOT)}  — nearest member: {near}")
    return "\n".join(lines)


def main(argv: List[str]) -> int:
    cmd = argv[0] if argv else "check"
    chapters, perr = load_chapters()
    web = load_web()
    if cmd == "check":
        errors, warnings = validate(chapters, web)
        errors = perr + errors
        n = sum(len(c.all_ids) for c in chapters)
        print(f"chapters: {len(chapters)}   placed nodes: {n}")
        for e in errors:
            print("  ERROR", e)
        for w in warnings:
            print("  warn ", w)
        return 1 if errors else 0
    if cmd == "unplaced":
        for i in unplaced_ids(chapters, web):
            print(i)
        return 0
    if cmd == "suggest" and len(argv) > 1:
        print(suggest(argv[1], chapters, web))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
