"""
=============================================================
  CODING TASK: Algorithm Design & Analysis in Python
  Topics: Top-down design, procedures vs functions,
          divide & conquer, backtracking, desk checking
=============================================================

INSTRUCTIONS
------------
Work through the tasks in order. Each level builds on the last.
Not everyone will reach every level — that's completely fine.
Read the comments carefully; they guide you through each step.

When you finish a level, TEST it by running the script and
checking the output matches what you'd expect from a desk check.

=============================================================
  LEVEL 1 — Procedures and Functions (All students)
  Identify, write, and call basic subroutines.
=============================================================
"""

# ----------------------------------------------------------
# TASK 1A: Identify the difference
# ----------------------------------------------------------
# Below are two subroutines. One is a PROCEDURE, one is a FUNCTION.
# Read them, then answer (in the comments below):

def greet_student(name):
    print(f"Welcome to class, {name}!")

def square(number):
    return number * number

# YOUR ANSWERS (fill in the blanks):
# greet_student is a: ___________  because: ___________
# square is a:        ___________  because: ___________


# ----------------------------------------------------------
# TASK 1B: Call them and observe the output
# ----------------------------------------------------------
# 1. Call greet_student with your own name.
# 2. Call square with the number 7 and PRINT the result.
# 3. Try printing the result of greet_student("Alex") — what do you notice?

# YOUR CODE HERE:



# ----------------------------------------------------------
# TASK 1C: Write your own function
# ----------------------------------------------------------
# Write a function called calculate_grade(score) that:
#   - Takes a numerical score as input
#   - Returns "A" if score >= 90
#   - Returns "B" if score >= 75
#   - Returns "C" if score >= 60
#   - Returns "F" otherwise
#
# (This is the same algorithm from Worksheet 2 — try it from memory first!)

def calculate_grade(score):
    # YOUR CODE HERE
    pass  # Remove this line when you add your code


# Test your function (uncomment these lines when ready):
# print(calculate_grade(95))   # Expected: A
# print(calculate_grade(80))   # Expected: B
# print(calculate_grade(62))   # Expected: C
# print(calculate_grade(40))   # Expected: F


"""
=============================================================
  LEVEL 2 — Top-Down Design: Building a Report System
  Apply structure-chart thinking in real code.
=============================================================

In this level you'll build a simple student report program
using TOP-DOWN DESIGN. The structure looks like this:

        run_report_system()
        /         |         \
get_student()  calculate_stats()  display_report()
                   /       \
           find_highest()  find_average()

You'll write each subroutine separately, then connect them.
"""

# ----------------------------------------------------------
# TASK 2A: Write the "leaf" subroutines first (bottom level)
# ----------------------------------------------------------

def find_average(scores):
    """
    INPUT:  a list of numbers (scores)
    OUTPUT: the average as a float
    Hint: sum(scores) gives you the total; len(scores) gives the count.
    """
    # YOUR CODE HERE
    pass


def find_highest(scores):
    """
    INPUT:  a list of numbers (scores)
    OUTPUT: the single highest score
    Hint: Python has a built-in max() function.
    """
    # YOUR CODE HERE
    pass


# Quick tests (uncomment to check):
# print(find_average([80, 90, 70]))   # Expected: 80.0
# print(find_highest([80, 90, 70]))   # Expected: 90


# ----------------------------------------------------------
# TASK 2B: Write the mid-level subroutine
# ----------------------------------------------------------

def calculate_stats(scores):
    """
    INPUT:  a list of scores
    OUTPUT: a dictionary with keys "average" and "highest"
    
    This function CALLS find_average() and find_highest().
    It combines their results into one package (a dictionary).
    
    Example return value: {"average": 80.0, "highest": 90}
    """
    # YOUR CODE HERE
    pass


# ----------------------------------------------------------
# TASK 2C: Write the display procedure
# ----------------------------------------------------------

def display_report(name, scores, stats):
    """
    PROCEDURE — no return value.
    Prints a formatted student report showing:
      - Student name
      - Their scores
      - Their average (from stats dictionary)
      - Their highest score (from stats dictionary)
      - Their overall grade (using calculate_grade from Level 1)
    """
    # YOUR CODE HERE
    pass


# ----------------------------------------------------------
# TASK 2D: Write the top-level function that ties it all together
# ----------------------------------------------------------

def run_report_system():
    """
    The "root" of the structure chart.
    
    1. Create a list of at least 3 students, each with a name and
       a list of scores. (You can hardcode this data for now.)
    2. For each student:
       a. Call calculate_stats() with their scores
       b. Call display_report() with their name, scores, and stats
    
    Example student data:
    students = [
        {"name": "Alex", "scores": [85, 90, 78]},
        {"name": "Sam",  "scores": [55, 60, 48]},
    ]
    """
    # YOUR CODE HERE
    pass


# Uncomment to run when all subroutines above are complete:
# run_report_system()


"""
=============================================================
  LEVEL 3 — Divide and Conquer: Binary Search
  Understand and implement a classic D&C algorithm.
=============================================================

Binary search works by DIVIDING the problem in half each time:
  - Look at the MIDDLE element of a sorted list
  - If it's the target → found it!
  - If target is SMALLER → search the LEFT half
  - If target is LARGER  → search the RIGHT half
  - Repeat until found or the list is empty

This is classic divide and conquer: each step halves the problem.
"""

