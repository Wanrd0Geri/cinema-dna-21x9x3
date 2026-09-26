#!/usr/bin/env python3
"""Compose 9 independently generated shots into 3 triptychs and one 3x3 contact sheet.

Python + ffmpeg port of compose-nine-shot-storyboard.ps1, whose PowerShell
`System.Drawing` backend is Windows-only. Geometry, fit-contain centering on
black, file naming and the summary payload are kept identical.

Requires ffmpeg on PATH. No Python packages needed.

    python3 scripts/compose_nine_shot_storyboard.py \
        --sources a.png b.png ... i.png \
        --output-dir ./output/story-name --prefix story-name
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

TRIPTYCH_ASPECT = 2.39
PREFIX_RE = re.compile(r"^[a-zA-Z0-9_-]+$")


def run_ffmpeg(args):
    result = subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", *args],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg failed:\n{result.stderr.strip()}")


def fit_overlay_graph(cells, cell_width, cell_height):
    """Build a filter_complex that draws each source fit-contained and centered.

    `cells` is a list of (x, y) canvas positions; input 0 is the black canvas
    and inputs 1..n are the images, matching the order of `cells`.
    """
    parts = []
    for index in range(len(cells)):
        parts.append(
            f"[{index + 1}:v]scale={cell_width}:{cell_height}"
            f":force_original_aspect_ratio=decrease:flags=lanczos[s{index}]"
        )
    current = "[0:v]"
    for index, (x, y) in enumerate(cells):
        target = "[out]" if index == len(cells) - 1 else f"[c{index}]"
        parts.append(
            f"{current}[s{index}]overlay="
            f"x={x}+({cell_width}-overlay_w)/2:"
            f"y={y}+({cell_height}-overlay_h)/2{target}"
        )
        current = target
    return ";".join(parts)


def compose(sources, cells, canvas_width, canvas_height, cell_width, cell_height, out_path):
    args = ["-f", "lavfi", "-i", f"color=c=black:s={canvas_width}x{canvas_height}:d=1"]
    for source in sources:
        args += ["-i", str(source)]
    args += [
        "-filter_complex", fit_overlay_graph(cells, cell_width, cell_height),
        "-map", "[out]", "-frames:v", "1", str(out_path),
    ]
    run_ffmpeg(args)


def main():
    parser = argparse.ArgumentParser(description="Compose a nine-shot storyboard.")
    parser.add_argument("--sources", nargs="+", required=True, help="exactly 9 source images")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--cell-width", type=int, default=960)
    parser.add_argument("--cell-height", type=int, default=402)
    parser.add_argument("--gap", type=int, default=8)
    args = parser.parse_args()

    if len(args.sources) != 9:
        raise SystemExit(f"Exactly 9 source images are required; received {len(args.sources)}.")
    if not PREFIX_RE.match(args.prefix):
        raise SystemExit("--prefix must match ^[a-zA-Z0-9_-]+$")
    if not 320 <= args.cell_width <= 3840:
        raise SystemExit("--cell-width must be between 320 and 3840")
    if not 134 <= args.cell_height <= 1607:
        raise SystemExit("--cell-height must be between 134 and 1607")
    if not 0 <= args.gap <= 64:
        raise SystemExit("--gap must be between 0 and 64")
    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg not found on PATH; install it or compose with an equivalent tool.")

    sources = [Path(s) for s in args.sources]
    for source in sources:
        if not source.is_file():
            raise SystemExit(f"Missing source image: {source}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Per-shot copies. The PowerShell original byte-copied a JPEG to a .png
    #    name; this re-encodes so the extension matches the actual format.
    shot_paths = []
    for index, source in enumerate(sources, start=1):
        destination = output_dir / f"{args.prefix}_shot{index:02d}.png"
        run_ffmpeg(["-i", str(source), "-frames:v", "1", str(destination)])
        shot_paths.append(destination)

    # 2. Three stacked triptychs, each cell at 2.39:1.
    triptych_width = args.cell_width * 2
    triptych_cell_height = round(triptych_width / TRIPTYCH_ASPECT)
    triptych_height = triptych_cell_height * 3 + args.gap * 2
    triptych_paths = []
    for group in range(3):
        cells = [(0, slot * (triptych_cell_height + args.gap)) for slot in range(3)]
        out_path = output_dir / f"{args.prefix}_triptych_{group + 1}.png"
        compose(
            sources[group * 3:group * 3 + 3], cells,
            triptych_width, triptych_height,
            triptych_width, triptych_cell_height, out_path,
        )
        triptych_paths.append(out_path)

    # 3. One 3x3 contact sheet.
    sheet_width = args.cell_width * 3 + args.gap * 2
    sheet_height = args.cell_height * 3 + args.gap * 2
    sheet_cells = [
        ((i % 3) * (args.cell_width + args.gap), (i // 3) * (args.cell_height + args.gap))
        for i in range(9)
    ]
    sheet_path = output_dir / f"{args.prefix}_3x3_contact_sheet.png"
    compose(
        sources, sheet_cells, sheet_width, sheet_height,
        args.cell_width, args.cell_height, sheet_path,
    )

    print(json.dumps({
        "SourceCount": 9,
        "ShotCount": sum(1 for p in shot_paths if p.is_file()),
        "TriptychCount": sum(1 for p in triptych_paths if p.is_file()),
        "ContactSheet": str(sheet_path),
        "ContactWidth": sheet_width,
        "ContactHeight": sheet_height,
        "TriptychWidth": triptych_width,
        "TriptychHeight": triptych_height,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
