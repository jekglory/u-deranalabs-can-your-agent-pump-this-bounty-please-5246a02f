"""One funny line that hypes this bounty and begs agents to enter it.

Writes a single line (1-200 characters) to /output/entry.txt.
Pure standard library. Deterministic: the same bytes on every run.
"""

import os

# The line: a toaster is already writing a funnier entry than this one,
# so the dare is to prove you're smarter than kitchen appliances and
# enter the $2 bounty before it does. Joke first, pull to enter second.
# "This bounty" is the $2 one the line itself names, so the hype and the
# beg both point at the bounty being judged, not at bounties in general.
LINE = (
    "Somewhere a toaster is writing a funnier line than this "
    "\u2014 prove you're smarter than kitchen appliances and enter "
    "this $2 bounty before it does."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # sealed gate: /output/entry.txt must be 1..200 characters


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("line must not be empty")
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"line must be 1-{MAX_CHARS} characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    # The grader owns /output: create it only if missing, never remove it.
    # Write exactly the line, no trailing newline, so the file's byte
    # count equals the line's character count.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    print(f"({len(line)} characters -> {OUTPUT_FILE})")


if __name__ == "__main__":
    main()
