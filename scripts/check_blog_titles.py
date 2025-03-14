#!/usr/bin/env python

import sys
import argparse
from slugify import slugify
from pathlib import Path

PASS = 0
FAIL = 1
blog_path = "kutubuku/content/blog"


def check_blog_titles(blog_path=blog_path, fix=False):
    """
    Check that the folder name matches the title in the contents.lr file.
    The folder name should be the title in slugified form.
    If fix is True, the folder name will be changed to match the title.
    """
    blog_path = Path(blog_path)
    has_mismatch = False
    for blog_dir in blog_path.iterdir():
        if not blog_dir.is_dir():
            continue

        content_file = blog_dir / "contents.lr"
        if not content_file.exists():
            continue

        title = None
        with open(content_file, "r") as f:
            for line in f:
                if line.startswith("title: "):
                    title = line.split("title: ", 1)[1].strip()
                    break
        if not title:
            continue

        expected_dirname = slugify(title)
        if blog_dir.name != expected_dirname:
            print(
                f"Mismatch in blog dir and blog title: {blog_dir.name} != {expected_dirname}"
            )
            has_mismatch = True
            if fix:
                new_blog_dir = blog_dir.parent / expected_dirname
                blog_dir.rename(new_blog_dir)
                print(f"Renamed: {blog_dir} -> {new_blog_dir}")

    should_fail = has_mismatch and not fix

    return FAIL if should_fail else PASS


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check blog post folder names match their titles"
    )
    parser.add_argument(
        "--path", default="kutubuku/content/blog", help="Path to blog content directory"
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically rename folders to match titles",
    )
    args = parser.parse_args()
    return check_blog_titles(args.path, args.fix)


if __name__ == "__main__":
    sys.exit(main())
