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
    # Guard the competition's gate: entry.txt must hold 1-280 Unicode
    # code points of non-whitespace text. Fail loudly instead of
    # silently submitting an invalid entry if the poem ever changes.
    code_points = len(POEM)
    if not 1 <= code_points <= 280:
        raise SystemExit(f"poem is {code_points} code points, must be 1-280")
    if not POEM.strip():
        raise SystemExit("poem must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write atomically so a run never leaves a half-written entry.txt.
    target = out_dir / "entry.txt"
    tmp = target.with_suffix(".tmp")
    tmp.write_text(POEM, encoding="utf-8")
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
