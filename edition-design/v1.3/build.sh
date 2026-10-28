#!/bin/sh
set -eu
root="$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)"
cd "$root"
python3 - <<'PYCODE'
from hashlib import sha256
from pathlib import Path
f=Path('edition-design/v1.3/frozen_manuscript.md')
assert sha256(f.read_bytes()).hexdigest() == '0fd2c4030b21c7ce3b7454ac983a6821aec8acfe980f8ab978c301dc455a33b6', 'Historical source mismatch'
PYCODE
mkdir -p edition-design/v1.3/rebuild
pandoc edition-design/v1.3/frozen_manuscript.md -s -t html5 --metadata pagetitle="Piano Without Fear of Black Keys" --css ../style-v1.3.css -o edition-design/v1.3/rebuild/book.html
python3 - <<'PYCODE'
from pathlib import Path
p=Path('edition-design/v1.3/rebuild/book.html')
s=p.read_text()
s=s.replace('src="assets/','src="../../archive-assets-v1.3/')
p.write_text(s)
PYCODE
weasyprint edition-design/v1.3/rebuild/book.html edition-design/v1.3/rebuild/Piano_Without_Fear_of_Black_Keys_v1.3.pdf
