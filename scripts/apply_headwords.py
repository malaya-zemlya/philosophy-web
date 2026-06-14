#!/usr/bin/env python3
"""Apply the approved headword rename sweep.

Reads `proposals/headword-rename.md` (the single source of truth) and sets each listed node's
`headword:` frontmatter field to the value in the table's third column. Deterministic and
idempotent: running twice changes nothing the second time.

Row contract: a Markdown table row `| <node-id> | <current> | <proposed> |`. Only column 1
(the id, as key) and column 3 (the new headword) are read. A proposed cell that is empty, `SKIP`,
or `—` leaves that node untouched. Node files are located by their frontmatter `id:` (filenames
do not always match the id), so renamed/odd filenames are handled correctly.

Run: `uv run --with pyyaml python scripts/apply_headwords.py`  (add `--check` for a dry run).
"""
import os
import re
import sys
from typing import Dict, Optional, Tuple

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(REPO, "web")
DOC = os.path.join(REPO, "proposals", "headword-rename.md")

ID_RE = re.compile(r"^(concept|claim|position|argument|question)-[a-z0-9-]+$")
SKIP_VALUES = {"", "SKIP", "—", "-"}


def build_id_index() -> Dict[str, str]:
    """Map every node id -> absolute file path by reading frontmatter `id:`."""
    index: Dict[str, str] = {}
    for root, _dirs, files in os.walk(WEB):
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    m = re.match(r"^id:\s*(.+?)\s*$", line)
                    if m:
                        index[m.group(1).strip()] = path
                        break
                    if line.strip() and not line.startswith("---"):
                        break  # past frontmatter without an id
    return index


def parse_doc() -> Dict[str, str]:
    """Return {node-id: proposed-headword} for every actionable row."""
    wanted: Dict[str, str] = {}
    with open(DOC, encoding="utf-8") as fh:
        for line in fh:
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3:
                continue
            node_id, _current, proposed = cells[0], cells[1], cells[2]
            if not ID_RE.match(node_id):
                continue  # header / separator / stray row
            if proposed in SKIP_VALUES:
                continue
            wanted[node_id] = proposed
    return wanted


def needs_quoting(value: str) -> bool:
    # A YAML plain scalar can't safely contain ": " or start with an indicator char.
    if re.search(r":(\s|$)", value):
        return True
    return value[:1] in "!&*[]{}#|>%@`\"',?-"


def yaml_value(value: str) -> str:
    if needs_quoting(value):
        return '"' + value.replace('"', '\\"') + '"'
    return value


def set_headword(path: str, headword: str) -> Tuple[str, Optional[str]]:
    """Return (action, old_value). action in {set-new, replaced, unchanged}."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: no frontmatter")
    # locate frontmatter bounds
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    new_line = f"headword: {yaml_value(headword)}\n"

    hw_idx = title_idx = None
    for i in range(1, end):
        if lines[i].startswith("headword:"):
            hw_idx = i
        elif lines[i].startswith("title:"):
            title_idx = i

    if hw_idx is not None:
        old = lines[hw_idx][len("headword:"):].strip().strip('"')
        if lines[hw_idx] == new_line:
            return ("unchanged", old)
        lines[hw_idx] = new_line
        action = "replaced"
        old_value: Optional[str] = old
    else:
        insert_at = (title_idx + 1) if title_idx is not None else end
        lines.insert(insert_at, new_line)
        action, old_value = "set-new", None

    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)
    return (action, old_value)


def main() -> int:
    check = "--check" in sys.argv
    index = build_id_index()
    wanted = parse_doc()

    missing = sorted(set(wanted) - set(index))
    no_headword = sorted(set(index) - set(wanted) - {None})
    counts = {"set-new": 0, "replaced": 0, "unchanged": 0}

    for node_id, headword in sorted(wanted.items()):
        path = index.get(node_id)
        if path is None:
            continue
        if check:
            # dry run: report intended action without writing
            with open(path, encoding="utf-8") as fh:
                has = any(l.startswith("headword:") for l in fh)
            counts["replaced" if has else "set-new"] += 1
            continue
        action, _old = set_headword(path, headword)
        counts[action] += 1

    print(f"rows actioned: {len(wanted)}   "
          f"set-new: {counts['set-new']}  replaced: {counts['replaced']}  "
          f"unchanged: {counts['unchanged']}" + ("   [--check dry run]" if check else ""))
    if missing:
        print(f"WARNING: {len(missing)} id(s) in doc not found in web/: {', '.join(missing)}")
    content_no_hw = [i for i in no_headword if i and ID_RE.match(i)]
    if content_no_hw:
        print(f"note: {len(content_no_hw)} content node(s) not listed in the doc "
              f"(left as-is): {', '.join(content_no_hw)}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
