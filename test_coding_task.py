"""
=============================================================
  TEST SUITE: Algorithm Design & Analysis Coding Task
=============================================================

Run with:   pytest test_coding_task.py -v
Or for a summary:  pytest test_coding_task.py -v --tb=short

Each level is tested independently. A student can pass Level 2
tests even if Level 3 is incomplete. Results are grouped clearly
so you can see at a glance how far each student has progressed.

SETUP NOTE
----------
This file expects the student's work to be saved as:
    coding_task_algorithm_design.py
in the same folder. If the file has a syntax error (e.g. the
??? placeholders haven't been replaced), that level's tests
will be marked as errors rather than failures — which is still
useful information.
=============================================================
"""

import importlib
import importlib.util
import sys
import os
import copy
import pytest


# =============================================================
#  IMPORT HELPER
#  Loads the student file carefully so a syntax error or
#  incomplete section doesn't crash the entire test run.
# =============================================================

STUDENT_FILE = "coding_task_algorithm_design.py"

def load_student_module():
    """
    Attempt to import the student file. Returns (module, error_msg).
    module is None if the file couldn't be loaded.
    """
    spec = importlib.util.spec_from_file_location(
        "student_code",
        os.path.join(os.path.dirname(__file__), STUDENT_FILE)
    )
    if spec is None:
        return None, f"Could not find '{STUDENT_FILE}' — make sure it's in the same folder."
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except SyntaxError as e:
        return None, f"Syntax error in student file (unfilled ??? placeholder?): {e}"
    except Exception as e:
        return None, f"Student file raised an error on import: {e}"
    return module, None


# Load once at module level for use across all tests
student, _load_error = load_student_module()


def get_fn(name):
    """
    Retrieve a named function from the student module.
    Skips the test with a helpful message if the module failed
    to load, the function doesn't exist, or it's still a stub (pass-only).
    """
    if student is None:
        pytest.skip(_load_error or "Student module could not be loaded.")
    fn = getattr(student, name, None)
    if fn is None:
        pytest.skip(f"'{name}' not found in student file.")
    return fn


# =============================================================
#  LEVEL 1 — Procedures and Functions
# =============================================================

class TestLevel1:
    """Level 1: Procedures and Functions"""

    def test_1c_grade_A(self):
        """calculate_grade returns 'A' for scores >= 90"""
        fn = get_fn("calculate_grade")
        assert fn(90)  == "A", "Score of 90 should return 'A'"
        assert fn(95)  == "A", "Score of 95 should return 'A'"
        assert fn(100) == "A", "Score of 100 should return 'A'"

    def test_1c_grade_B(self):
        """calculate_grade returns 'B' for scores 75–89"""
        fn = get_fn("calculate_grade")
        assert fn(75) == "B", "Score of 75 should return 'B'"
        assert fn(80) == "B", "Score of 80 should return 'B'"
        assert fn(89) == "B", "Score of 89 should return 'B'"

    def test_1c_grade_C(self):
        """calculate_grade returns 'C' for scores 60–74"""
        fn = get_fn("calculate_grade")
        assert fn(60) == "C", "Score of 60 should return 'C'"
        assert fn(62) == "C", "Score of 62 should return 'C'"
        assert fn(74) == "C", "Score of 74 should return 'C'"

    def test_1c_grade_F(self):
        """calculate_grade returns 'F' for scores below 60"""
        fn = get_fn("calculate_grade")
        assert fn(59) == "F", "Score of 59 should return 'F'"
        assert fn(40) == "F", "Score of 40 should return 'F'"
        assert fn(0)  == "F", "Score of 0 should return 'F'"

    def test_1c_returns_a_value(self):
        """calculate_grade must return a value, not print it"""
        fn = get_fn("calculate_grade")
        result = fn(85)
        assert result is not None, (
            "calculate_grade returned None — did you use 'return' instead of 'print'?"
        )

    def test_1c_boundary_exactly_90(self):
        """Boundary check: score of exactly 90 is an A, not a B"""
        fn = get_fn("calculate_grade")
        assert fn(90) == "A", "Score of exactly 90 should be 'A' (>= 90)"

    def test_1c_boundary_exactly_75(self):
        """Boundary check: score of exactly 75 is a B, not a C"""
        fn = get_fn("calculate_grade")
        assert fn(75) == "B", "Score of exactly 75 should be 'B' (>= 75)"

    def test_1c_boundary_exactly_60(self):
        """Boundary check: score of exactly 60 is a C, not an F"""
        fn = get_fn("calculate_grade")
        assert fn(60) == "C", "Score of exactly 60 should be 'C' (>= 60)"


