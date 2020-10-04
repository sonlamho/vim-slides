# vim-slides

## Source file syntax:
  - Each slide must start with a line that starts with `##`. Optionally follow it with a file extension. E.g.
    `## .py`, or `## .txt`

## How to create slides from source file:
  - If source file is named `source.py` in folder `path/to/folder/` then run:
      ```
      python create_slide_deck.py path/to/folder/source.py
      ```
    will generate `slide_*` files in that same folder.
  
