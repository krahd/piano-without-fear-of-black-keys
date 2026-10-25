#!/bin/sh
set -eu
cd "$(dirname "$0")"

# The public filename is stable because laurenzo.net links to it.
# Build the current edition first; never accidentally regenerate v1.3 here.
python3 edition-design/v1.3.1/build.py
cp edition-design/v1.3.1/Piano_Without_Fear_of_Black_Keys_v1.3.1.pdf Piano_Without_Fear_of_Black_Keys.pdf