# ----------------------------------------------------------
# TASK 3A: Complete the binary search function
# ----------------------------------------------------------

def binary_search(sorted_list, target):
    """
    INPUT:  a sorted list of numbers, and a target to find
    OUTPUT: the INDEX of the target, or -1 if not found
    
    Fill in the missing parts marked with ???
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2        # Integer division to find middle index
        middle_value = sorted_list[mid]

        if middle_value == target:
            return mid                  # Found it!
        elif target < middle_value:
            high = ???                  # Search LEFT half — update high
        else:
            low = ???                   # Search RIGHT half — update low

    return -1  # Target not in list


# Test cases (uncomment when ready):
# numbers = [3, 7, 12, 19, 25, 31, 44, 58, 67, 90]
# print(binary_search(numbers, 25))   # Expected: 4 (index of 25)
# print(binary_search(numbers, 10))   # Expected: -1 (not in list)
# print(binary_search(numbers, 90))   # Expected: 9


# ----------------------------------------------------------
# TASK 3B: Desk check (trace) your binary search
# ----------------------------------------------------------
# On paper (or in comments below), trace binary_search([3,7,12,19,25], 19):
#
# Step | low | high | mid | sorted_list[mid] | Action
# -----|-----|-------|-----|------------------|--------
#  1   |  0  |   4   |  2  |       12         | 19 > 12, set low = mid+1
#  2   |  ?  |   ?   |  ?  |        ?         | ?
#  3   |  ?  |   ?   |  ?  |        ?         | ?
#
# Complete the table above as a comment.


"""
=============================================================
  LEVEL 4 — Backtracking: Maze Solver  (Extension)
  A classic backtracking algorithm.
=============================================================

A maze is represented as a grid of 0s (open) and 1s (walls).
The solver starts at (0,0) and tries to reach the bottom-right.

Backtracking strategy:
  - Try moving RIGHT first
  - If that fails, try DOWN
  - If both fail → BACKTRACK (return False to caller)
  - Mark visited cells to avoid loops
"""

def solve_maze(maze, row, col, path):
    """
    INPUT:
      maze  — 2D list (0=open, 1=wall)
      row, col — current position
      path  — list of (row, col) tuples showing the route so far
    OUTPUT:
      True if a solution was found (and path is updated),
      False if this direction leads to a dead end.
    """
    rows = len(maze)
    cols = len(maze[0])

    # --- BASE CASES ---
    # Out of bounds
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False
    # Hit a wall or already visited (marked as 2)
    if maze[row][col] != 0:
        return False
    # Reached the goal (bottom-right corner)
    if row == rows - 1 and col == cols - 1:
        path.append((row, col))
        return True

    # Mark this cell as visited
    maze[row][col] = 2
    path.append((row, col))

    # --- RECURSIVE EXPLORATION ---
    # Try RIGHT, then DOWN, then LEFT, then UP
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if solve_maze(maze, row + dr, col + dc, path):
            return True  # This direction worked!

    # --- BACKTRACK ---
    # No direction worked — undo this step
    path.pop()
    maze[row][col] = 0   # Unmark so other paths can try this cell
    return False


def print_maze(maze):
    """Prints the maze in a readable grid format."""
    icons = {0: "·", 1: "█", 2: "★"}
    for row in maze:
        print("  " + " ".join(icons.get(cell, str(cell)) for cell in row))
    print()


# ----------------------------------------------------------
# TASK 4A: Run the maze solver and observe the output
# ----------------------------------------------------------

maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
]

# Uncomment to run:
# path = []
# print("Original maze:")
# print_maze([row[:] for row in maze])   # Print a copy
#
# if solve_maze(maze, 0, 0, path):
#     print(f"Solution found! Path taken: {path}")
#     print("\nMaze with path marked (★):")
#     print_maze(maze)
# else:
#     print("No solution exists.")


# ----------------------------------------------------------
# TASK 4B: Experiment (choose one or more)
# ----------------------------------------------------------
# 1. Create your own 5x5 maze (using 0s and 1s) and solve it.
# 2. Modify the solver to count how many cells it BACKTRACKS from.
# 3. Change the exploration order (try UP first, then LEFT) — does
#    it find a different path? Why or why not?
# 4. Can you create a maze with NO solution? What does the solver output?

# YOUR CODE HERE:


"""
=============================================================
  REFLECTION (answer in comments)
=============================================================

1. Which subroutines in your Level 2 report system are PROCEDURES
   and which are FUNCTIONS? How did you decide?

   YOUR ANSWER:

2. In binary search (Level 3), how many comparisons did your
   desk check take to find the target? How does this compare
   to checking every element one by one?

   YOUR ANSWER:

3. In the maze solver (Level 4), what makes this algorithm
   a "backtracking" approach? At what point does it backtrack?

   YOUR ANSWER:

4. How does the structure of your Level 2 code relate to the
   structure chart concept from Worksheet 1?

   YOUR ANSWER:
"""
