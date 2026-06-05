#!/usr/bin/env python3
"""
graph.py — render the philosophy web as a Graphviz SVG you can view on GitHub.

Draws the dialectic: claims, arguments and concepts, plus the two governing questions as anchors,
with the relations among them (premise / concludes / supports / attacks / responds_to / answers /
uses_concept). Nodes are coloured by type; edges by relation. Output lands in graph/web.{dot,svg}.

Pure Python + the existing parsing in weblinks.py / lint.py; the only external dependency is the
Graphviz `dot` binary, which the script shells out to and degrades gracefully without.

    .venv/bin/python scripts/graph.py            # write graph/web.dot and graph/web.svg
    .venv/bin/python scripts/graph.py --engine sfdp --png   # try a force-directed layout + a PNG

Install Graphviz: brew install graphviz  (macOS) · apt-get install graphviz (Debian) ·
dnf install graphviz (Fedora).
"""
import sys
import shutil
import argparse
import subprocess
import pathlib

import weblinks                      # split_frontmatter, build_id_to_path, slug_of
from lint import parse, as_list      # frontmatter parse + edge-list normaliser (no side effects)

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEB = ROOT / "web"

# what to draw
NODE_TYPES = {"claim", "argument", "concept", "question"}
EDGE_TYPES = ["premise", "concludes", "supports", "attacks", "responds_to", "answers", "uses_concept"]

# colour by node type
NODE_STYLE = {
    "claim":    {"shape": "box", "style": "filled,rounded", "fillcolor": "#cfe0f5", "color": "#5b8fbf"},
    "argument": {"shape": "box", "style": "filled", "fillcolor": "#eeeeee", "color": "#888888"},
    "concept":  {"shape": "ellipse", "style": "filled", "fillcolor": "#e8dff5", "color": "#9a78c0"},
    "question": {"shape": "doubleoctagon", "style": "filled,bold", "fillcolor": "#fff2cc", "color": "#bfa400"},
}
# colour / line by relation
EDGE_STYLE = {
    "supports":     {"color": "#2e7d32", "penwidth": "1.6"},
    "attacks":      {"color": "#c62828", "penwidth": "1.6"},
    "responds_to":  {"color": "#757575", "style": "dashed"},
    "premise":      {"color": "#1565c0"},
    "concludes":    {"color": "#222222", "penwidth": "1.8"},
    "answers":      {"color": "#9e9e9e", "style": "dotted", "arrowhead": "onormal"},
    "uses_concept": {"color": "#cccccc", "style": "dotted", "arrowhead": "none", "penwidth": "0.6"},
}

LEGEND = """  legend [shape=plaintext, fontsize=10, label=<
    <table border="1" cellborder="0" cellspacing="3" cellpadding="2" bgcolor="white">
      <tr><td colspan="2"><b>Legend</b></td></tr>
      <tr><td bgcolor="#cfe0f5">claim</td><td bgcolor="#eeeeee">argument</td></tr>
      <tr><td bgcolor="#e8dff5">concept</td><td bgcolor="#fff2cc">question</td></tr>
      <tr><td><font color="#2e7d32"><b>&#8594;</b></font> supports</td><td><font color="#c62828"><b>&#8594;</b></font> attacks</td></tr>
      <tr><td><font color="#757575">&#8594; responds_to</font></td><td><font color="#1565c0">&#8594; premise</font></td></tr>
      <tr><td><b>&#8594;</b> concludes</td><td><font color="#9e9e9e">&#8594; answers / uses_concept</font></td></tr>
    </table>
  >];"""


def wrap_label(slug, width=18):
    """slug -> human-ish label, dashes to spaces, soft-wrapped onto short lines."""
    lines, cur = [], ""
    for w in slug.replace("-", " ").split():
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return "\\n".join(lines)


def esc(v):
    return str(v).replace("\\", "\\\\").replace('"', '\\"')


def fmt_attrs(attrs):
    # `label` is pre-built (slug + \n escapes) and must not be re-escaped; everything else is.
    parts = []
    for k, v in attrs.items():
        parts.append(f'label="{v}"' if k == "label" else f'{k}="{esc(v)}"')
    return ", ".join(parts)


