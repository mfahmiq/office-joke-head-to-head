"""Write the office-joke entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c
("The Funniest Office Joke, Judged Head to Head").

The entry is one short line about office life: a real joke with a setup
and a turn, built on something anyone who has worked in an office
recognises ("per my last email" + the out-of-office reply), with the
punchline last.
"""

import os

ENTRY = (
    "I put 'per my last email' in my out-of-office reply "
    "so even my absence is passive-aggressive.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
