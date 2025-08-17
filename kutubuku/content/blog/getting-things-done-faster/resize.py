#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "Pillow",
# ]
# ///

import sys
import os
from pathlib import Path

from PIL import Image


def resize_image(input_path, output_path, target_width=224, target_height=224):
    """Resize image"""
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (handles PNG with alpha, etc.)
            if img.mode != "RGB":
                img = img.convert("RGB")

            # Resize maintaining aspect ratio, then center crop
            img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)

            # Create centered crop if needed
            width, height = img.size
            if width != target_width or height != target_height:
                left = (width - target_width) // 2
                top = (height - target_height) // 2
                right = left + target_width
                bottom = top + target_height
                img = img.crop((left, top, right, bottom))

            Path(os.path.dirname(output_path)).mkdir(parents=True, exist_ok=True)

            img.save(output_path, "JPEG", quality=95)

            print(f"Success processing: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")


if __name__ == "__main__":
    if len(sys.argv) not in [3, 4, 5]:
        print(
            "Usage: python resize_image.py <input_path> <output_path> [width] [height]"
        )
        print("Example: python resize_image.py input.jpg processed/output.jpg 300 300")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Optional width and height parameters
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    height = int(sys.argv[4]) if len(sys.argv) > 4 else 300

    resize_image(input_path, output_path, width, height)
