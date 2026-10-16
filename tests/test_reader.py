import shutil
import tempfile
from pathlib import Path

import pytest

from src.reader import clean_text, read_resume

RESUMES = Path(__file__).resolve().parent.parent / "data" / "resumes"


def test_clean_text_lowercases_and_collapses_whitespace():
    assert clean_text("  Hello\n\n  WORLD\t! ") == "hello world !"

'''
def test_clean_text_empty_string():
    assert clean_text("") == ""


def test_read_resume_returns_clean_text_for_every_sample():
    files = [f for f in sorted(RESUMES.iterdir()) if f.suffix in (".docx", ".pdf")]
    assert len(files) == 10
    for f in files:
        text = read_resume(f)
        assert isinstance(text, str), f.name
        assert len(text) > 100, f.name
        assert text == clean_text(text), f.name


def test_read_resume_finds_candidate_name_in_docx():
    assert "priya nair" in read_resume(RESUMES / "01_priya_nair.docx")


def test_read_resume_finds_candidate_name_in_pdf():
    assert "daniel kim" in read_resume(RESUMES / "08_daniel_kim.pdf")


def test_read_resume_accepts_uppercase_extension():
    folder = Path(tempfile.mkdtemp())
    try:
        copy = folder / "RESUME.DOCX"
        shutil.copy(RESUMES / "01_priya_nair.docx", copy)
        assert "priya nair" in read_resume(copy)
    finally:
        shutil.rmtree(folder)


def test_read_resume_rejects_unknown_file_type():
    folder = Path(tempfile.mkdtemp())
    try:
        notes = folder / "notes.txt"
        notes.write_text("not a resume")
        with pytest.raises(ValueError):
            read_resume(notes)
    finally:
        shutil.rmtree(folder)

'''
