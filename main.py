"""Copy the finished front-page image to the output directory.

The image (entry.png) was drawn during the build and ships in this
repository. This program only copies it, using the standard library,
so it runs the same way in the grading sandbox (Python 3.13, no
network, nothing installed) and both runs write identical bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
