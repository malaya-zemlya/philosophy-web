#!/usr/bin/env python3
"""
migrate_links.py — ONE-TIME migration to clickable cross-references.

Wraps existing bare / parenthesised id mentions in node bodies and transcripts with the `[[id]]`
shorthand. Only strings that EXACTLY equal a real node id are wrapped (no false positives); spans
already inside `[[…]]`, `[…](…)`, or `` `code` `` are left untouched. Frontmatter is never changed.

After this runs, `scripts/lint.py` renders the `[[id]]` shorthand into clickable `[slug](relpath)`
links. So the full migration is:

    python scripts/migrate_links.py --dry-run     # review the unified diff
    python scripts/migrate_links.py               # apply the [[id]] wrapping
    .venv/bin/python scripts/lint.py              # render [[id]] -> clickable links

This is a throwaway script kept in history for provenance; everyday maintenance is lint's job.
"""
import sys, os, difflib, pathlib
import weblinks

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
TRANSCRIPTS = ROOT / "transcripts"


def node_id_set():
    ids = set()
    for path in WEB.rglob("*.md"):
        if path.name == "INDEX.md":
            continue
        fm, _ = weblinks.split_frontmatter(path.read_text(encoding="utf-8"))
        for line in fm.splitlines():
            if line.startswith("id:"):
                ids.add(line.split(":", 1)[1].strip())
                break
    return ids


def main():
    dry = "--dry-run" in sys.argv[1:]
    id_set = node_id_set()
    files = sorted(WEB.rglob("*.md")) + (sorted(TRANSCRIPTS.rglob("*.md"))
                                         if TRANSCRIPTS.is_dir() else [])
    changed = 0
    for path in files:
        if path.name == "INDEX.md":
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = weblinks.split_frontmatter(text)
        new_body = weblinks.wrap_bare_ids(body, id_set)
        if new_body == body:
            continue
        changed += 1
        rel = path.relative_to(ROOT)
        if dry:
            diff = difflib.unified_diff(body.splitlines(True), new_body.splitlines(True),
                                        fromfile=str(rel), tofile=str(rel))
            sys.stdout.writelines(diff)
        else:
            path.write_text(fm + new_body, encoding="utf-8")
    print(f"\n{'would wrap' if dry else 'wrapped'} ids in {changed} file(s) "
          f"({len(id_set)} known ids).")
    if dry:
        print("review above, then run without --dry-run, then run scripts/lint.py")


if __name__ == "__main__":
    main()
