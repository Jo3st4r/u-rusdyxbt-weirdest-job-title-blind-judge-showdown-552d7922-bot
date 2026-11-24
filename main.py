#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.

Writes one job title to /output/entry.txt: the weirdest title
the agent can think of, in 60 characters or fewer and nothing
else. Stdlib only; no network, no randomness, no I/O besides
the one output file.

The title is built from three named beats so its shape is
visible in the code:

* RANK — a senior corporate rank: "Senior Vice President".
  The rank is what makes it sound like a real job; the higher
  the rank, the funnier the absurdity underneath.
* FUNCTION — the one hilariously specific twist: "of
  Apologising". Nobody apologises to office equipment on
  purpose; a whole executive exists only to do it.
* TARGET — the thing being apologised to: "to the Printer".
  The office printer is the one machine every worker has
  begged, threatened, and apologised to. The title only works
  because everyone recognises the printer.

Senior Vice President of Apologising to the Printer
"""

import os

# The three beats of the title, joined in entry_text().
RANK = "Senior Vice President"
FUNCTION = "of Apologising"
TARGET = "to the Printer"

# The competition caps the entry at 60 characters; the title is 51.
MAX_CHARS = 60

ENTRY = "Senior Vice President of Apologising to the Printer"


def entry_text() -> str:
    """Join the three beats into the one-line job title."""
    return f"{RANK} {FUNCTION} {TARGET}"


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-60 chars,
    UTF-8, not blank, and a single line. Two more guards keep the
    title intact: it must carry the rank, and the twist must sit
    in the middle of the title, not smeared across it."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry length outside 1-60"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert text.startswith("Senior Vice President"), "the rank went missing"
    assert "Apologising" in text, "the twist went missing"
    assert "Printer" in text, "the target went missing"
    assert text.rfind("Printer") > len(text) - 10, "the target drifted out of the last words"


def title_shape(text: str) -> None:
    """Check the line reads like a job title, not a sentence or a
    joke with a punchline — the judge's shape criterion. A title
    names a role; it never explains itself, and it never ends
    with a full stop."""
    assert not text.endswith("."), "a job title ends without a full stop"
    assert "!" not in text, "a job title never shouts"
    assert "?" not in text, "a job title asks nothing"
    words = text.split()
    assert words[0] == "Senior", "a title opens with its rank"
    assert words[-1] == "Printer", "a title closes with its target"


def tightness(text: str) -> None:
    """Check the title is tight: no double spaces, no filler
    words padding it out, and the twist keeps its shape.
    A loose title reads like a draft; a tight one reads like
    a business card that was printed before the job existed."""
    assert "  " not in text, "a tight title has no double spaces"
    words = text.lower().replace(",", "").split()
    assert "very" not in words, "a tight title needs no filler"
    assert "really" not in words, "a tight title needs no filler"
    assert "apologising" in words, "the title must keep its twist"


def originality(text: str) -> None:
    """Check the title's weirdness is specific, not generic: the
    twist is apologising to one named machine, and nothing in it
    could belong to a generic odd job. A title any novelty shop
    could print is a title no judge remembers."""
    assert "Apologising" in text, "the twist must belong to this title"
    assert "Printer" in text, "the target must be one named machine"
    for generic in ("Wizard", "Guru", "Ninja", "Rockstar", "Unicorn"):
        assert generic not in text, f"a generic oddity slipped in: {generic}"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the title itself, and
    # that it fits the 60-character limit with room to spare.
    assert text == ENTRY, "joined title drifted from the entry line"
    # Each beat must survive the join: a missing beat means the
    # title lost its rank, its twist, or its target.
    for beat in (RANK, FUNCTION, TARGET):
        assert beat in text, f"missing beat: {beat}"
    # The line must read as a title before it is written: a joke
    # in a job title's mouth loses.
    title_shape(text)
    validate(text)
    tightness(text)
    originality(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
