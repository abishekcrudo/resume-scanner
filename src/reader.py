"""Read resume files (.docx and .pdf) and return clean text.

Your job: replace each `raise NotImplementedError` with working code.
Run `pytest tests/test_reader.py` after each function to check your work.
"""
from pathlib import Path


def clean_text(text: str) -> str:
    """Return the text in lowercase, with every run of whitespace
    (spaces, tabs, newlines) collapsed into a single space and no
    leading or trailing whitespace.

    Exercise 1.
    """
    raise NotImplementedError


def read_docx(path) -> str:
    """Return the raw text of a Word (.docx) file.

    Exercise 2. Library to look up: python-docx (`import docx`).
    """
    raise NotImplementedError


def read_pdf(path) -> str:
    """Return the raw text of a PDF file, from all pages.

    Exercise 3. Library to look up: pdfplumber.
    Think about what happens when a page has no text.
    """
    raise NotImplementedError


def read_resume(path) -> str:
    """Read a resume and return its cleaned text.

    - Choose the right reader from the file extension (.docx or .pdf,
      in any letter case).
    - Pass the result through clean_text().
    - Raise ValueError, with a helpful message, for any other file type.

    Exercise 4.
    """
    raise NotImplementedError
