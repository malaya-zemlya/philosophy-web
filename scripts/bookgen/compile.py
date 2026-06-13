"""Locate a LaTeX engine and run it.

Mirrors how scripts/graph.py treats the Graphviz `dot` binary: optional. The caller always has a
valid .tex; this module just turns it into a PDF when an engine is available, searching PATH and
the usual TeX bin dirs (so a freshly-installed MacTeX works before the shell is restarted).

All engine intermediates (.aux/.log/.fls/.fdb_latexmk/.xdv/…) are written to a separate build
directory so the deliverables — the .tex and the .pdf — are all that land beside the output path.
"""
import os
import shutil
import subprocess
from shutil import which
from typing import List, Optional, Tuple

# Tried in order for --engine auto. tectonic first: it fetches packages on demand, so a fresh
# machine needs nothing else. latexmk handles the multi-pass dance (labels / guide words).
ENGINE_CANDIDATES = ["tectonic", "latexmk", "xelatex", "lualatex", "pdflatex"]

# Where TeX distributions place binaries when they aren't on PATH yet.
TEX_BIN_DIRS = ["/Library/TeX/texbin", "/usr/local/texlive/2024/bin/universal-darwin",
                "/opt/homebrew/bin", "/usr/local/bin"]


def _locate(name: str) -> Optional[str]:
    found = which(name)
    if found:
        return found
    for d in TEX_BIN_DIRS:
        cand = os.path.join(d, name)
        if os.path.exists(cand):
            return cand
    return None


def find_engine(requested: str = "auto") -> Optional[str]:
    """Path to the engine to use, or None. `requested` may name one explicitly or be 'auto'."""
    if requested and requested != "auto":
        return _locate(requested)
    for name in ENGINE_CANDIDATES:
        path = _locate(name)
        if path:
            return path
    return None


def _commands(engine_path: str, base: str, outdir: str) -> List[List[str]]:
    """Engine invocations that send all output to `outdir` (each engine spells the flag its way)."""
    name = os.path.basename(engine_path)
    if name == "latexmk":
        return [[engine_path, "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
                 "-output-directory=" + outdir, base]]
    if name == "tectonic":
        return [[engine_path, "--outdir", outdir, base]]
    run = [engine_path, "-interaction=nonstopmode", "-halt-on-error",
           "-output-directory=" + outdir, base]
    return [run, run]  # two passes resolve \label / \pageref / guide words


def _engine_env(engine_path: str) -> dict:
    """A copy of the environment with the engine's bin dir on PATH, so wrappers like latexmk can
    find the sibling binaries (xelatex, …) they shell out to even when PATH is bare."""
    env = dict(os.environ)
    extra = [os.path.dirname(os.path.abspath(engine_path))] + TEX_BIN_DIRS
    env["PATH"] = os.pathsep.join(extra + [env.get("PATH", "")])
    return env


def compile_pdf(engine_path: str, tex_path: str, build_dir: str) -> Tuple[bool, str]:
    """Compile tex_path to a sibling .pdf, keeping intermediates in build_dir.

    Returns (ok, last_log_lines_on_failure). On success the finished PDF is moved out of build_dir
    to sit beside the .tex; everything else stays in build_dir."""
    workdir = os.path.dirname(tex_path)
    base = os.path.basename(tex_path)
    os.makedirs(build_dir, exist_ok=True)
    env = _engine_env(engine_path)
    for cmd in _commands(engine_path, base, build_dir):
        try:
            r = subprocess.run(cmd, cwd=workdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               env=env)
        except OSError as e:
            return False, str(e)
        if r.returncode != 0:
            tail = r.stdout.decode("utf-8", "replace").splitlines()[-30:]
            return False, "\n".join(tail)

    built = os.path.join(build_dir, os.path.splitext(base)[0] + ".pdf")
    final = os.path.splitext(tex_path)[0] + ".pdf"
    if not os.path.exists(built):
        return False, "engine reported success but produced no PDF in %s" % build_dir
    if os.path.abspath(built) != os.path.abspath(final):
        shutil.move(built, final)
    return True, ""
