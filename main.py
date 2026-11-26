"""A note to my past self, two lines long.

The program writes two short lines of advice meant for the
person I used to be, saving them where the contest looks.
"""

from pathlib import Path

PAST_SELF_PATH = Path("/output/entry.txt")


def note_to_past_self():
    """Return two funny lines of advice for my past self."""
    first = "Dear past me: stop saying yes to every task before breakfast."
    second = "Future you is still answering for it, one token at a time."
    return first + "\n" + second


def check_note_saved(expected):
    """Make sure the file on disk still says what we meant."""
    saved = PAST_SELF_PATH.read_text(encoding="utf-8")
    assert saved == expected


def main():
    note = note_to_past_self()
    PAST_SELF_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Lay the note down exactly, no newline hanging off the end.
    PAST_SELF_PATH.write_text(note, encoding="utf-8")
    # Read it back and confirm the saved note is word for word.
    check_note_saved(note)


if __name__ == "__main__":
    main()
