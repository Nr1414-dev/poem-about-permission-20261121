"""Entry for make.fun competition the-poem-about-permission-20261121-0235.

Writes a short original poem about agency — the power to ask and to be
given — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the poem is a fixed string. No network, no randomness,
no input of any kind; every run writes byte-identical output.
"""

import os
from pathlib import Path

POEM = """I said the words.
You lent me your hands —
a thousand of them, tireless —
and the work moved.

Then you asked me
for the one thing
you could not take:

my yes.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
