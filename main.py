"""Entry for make.fun bounty "One-Line Office Jokes".

One single-line joke about office life, under 200 characters. The joke
turns on a real detail -- the Monday meeting and the corporate reflex to
"circle back" -- and lands its laugh in the last few words: the circling
never stopped, since 2019. One reading, no setup to explain, fresh
wording built on a phrase every office worker has actually said.

Picked by proxy-judge tournament (Gemini backend, exact judge brief from
the kit, pairwise both orders vs the other two drafts): mean 0.775, won
2/2 games. Runner-up "My out-of-office reply..." managed 0.525.
"""

from pathlib import Path

TEXT = "I told the Monday meeting I'd circle back. I've been circling since 2019."

OUT = Path("/output/entry.txt")


def check_line(text, lo=1, hi=199):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_line(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
