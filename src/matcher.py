"""Match required skills against resume text and rank resumes.

Your job: replace each `raise NotImplementedError` with working code.
Run `pytest tests/test_matcher.py` after each function to check your work.
"""
import re
from pathlib import Path
from src.reader import read_resume

from docx import Document   # pip install python-docx
from pypdf import PdfReader  # pip install pypdf

def find_skills(text: str, skills: list[str]) -> set[str]:
    found = set()
    for skill in skills:
        words = skill.split()
        core = r"\s+".join(re.escape(w) for w in words)

        pattern = r"(?<![\w+#])" + core + r"(?![\w+#])"

        if re.search(pattern, text, re.IGNORECASE):
            found.add(skill)
    return found


def skill_match_score(found: set[str], required: list[str]) -> float:
    if len(required) == 0:
        return 0.0
    return ((len(found & set(required)) / len(required)) * 100)


def _read_text(path: Path) -> str:
    """Return all the text in a .docx or .pdf file."""
    if path.suffix.lower() == ".docx":
        doc = Document(str(path))
        parts = [p.text for p in doc.paragraphs]
        for table in doc.tables:
            for row in table.rows:
                parts.extend(cell.text for cell in row.cells)
        return "\n".join(parts)
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)



def rank_resumes(folder_path, skills: list[str]) -> list[dict]:
    """Score every resume in `folder_path` and return the results, best first."""
    results = []
    for path in Path(folder_path).iterdir():
        if not path.is_file() or path.suffix.lower() not in {".docx", ".pdf"}:
            continue
        if path.name.startswith("~$"):  # Word lock/temp files
            continue

        text = _read_text(path)   
        matched = sorted(find_skills(text, skills))
        missing = sorted(s for s in skills if s not in matched)

        results.append({
            "file": path.name,
            "score": skill_match_score(set(matched), skills),
            "matched": matched,
            "missing": missing,
        })

    results.sort(key=lambda r: (-r["score"], r["file"]))
    return results
