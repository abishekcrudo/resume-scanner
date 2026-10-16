"""Match required skills against resume text and rank resumes.

Your job: replace each `raise NotImplementedError` with working code.
Run `pytest tests/test_matcher.py` after each function to check your work.
"""
from pathlib import Path

from src.reader import read_resume


def find_skills(text: str, skills: list[str]) -> set[str]:
    """Return the set of skills that appear in the text.

    - Ignore letter case.
    - Match whole words only: "Java" must not match inside "JavaScript".
    - Return each skill exactly as it was written in `skills`.
    - Skills can have several words ("Spring Boot") or special
      characters ("C++", ".NET").

    Exercise 5.
    """
    raise NotImplementedError


def skill_match_score(found: set[str], required: list[str]) -> float:
    """Return the percentage (0 to 100) of required skills that were found.

    If `required` is empty, return 0.0 without crashing.

    Exercise 6a.
    """
    raise NotImplementedError


def rank_resumes(folder, skills: list[str]) -> list[dict]:
    """Score every resume in `folder` and return the results, best first.

    Each result is a dict with these keys:
        "file"     the file name, such as "01_priya_nair.docx"
        "score"    the number from skill_match_score()
        "matched"  a sorted list of the required skills found
        "missing"  a sorted list of the required skills not found

    - Sort by score, highest first. Break ties by file name.
    - Skip files that are not .docx or .pdf.

    Exercise 6b.
    """
    raise NotImplementedError
