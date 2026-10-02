#!/usr/bin/env python3
"""Crop a raster image to an exact 2.39:1 frame without stretching.

ffmpeg port of cinematic-director-frame's PIL-based crop_to_scope.py, so the
skill keeps a single external dependency (ffmpeg) shared with
compose_nine_shot_storyboard.py. Geometry is identical: the largest 239:100
window that fits inside the source, positioned by normalized anchors.

Requires ffmpeg and ffprobe on PATH. No Python packages needed.

    python3 -X utf8 scripts/crop_to_scope.py INPUT OUTPUT --anchor-x 0.5 --anchor-y 0.5
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

BASE_WIDTH = 239
BASE_HEIGHT = 100


def clamp(value):
    return max(0.0, min(1.0, value))


def probe_size(path):
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height", "-of", "json", str(path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"ffprobe failed:\n{result.stderr.strip()}")
    stream = json.loads(result.stdout)["streams"][0]
    return int(stream["width"]), int(stream["height"])


def crop_box(width, height, anchor_x, anchor_y):
    """Return (left, top, crop_width, crop_height) for the largest exact 239:100 window."""
    if width * BASE_HEIGHT == height * BASE_WIDTH:
        return 0, 0, width, height
    scale = min(width // BASE_WIDTH, height // BASE_HEIGHT)
    if scale < 1:
        raise SystemExit("Input is too small for an exact 239:100 crop")
    crop_width = BASE_WIDTH * scale
    crop_height = BASE_HEIGHT * scale
    left = int(round((width - crop_width) * clamp(anchor_x)))
    top = int(round((height - crop_height) * clamp(anchor_y)))
    left = max(0, min(left, width - crop_width))
    top = max(0, min(top, height - crop_height))
    return left, top, crop_width, crop_height


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--anchor-x", type=float, default=0.5,
                        help="0 keeps the left edge, 1 keeps the right edge (default 0.5)")
    parser.add_argument("--anchor-y", type=float, default=0.5,
                        help="0 keeps the top edge, 1 keeps the bottom edge (default 0.5)")
    args = parser.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            raise SystemExit(f"{tool} not found on PATH; install ffmpeg or crop with an equivalent tool.")
    if not args.input.is_file():
        raise SystemExit(f"Input not found: {args.input}")

    width, height = probe_size(args.input)
    left, top, crop_width, crop_height = crop_box(width, height, args.anchor_x, args.anchor_y)
    args.output.parent.mkdir(parents=True, exist_ok=True)

    result = subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(args.input),
            "-vf", f"crop={crop_width}:{crop_height}:{left}:{top}",
            "-frames:v", "1", str(args.output),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg failed:\n{result.stderr.strip()}")

    summary = {
        "Input": str(args.input),
        "Output": str(args.output),
        "SourceSize": [width, height],
        "CropBox": [left, top, crop_width, crop_height],
        "Ratio": f"{crop_width / crop_height:.4f}:1",
        "Cropped": not (width * BASE_HEIGHT == height * BASE_WIDTH),
    }
    json.dump(summary, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
