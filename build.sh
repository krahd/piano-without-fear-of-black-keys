#!/bin/sh
set -eu
cd "$(dirname "$0")"

pandoc piano_transposition_manual.md -s -t html5 \
  --metadata title="Piano Without Fear of Black Keys" \
  --css style.css -o book.html

output="Piano_Without_Fear_of_Black_Keys.pdf"

if command -v weasyprint >/dev/null 2>&1; then
  weasyprint book.html "$output"
elif [ -x "/Applications/Chromium.app/Contents/MacOS/Chromium" ]; then
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/$output" "file://$PWD/book.html" >/dev/null 2>&1
elif command -v chromium >/dev/null 2>&1; then
  chromium --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$PWD/$output" "file://$PWD/book.html" >/dev/null 2>&1
else
  echo "ERROR: install WeasyPrint or Chromium to build the PDF." >&2
  exit 1
fi