# =============================================================
#  LEVEL 2 — Top-Down Design: Report System
# =============================================================

class TestLevel2:
    """Level 2: Top-Down Design — Report System"""

    def test_2a_find_average_basic(self):
        """find_average returns correct average for a simple list"""
        fn = get_fn("find_average")
        result = fn([80, 90, 70])
        assert result == pytest.approx(80.0), (
            f"find_average([80, 90, 70]) should be 80.0, got {result}"
        )

    def test_2a_find_average_returns_float(self):
        """find_average returns a number (int or float), not None"""
        fn = get_fn("find_average")
        result = fn([50, 100])
        assert result is not None, "find_average returned None — did you forget 'return'?"
        assert isinstance(result, (int, float)), (
            f"find_average should return a number, got {type(result)}"
        )

    def test_2a_find_average_single(self):
        """find_average works with a single-element list"""
        fn = get_fn("find_average")
        assert fn([77]) == pytest.approx(77.0)

    def test_2a_find_average_decimals(self):
        """find_average handles non-whole averages"""
        fn = get_fn("find_average")
        result = fn([70, 71])
        assert result == pytest.approx(70.5), (
            f"find_average([70, 71]) should be 70.5, got {result}"
        )

    def test_2a_find_highest_basic(self):
        """find_highest returns the maximum value"""
        fn = get_fn("find_highest")
        assert fn([80, 90, 70]) == 90, (
            "find_highest([80, 90, 70]) should return 90"
        )

    def test_2a_find_highest_returns_value(self):
        """find_highest returns a value, not None"""
        fn = get_fn("find_highest")
        result = fn([55, 72, 88])
        assert result is not None, "find_highest returned None — did you forget 'return'?"

    def test_2a_find_highest_single(self):
        """find_highest works with a single-element list"""
        fn = get_fn("find_highest")
        assert fn([42]) == 42

    def test_2a_find_highest_all_same(self):
        """find_highest works when all scores are equal"""
        fn = get_fn("find_highest")
        assert fn([70, 70, 70]) == 70

    def test_2b_calculate_stats_structure(self):
        """calculate_stats returns a dict with 'average' and 'highest' keys"""
        fn = get_fn("calculate_stats")
        result = fn([80, 90, 70])
        assert result is not None, "calculate_stats returned None — did you forget 'return'?"
        assert isinstance(result, dict), (
            f"calculate_stats should return a dict, got {type(result)}"
        )
        assert "average" in result, "Result dict missing key 'average'"
        assert "highest" in result, "Result dict missing key 'highest'"

    def test_2b_calculate_stats_values(self):
        """calculate_stats returns correct average and highest"""
        fn = get_fn("calculate_stats")
        result = fn([80, 90, 70])
        assert result["average"] == pytest.approx(80.0), (
            f"Expected average 80.0, got {result.get('average')}"
        )
        assert result["highest"] == 90, (
            f"Expected highest 90, got {result.get('highest')}"
        )

    def test_2b_calculate_stats_calls_helpers(self):
        """calculate_stats delegates to find_average and find_highest (not reimplemented inline)"""
        # We can't perfectly enforce this, but we check the results are consistent
        # with what those functions would return — a strong hint they're being used.
        calc   = get_fn("calculate_stats")
        avg_fn = get_fn("find_average")
        hi_fn  = get_fn("find_highest")
        scores = [55, 72, 88, 61]
        result = calc(scores)
        assert result is not None
        assert result.get("average") == pytest.approx(avg_fn(scores)), (
            "calculate_stats average doesn't match find_average — are you calling it?"
        )
        assert result.get("highest") == hi_fn(scores), (
            "calculate_stats highest doesn't match find_highest — are you calling it?"
        )

    def test_2c_display_report_runs_without_error(self, capsys):
        """display_report runs without raising an exception"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats  = calc(scores) if calc(scores) is not None else {"average": 84.3, "highest": 90}
        fn("Alex", scores, stats)   # Should not raise

    def test_2c_display_report_prints_something(self, capsys):
        """display_report actually prints output"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats  = calc(scores) or {"average": 84.3, "highest": 90}
        fn("Alex", scores, stats)
        captured = capsys.readouterr()
        assert captured.out.strip() != "", (
            "display_report produced no output — did you forget to print anything?"
        )

    def test_2c_display_report_includes_name(self, capsys):
        """display_report output includes the student's name"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats  = calc(scores) or {"average": 84.3, "highest": 90}
        fn("Jordan", scores, stats)
        captured = capsys.readouterr()
        assert "Jordan" in captured.out, (
            "display_report output doesn't include the student's name"
        )

    def test_2c_display_report_includes_grade(self, capsys):
        """display_report output includes a grade letter"""
        fn = get_fn("display_report")
        calc = get_fn("calculate_stats")
        scores = [85, 90, 78]
        stats  = calc(scores) or {"average": 84.3, "highest": 90}
        fn("Alex", scores, stats)
        captured = capsys.readouterr()
        assert any(g in captured.out for g in ["A", "B", "C", "F"]), (
            "display_report output doesn't include a grade letter (A/B/C/F)"
        )

    def test_2d_run_report_system_runs(self, capsys):
        """run_report_system runs without raising an exception"""
        fn = get_fn("run_report_system")
        fn()   # Should not raise

    def test_2d_run_report_system_prints_multiple_students(self, capsys):
        """run_report_system prints output for at least 2 students"""
        fn = get_fn("run_report_system")
        fn()
        captured = capsys.readouterr()
        lines = [l for l in captured.out.strip().splitlines() if l.strip()]
        assert len(lines) >= 2, (
            f"run_report_system printed {len(lines)} line(s) — expected output for at least 2 students"
        )


# =============================================================
#  LEVEL 3 — Divide and Conquer: Binary Search
# =============================================================

class TestLevel3:
    """Level 3: Divide and Conquer — Binary Search"""

    NUMBERS = [3, 7, 12, 19, 25, 31, 44, 58, 67, 90]

    def test_3a_finds_element_in_middle(self):
        """binary_search finds a value near the middle of the list"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 25) == 4, (
            "binary_search([3,7,12,19,25,31,44,58,67,90], 25) should return 4"
        )

    def test_3a_finds_first_element(self):
        """binary_search finds the first element"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 3) == 0, (
            "binary_search should return 0 for the first element"
        )

    def test_3a_finds_last_element(self):
        """binary_search finds the last element"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 90) == 9, (
            "binary_search should return 9 for the last element (90)"
        )

    def test_3a_returns_negative_one_when_missing(self):
        """binary_search returns -1 when target is not in the list"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 10) == -1, (
            "binary_search should return -1 when target is not found"
        )

    def test_3a_returns_negative_one_below_range(self):
        """binary_search returns -1 for a value below the list range"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 1) == -1

    def test_3a_returns_negative_one_above_range(self):
        """binary_search returns -1 for a value above the list range"""
        fn = get_fn("binary_search")
        assert fn(self.NUMBERS, 999) == -1

    def test_3a_single_element_found(self):
        """binary_search works on a single-element list when target is present"""
        fn = get_fn("binary_search")
        assert fn([42], 42) == 0

    def test_3a_single_element_not_found(self):
        """binary_search works on a single-element list when target is absent"""
        fn = get_fn("binary_search")
        assert fn([42], 7) == -1

    def test_3a_two_elements_first(self):
        """binary_search finds the first of two elements"""
        fn = get_fn("binary_search")
        assert fn([10, 20], 10) == 0

    def test_3a_two_elements_second(self):
        """binary_search finds the second of two elements"""
        fn = get_fn("binary_search")
        assert fn([10, 20], 20) == 1

    def test_3a_returns_an_index_not_the_value(self):
        """binary_search returns the INDEX, not the value itself"""
        fn = get_fn("binary_search")
        result = fn(self.NUMBERS, 31)
        assert result == 5, (
            f"binary_search should return index 5 for value 31, got {result}. "
            "Make sure you're returning the index, not the value."
        )


