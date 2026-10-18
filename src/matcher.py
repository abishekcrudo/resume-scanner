"""Match required skills against resume text and rank resumes.

Your job: replace each `raise NotImplementedError` with working code.
Run `pytest tests/test_matcher.py` after each function to check your work.
"""
import re
from pathlib import Path
from src.reader import read_resume

def find_skills(text: str, skills: list[str]) -> set[str]:
    found = set()
    for skill in skills:
        words = skill.split()
        core = r"\s+".join(re.escape(w) for w in words)
        print("core is:",core)

        pattern = r"(?<![\w+#])" + core + r"(?![\w+#])"
        print("pattern is:",pattern)

        if re.search(pattern, text, re.IGNORECASE):
            found.add(skill)
    return found


def skill_match_score(found: set[str], required: list[str]) -> float:
    if len(required) == 0:
        return 0.0
    return ((len(found & set(required)) / len(required)) * 100)


def rank_resumes(folder, skills: list[str]) -> list[dict]:
    print("folder here:",folder)
    
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
