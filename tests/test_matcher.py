import shutil
import tempfile
from pathlib import Path

from src.matcher import find_skills, rank_resumes, skill_match_score

RESUMES = Path(__file__).resolve().parent.parent / "data" / "resumes"
SKILLS = ["Java", "Spring Boot", "REST API", "SQL", "Docker", "Git", "AWS"]


# ---- Exercise 5: find_skills -------------------------------------------

def test_find_skills_basic():
    assert find_skills("I know Java and SQL", ["Java", "SQL", "Docker"]) == {"Java", "SQL"}


def test_find_skills_ignores_case():
    assert find_skills("JAVA developer", ["Java"]) == {"Java"}
    assert find_skills("java developer", ["JAVA"]) == {"JAVA"}


def test_find_skills_matches_whole_words_only():
    assert find_skills("javascript expert", ["Java"]) == set()


def test_find_skills_handles_punctuation():
    assert find_skills("skills: java, sql.", ["Java", "SQL"]) == {"Java", "SQL"}

def test_find_skills_multi_word_skill():
    assert find_skills("built spring boot services", ["Spring Boot"]) == {"Spring Boot"}


def test_find_skills_special_characters():
    assert find_skills("c++ and .net", ["C++", ".NET"]) == {"C++", ".NET"}


def test_find_skills_stretch_c_is_not_c_plus_plus():
    assert find_skills("c++ developer", ["C"]) == set()
    assert find_skills("c and c#", ["C"]) == {"C"}

# ---- Exercise 6a: skill_match_score ------------------------------------

def test_score_half():
    assert skill_match_score({"Java", "SQL"}, ["Java", "SQL", "Docker", "Git"]) == 50.0


def test_score_all_and_none():
    assert skill_match_score({"Java"}, ["Java"]) == 100.0
    assert skill_match_score(set(), ["Java", "SQL"]) == 0.0


def test_score_one_third():
    assert abs(skill_match_score({"Java"}, ["Java", "SQL", "Git"]) - 33.33) < 0.01


def test_score_with_no_required_skills():
    assert skill_match_score({"Java"}, []) == 0.0


# ---- Exercise 6b: rank_resumes -----------------------------------------

def test_rank_resumes_is_sorted_best_first():
    results = rank_resumes(RESUMES, SKILLS)
    assert len(results) == 10
    scores = [r["score"] for r in results]
    assert scores == sorted(scores, reverse=True)

'''
def test_rank_resumes_result_shape():
    for r in rank_resumes(RESUMES, SKILLS):
        assert set(r) >= {"file", "score", "matched", "missing"}
        assert r["matched"] == sorted(r["matched"])
        assert r["missing"] == sorted(r["missing"])
        assert sorted(r["matched"] + r["missing"]) == sorted(SKILLS)


def test_rank_resumes_does_not_count_javascript_as_java():
    results = rank_resumes(RESUMES, SKILLS)
    jordan = next(r for r in results if r["file"].startswith("04_"))
    assert "Java" not in jordan["matched"]
    assert "Docker" in jordan["matched"]


def test_rank_resumes_skips_other_file_types():
    folder = Path(tempfile.mkdtemp())
    try:
        shutil.copy(RESUMES / "01_priya_nair.docx", folder / "01_priya_nair.docx")
        (folder / "notes.txt").write_text("not a resume")
        results = rank_resumes(folder, SKILLS)
        assert [r["file"] for r in results] == ["01_priya_nair.docx"]
    finally:
        shutil.rmtree(folder)
cls
        '''