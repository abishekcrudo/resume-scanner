# Stage 1: Python basics with a keyword matcher

**Goal:** a program that reads resumes (Word and PDF), finds which required skills each one mentions, and ranks them. No machine learning yet. This is your baseline, and every later stage has to beat it.

**How you work:** the tests in `tests/` describe what each function must do. They all fail at the start. Your job is to make them pass, one function at a time. This is called test-driven development, and it is how professional developers work.

**Rules for yourself**
- Write the code yourself. Look things up in the official docs first.
- When stuck, read the error message slowly, then try one thing. After that, ask me for a hint, not the answer.
- Commit to Git after each exercise, with a message that says what you did.

---

## Exercise 0: Set up

1. Create a virtual environment and activate it.
2. Install the packages in `requirements.txt`.
3. Run `pytest`. Every test should fail with `NotImplementedError`. That is the correct starting point.
4. Run `git init` and make your first commit.

**You will learn:** virtual environments, pip, running a test suite, reading a failing test.

## Exercise 1: `clean_text` (in `src/reader.py`)

Make the two `clean_text` tests pass.

**Look up:** what `str.lower()` does, and what `str.split()` does when you give it no arguments. Then find a way to join the pieces back together.

**You will learn:** string methods and why cleaning text comes before any matching.

## Exercise 2: `read_docx`

Read all the text from a Word file.

**Look up:** the `python-docx` documentation, the `Document` class and its `paragraphs`.

**Stretch:** many real resumes put skills in a table. Find out how to read table cells too. Our sample files don't need this, but real ones do.

**You will learn:** using a third-party library from its documentation, and working with file paths through `pathlib`.

## Exercise 3: `read_pdf`

Read all the text from a PDF file.

**Look up:** `pdfplumber.open`, `pages`, `extract_text`. Check what `extract_text` returns for a blank page.

**You will learn:** context managers (`with`), loops over pages, and handling `None` values.

## Exercise 4: `read_resume`

Choose the reader from the file extension, clean the text, and raise a clear `ValueError` for anything else.

**Look up:** `Path.suffix`, `str.lower()`, and how to raise an exception with a message.

**You will learn:** branching, raising exceptions, and why error messages should say what the user can do about it.

Run `pytest tests/test_reader.py`. All of it should pass now.

## Exercise 5: `find_skills` (in `src/matcher.py`)

This is the hardest exercise. First try the simplest idea: `skill.lower() in text`. Run the tests and see which ones fail. Then write in your notes why `"java" in "javascript"` is a problem.

**Look up:** Python's `re` module, `re.escape`, and the regular expression ideas of word boundaries and lookarounds (`(?<!...)` and `(?!...)`).

**Hint level 1:** `\b` works for plain words, but it breaks for skills such as `C++` and `.NET`, because `+` and `.` are not word characters. Decide what "a skill is a whole word" should mean for those, and write your own boundary rule.

**You will learn:** regular expressions, sets, and testing edge cases. The last test, `test_find_skills_stretch_c_is_not_c_plus_plus`, is a stretch goal.

## Exercise 6: scoring and ranking

6a. `skill_match_score`: the percentage of required skills found. Handle an empty list of required skills.

6b. `rank_resumes`: loop over the files in a folder, skip files that are not resumes, build one dictionary per resume, and sort the list.

**Look up:** `sorted` with a `key=` function, `Path.iterdir`, and sorting by two values at once (score, then file name).

**You will learn:** list comprehensions, dictionaries, custom sorting, and writing functions that call other functions.

Run `pytest`. When everything passes, Stage 1's code is done.

## Exercise 7: Compare yourself with the program

1. **Before** you run `rank_resumes` on the sample resumes, fill in `notes/my_ranking.md`. Read the job description and rank the ten resumes yourself.
2. Write a short script (or use the Python prompt) that runs `rank_resumes` on `data/resumes` with the required skills from the job description, and print the results.
3. Compare. Where do you and the program disagree? Look at these cases in particular:
   - `REST API` in the required skills versus `REST APIs` in a resume.
   - `PostgreSQL` listed, but `SQL` not found as a separate word.
   - A DevOps engineer whose resume mentions Java only because they deploy Java services.
   - A resume that writes `JAVA` in capitals.
   - Experience and seniority, which keyword counting ignores completely.
4. Write your findings in `notes/stage1_notes.md`.

**You will learn:** what a baseline is, where simple rules break, and what a smarter method must do. That list of problems is the reason Stage 2 exists.

---

## Definition of done

- [ ] All tests pass with `pytest`.
- [ ] One Git commit per exercise.
- [ ] `notes/my_ranking.md` and `notes/stage1_notes.md` are filled in.
- [ ] You can explain in your own words why `"java" in text` is not good enough.

## How to ask me for help

Tell me which exercise you are on, paste the error or failing test, and say what you already tried. Ask for a hint level: a nudge, a bigger hint, or an explanation of the concept. I would rather explain an idea than give you working code.