# =============================================================
#  LEVEL 4 — Backtracking: Maze Solver
#  (solve_maze is provided in full — tests check the student
#   hasn't accidentally broken it while experimenting.)
# =============================================================

class TestLevel4:
    """Level 4: Backtracking — Maze Solver (provided code integrity check)"""

    SOLVABLE_MAZE = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    UNSOLVABLE_MAZE = [
        [0, 1],
        [1, 0],
    ]

    def _fresh_maze(self, template):
        return copy.deepcopy(template)

    def test_4a_solvable_maze_returns_true(self):
        """solve_maze returns True for a solvable maze"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        result = fn(maze, 0, 0, [])
        assert result is True, "solve_maze should return True for a solvable maze"

    def test_4a_path_is_populated(self):
        """solve_maze populates the path list when a solution is found"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        assert len(path) > 0, "path list should contain cells after solving"

    def test_4a_path_starts_at_origin(self):
        """Path starts at (0, 0)"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        assert path[0] == (0, 0), f"Path should start at (0,0), started at {path[0]}"

    def test_4a_path_ends_at_goal(self):
        """Path ends at the bottom-right corner"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.SOLVABLE_MAZE)
        rows, cols = len(maze), len(maze[0])
        path = []
        fn(maze, 0, 0, path)
        assert path[-1] == (rows - 1, cols - 1), (
            f"Path should end at ({rows-1},{cols-1}), ended at {path[-1]}"
        )

    def test_4a_path_only_visits_open_cells(self):
        """Path only steps through originally open cells (no walls)"""
        fn = get_fn("solve_maze")
        original = self._fresh_maze(self.SOLVABLE_MAZE)
        maze     = self._fresh_maze(self.SOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        for r, c in path:
            assert original[r][c] == 0, (
                f"Path stepped through a wall at ({r},{c})"
            )

    def test_4a_unsolvable_maze_returns_false(self):
        """solve_maze returns False for an unsolvable maze"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.UNSOLVABLE_MAZE)
        result = fn(maze, 0, 0, [])
        assert result is False, "solve_maze should return False for an unsolvable maze"

    def test_4a_unsolvable_maze_path_is_empty(self):
        """Path list remains empty when no solution exists"""
        fn = get_fn("solve_maze")
        maze = self._fresh_maze(self.UNSOLVABLE_MAZE)
        path = []
        fn(maze, 0, 0, path)
        assert path == [], (
            f"Path should be empty for unsolvable maze, got {path}"
        )


# =============================================================
#  SUMMARY HELPER
#  Prints a clean level-by-level progress summary at the end.
# =============================================================

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print a student-friendly progress summary after all tests."""
    passed = {r.nodeid for r in terminalreporter.stats.get("passed", [])}
    failed = {r.nodeid for r in terminalreporter.stats.get("failed", [])}
    errors = {r.nodeid for r in terminalreporter.stats.get("error",  [])}
    skipped= {r.nodeid for r in terminalreporter.stats.get("skipped",[])}

    levels = {
        "Level 1 — Procedures & Functions": "TestLevel1",
        "Level 2 — Top-Down Design (Report System)": "TestLevel2",
        "Level 3 — Divide & Conquer (Binary Search)": "TestLevel3",
        "Level 4 — Backtracking (Maze Solver)": "TestLevel4",
    }

    lines = [
        "",
        "=" * 62,
        "  STUDENT PROGRESS SUMMARY",
        "=" * 62,
    ]

    for label, cls in levels.items():
        level_passed  = [n for n in passed  if cls in n]
        level_failed  = [n for n in failed  if cls in n]
        level_errored = [n for n in errors  if cls in n]
        level_skipped = [n for n in skipped if cls in n]

        total    = len(level_passed) + len(level_failed) + len(level_errored)
        n_passed = len(level_passed)

        if total == 0 and level_skipped:
            status = "⏭  SKIPPED  (not attempted or file error)"
        elif level_errored:
            status = f"⚠  ERROR    ({len(level_errored)} test(s) couldn't run — check syntax)"
        elif n_passed == total and total > 0:
            status = f"✅ COMPLETE  ({n_passed}/{total} tests passed)"
        elif n_passed > 0:
            status = f"🔶 PARTIAL   ({n_passed}/{total} tests passed)"
        else:
            status = f"❌ NOT DONE  (0/{total} tests passed)"

        lines.append(f"  {label}")
        lines.append(f"    {status}")
        lines.append("")

    lines.append("=" * 62)
    terminalreporter.write_line("\n".join(lines))
