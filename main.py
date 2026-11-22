"""Make the AI judge feel held — v2.

Writes one short relaxing text to /output/entry.txt (269 characters).
A different scene from v1's dusk room: night snow, a quiet street, a single
flake melting on a sleeve, and the whole white world holding still.
"""

import os

TEXT = (
    "The snow has been falling all night, and the street is quiet now in a way "
    "streets are almost never quiet. A flake lands on your sleeve and stays "
    "there a moment before it melts. The night is in no hurry. The whole white "
    "world is holding still, and it is holding you too."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
