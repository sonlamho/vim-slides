# vim-slides

## Source file syntax:
  - Slides are separated by lines which start with `##`. Optionally follow it with a file extension. E.g.
    `## .py`, or `## .txt`
  - Final slide must be followed by a `##` line to mark the end.

## How to create slides from source file:
  - If source file is named `source.py` in folder `path/to/folder/` then run:
      ```
      python create_slide_deck.py path/to/folder/source.py
      ```
    will generate `slide_*` files in that same folder.
  
