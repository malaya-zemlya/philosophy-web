"""Command-line interface: parse arguments, select nodes, build the .tex, compile the PDF."""
import argparse
import os
import sys
from typing import List, Optional

from .compile import compile_pdf, find_engine
from .config import BookOptions, BUILDDIR, OUTDIR, ROOT
from .document import build_document
from .nodes import load_nodes, select_ids


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="book.py", description="Typeset web nodes as a printable encyclopedia (LaTeX -> PDF).")
    sel = ap.add_argument_group("selection (combine freely; default = all content nodes)")
    sel.add_argument("ids", nargs="*", help="node ids, slugs, or .md paths to include")
    sel.add_argument("--from", dest="from_file", metavar="FILE",
                     help="read ids/slugs/paths, one per line (# comments allowed)")
    sel.add_argument("--type", help="include every node of these comma-separated types")
    sel.add_argument("--all", action="store_true",
                     help="all content nodes (concept, claim, argument, question, position)")
    sel.add_argument("--limit", type=int, help="cap the number of entries (quick test builds)")

    fmt = ap.add_argument_group("formatting")
    fmt.add_argument("--sort", choices=["title", "type", "id"], default="title")
    fmt.add_argument("--columns", type=int, choices=[1, 2], default=2)
    fmt.add_argument("--title", default=BookOptions.title)
    fmt.add_argument("--subtitle", default=BookOptions.subtitle)
    fmt.add_argument("--running-head", help="short title for the page header (defaults to --title)")
    fmt.add_argument("--no-attribution", action="store_true",
                     help="omit the 'after <Author>' line under each headword")
    fmt.add_argument("--paper", default=BookOptions.paper, help="a4paper, letterpaper, …")
    fmt.add_argument("--margin", default=BookOptions.margin)
    fmt.add_argument("--twoside", action="store_true", help="two-sided layout (mirror margins)")

    out = ap.add_argument_group("output")
    out.add_argument("--engine", default="auto",
                     help="tectonic|latexmk|xelatex|lualatex|pdflatex|auto (default auto)")
    out.add_argument("--no-pdf", action="store_true", help="write the .tex only; never compile")
    out.add_argument("--output", default=os.path.join(OUTDIR, "encyclopedia.tex"),
                     help="output .tex path (the .pdf lands beside it)")
    return ap


def _options(args: argparse.Namespace) -> BookOptions:
    return BookOptions(
        title=args.title, subtitle=args.subtitle, running_head=args.running_head,
        columns=args.columns, sort=args.sort, attribution=not args.no_attribution,
        twoside=args.twoside, paper=args.paper, margin=args.margin)


def _tokens(args: argparse.Namespace) -> List[str]:
    tokens = list(args.ids)
    if args.from_file:
        for line in open(args.from_file, encoding="utf-8"):
            line = line.split("#", 1)[0].strip()
            if line:
                tokens.append(line)
    return tokens


def main(argv: Optional[List[str]] = None) -> None:
    args = build_parser().parse_args(argv)

    nodes = load_nodes()
    if not nodes:
        sys.exit("no nodes found under web/")
    types = [t.strip() for t in args.type.split(",")] if args.type else []
    ids = select_ids(nodes, tokens=_tokens(args), types=types,
                     include_all=args.all, limit=args.limit)
    if not ids:
        sys.exit("selection is empty — nothing to typeset")

    doc = build_document(ids, nodes, _options(args))
    tex_path = args.output if os.path.isabs(args.output) else os.path.join(ROOT, args.output)
    os.makedirs(os.path.dirname(tex_path), exist_ok=True)
    open(tex_path, "w", encoding="utf-8").write(doc)
    print(f"entries: {len(ids)}   wrote {os.path.relpath(tex_path, ROOT)}")

    if args.no_pdf:
        return
    engine = find_engine(args.engine)
    if not engine:
        print("no LaTeX engine found — wrote .tex only. Install tectonic (recommended) or a TeX\n"
              "distribution (mactex-no-gui / texlive-xetex), then re-run or compile the .tex.")
        return
    print(f"compiling with {os.path.basename(engine)} ...")
    ok, log = compile_pdf(engine, tex_path, BUILDDIR)
    pdf = os.path.splitext(tex_path)[0] + ".pdf"
    if ok and os.path.exists(pdf):
        print(f"built {os.path.relpath(pdf, ROOT)}")
    else:
        sys.exit(f"compile failed ({os.path.basename(engine)}). The .tex is fine; last log lines:\n{log}")