def collect():
    """{id: frontmatter} for kept types, and the list of (src, tgt, edge) among kept nodes."""
    nodes = {}
    for path in sorted(WEB.rglob("*.md")):
        if path.name in ("INDEX.md", "README.md"):
            continue
        fm = parse(path)
        if fm and fm.get("id") and fm.get("type") in NODE_TYPES:
            nodes[fm["id"]] = fm
    edges = []
    for nid, fm in nodes.items():
        for et in EDGE_TYPES:
            for tgt in as_list(fm.get(et)):
                if tgt in nodes:
                    edges.append((nid, tgt, et))
    return nodes, sorted(set(edges))


def to_dot(nodes, edges, id_to_path):
    out = [
        "digraph web {",
        '  rankdir=LR;',
        '  graph [overlap=prism, sep="+8", splines=true, nodesep=0.35, ranksep=0.7, fontname="Helvetica", bgcolor="white"];',
        '  node  [fontname="Helvetica", fontsize=10];',
        '  edge  [fontname="Helvetica", fontsize=8, arrowsize=0.7];',
        "",
    ]
    for nid in sorted(nodes):
        fm = nodes[nid]
        attrs = dict(NODE_STYLE[fm["type"]])
        attrs["label"] = wrap_label(weblinks.slug_of(nid))
        attrs["tooltip"] = fm.get("title", nid)
        rel = id_to_path.get(nid)
        if rel:
            attrs["URL"] = "../" + rel        # graph/web.svg -> ../web/<type>s/<slug>.md
        out.append(f'  "{nid}" [{fmt_attrs(attrs)}];')
    out.append("")
    for s, t, et in edges:
        attrs = dict(EDGE_STYLE[et])
        attrs["tooltip"] = et
        out.append(f'  "{s}" -> "{t}" [{fmt_attrs(attrs)}];')
    out.append("")
    out.append(LEGEND)
    out.append("}")
    return "\n".join(out) + "\n"


def render(dot_path, out_path, engine, fmt):
    binary = shutil.which(engine)
    if not binary:
        print(f"graphviz '{engine}' not found — wrote {dot_path.relative_to(ROOT)} only.")
        print("install it:  brew install graphviz  (macOS) · apt-get install graphviz (Debian)")
        return False
    # force-directed engines emit harmless spline-routing warnings on a dense graph; swallow
    # stderr on success, surface it only if dot actually fails.
    proc = subprocess.run([binary, f"-T{fmt}", str(dot_path), "-o", str(out_path)],
                          stderr=subprocess.PIPE, text=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit(f"graphviz '{engine}' failed (exit {proc.returncode})")
    return True


def main():
    ap = argparse.ArgumentParser(description="Render the philosophy web as a Graphviz SVG.")
    ap.add_argument("--engine", default="sfdp", help="graphviz layout engine (sfdp, dot, neato, fdp, circo)")
    ap.add_argument("--out", default=str(ROOT / "graph"), help="output directory")
    ap.add_argument("--png", action="store_true", help="also emit web.png (handy for a quick visual check)")
    args = ap.parse_args()

    nodes, edges = collect()
    id_to_path = weblinks.build_id_to_path(ROOT)

    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    dot_path = outdir / "web.dot"
    dot_path.write_text(to_dot(nodes, edges, id_to_path), encoding="utf-8")

    by_type = {}
    for fm in nodes.values():
        by_type[fm["type"]] = by_type.get(fm["type"], 0) + 1
    print(f"nodes: {len(nodes)} ({', '.join(f'{k}={v}' for k, v in sorted(by_type.items()))})"
          f"   edges: {len(edges)}")

    ok = render(dot_path, outdir / "web.svg", args.engine, "svg")
    if ok:
        print(f"wrote {(outdir / 'web.svg').relative_to(ROOT)} (engine={args.engine})")
        if args.png:
            render(dot_path, outdir / "web.png", args.engine, "png")
            print(f"wrote {(outdir / 'web.png').relative_to(ROOT)}")
    sys.exit(0)


if __name__ == "__main__":
    main()
