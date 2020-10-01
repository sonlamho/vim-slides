import os
import argparse
from argparse import Namespace
from typing import List, Tuple

DEFAULT_LINES = 20


def get_slides(fpath: str, n_lines: int) -> List[Tuple[str, str]]:
    with open(fpath, "r") as f:
        lines = f.readlines()
    #
    slides = []
    ext = ""
    texts: List[str] = []
    for line in lines:
        if line.startswith("##"):
            if texts:
                # create a slide
                post_process(texts)
                assert len(texts) <= n_lines
                padding = ["\n"] * (n_lines - len(texts))
                slides.append((ext, "".join(texts + padding)))
            # prep for a new slide
            ext = line.strip("#").strip()
            if not ext.startswith("."):
                ext = "." + ext
            texts = []
        else:
            texts.append(line)
    return slides


def post_process(slide_lines: List[str]):
    if slide_lines[0].strip():
        slide_lines.insert(0, "\n")


def export(slides: List[Tuple[str, str]], fpath: str):
    for i, ext_text in enumerate(slides):
        ext, text = ext_text
        num = str(i).zfill(8)
        slide_path = os.path.join(fpath, f"slide_{num}{ext}")
        mode = "w" if os.path.exists(slide_path) else "x"
        with open(slide_path, mode) as f:
            f.write(text)


def main(args: Namespace):
    fpath = os.path.realpath(args.folderpath[0])
    print(f"Creating slides in:\n  {fpath}")
    src_path = os.path.join(fpath, "source.py")
    slides = get_slides(src_path, args.lines)
    export(slides, fpath)


def _init_parser() -> argparse.ArgumentParser:
    _parser = argparse.ArgumentParser()
    _parser.add_argument("folderpath", type=str, nargs=1)
    _parser.add_argument(
        "--lines",
        type=int,
        default=DEFAULT_LINES,
        help="Target number of lines per slide",
    )
    return _parser


if __name__ == "__main__":
    _parser = _init_parser()
    args: Namespace = _parser.parse_args()
    args_dict = {a: getattr(args, a) for a in dir(args) if not a.startswith("_")}
    print(args_dict)
    main(args)
