#!/bin/sh
set -eu
root="$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)"
cd "$root"

# Reproduce the historical v1.3 typesetting without overwriting the
# stable root filename (which now serves the newer v1.3.1 edition).
pandoc piano_transposition_manual.md -s -t html5 \
  --metadata pagetitle="Piano Without Fear of Black Keys" \
  --css style.css -o book.html
weasyprint book.html edition-design/v1.3/Piano_Without_Fear_of_Black_Keys_v1.3.pdf
