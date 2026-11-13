#!/bin/sh
set -eu
cd "$(dirname "$0")"
# Pin the book's Python dependencies in an isolated environment when absent.
# BOOK_PYTHON may point to an already prepared interpreter (e.g., a venv).
if [ -n "${BOOK_PYTHON:-}" ]; then
  "$BOOK_PYTHON" edition-design/v1.3.3/build.py
elif python3 -c 'import bs4, weasyprint' >/dev/null 2>&1; then
  python3 edition-design/v1.3.3/build.py
elif command -v uv >/dev/null 2>&1; then
  uv run --no-project --with 'beautifulsoup4==4.14.3' --with 'weasyprint==68.0' python3 edition-design/v1.3.3/build.py
else
  echo 'Missing build dependencies. Install from requirements-book.txt in an isolated environment, then set BOOK_PYTHON.' >&2
  exit 1
fi
cp edition-design/v1.3.3/Piano_Without_Fear_of_Black_Keys_v1.3.3.pdf Piano_Without_Fear_of_Black_Keys.pdf
