# -*- coding: utf-8 -*-
import sys
import os
import json
import random
import time
import traceback
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
SCORE_FILE = os.path.join(DATA_DIR, "scores.json")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {"total_score": 0, "completed_lessons": [], "streak": 0}

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_slow(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header(title):
    clear_screen()
    print("=" * 60)
    print(f"  PYTHON LEARN - {title}")
    print("=" * 60)
    print()

def print_progress(completed, total):
    bar_length = 30
    filled = int((completed / total) * bar_length)
    bar = "#" * filled + "-" * (bar_length - filled)
    print(f"  [{bar}] {completed}/{total} lessons")
    print()

def get_input(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye! Python Snake!")
        sys.exit(0)

def check_answer(user_answer, correct_answer, lesson_num):
    user_answer = user_answer.strip().lower()
    correct_answer = str(correct_answer).strip().lower()
    if user_answer == correct_answer:
        return True
    return False

def lesson_complete(scores, lesson_id):
    if lesson_id not in scores["completed_lessons"]:
        scores["completed_lessons"].append(lesson_id)
        scores["streak"] += 1
        scores["total_score"] += 10
        save_scores(scores)
        return True
    return False

# ============================================================
# LECCIONES
# ============================================================

LESSONS = {
    1: {
        "title": "Hello World",
        "theory": """
        In Python, we use print() to show text on screen.
        It is the first function every programmer must know!

        Example:
            print("Hello, World!")
            print("I am learning Python")
        """,
        "exercises": [
            {
                "question": "Write code to print 'Hello, Python'",
                "answer": 'print("Hello, Python")',
                "hint": "Use the print() function with quotes"
            }
        ]
    },
    2: {
        "title": "Variables and Data Types",
        "theory": """
        In Python, variables store data. You don't need to declare the type:

        name = "Ana"          # string (text)
        age = 25              # int (integer)
        height = 1.70         # float (decimal)
        is_student = True     # bool (boolean)

        You can use type() to check the type:
            type(age)  # <class 'int'>
        """,
        "exercises": [
            {
                "question": "Create a variable 'name' with your name and print it",
                "answer": 'name = "your_name"\nprint(name)',
                "hint": "Assign a string to the variable and use print()"
            }
        ]
    },
    3: {
        "title": "Arithmetic Operators",
        "theory": """
        Python supports the same operators as a calculator:

        +  Addition    5 + 3 = 8
        -  Subtraction 5 - 3 = 2
        *  Multiplication  5 * 3 = 15
        /  Division    6 / 3 = 2.0
        // Integer Division 7 // 2 = 3
        %  Modulo      7 % 2 = 1
        ** Exponent   2 ** 3 = 8
        """,
        "exercises": [
            {
                "question": "Calculate the area of a circle with radius 5 (use 3.14159 as pi)",
                "answer": "print(3.14159 * 5 ** 2)",
                "hint": "Area = pi * radius^2. Use ** to square"
            }
        ]
    },
    4: {
        "title": "Conditionals if/elif/else",
        "theory": """
        Conditionals let you make decisions in your code:

        age = 18
        if age >= 18:
            print("You are an adult")
        elif age >= 13:
            print("You are a teenager")
        else:
            print("You are a child")

        The colons (:) are mandatory and indentation is key in Python.
        """,
        "exercises": [
            {
                "question": "Write code that asks for a number and prints if it is even or odd",
                "answer": 'num = int(input("Num: "))\nif num % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")',
                "hint": "Use % (modulo) to check if even. num % 2 == 0 means even"
            }
        ]
    },
    5: {
        "title": "Loops for and while",
        "theory": """
        Loops repeat code multiple times:

        # For loop
        for i in range(5):
            print(i)  # prints 0,1,2,3,4

        # While loop
        counter = 0
        while counter < 5:
            print(counter)
            counter += 1

        Watch out for infinite loops!
        """,
        "exercises": [
            {
                "question": "Use a for loop to print numbers 1 to 5",
                "answer": "for i in range(1, 6):\n    print(i)",
                "hint": "range(1, 6) generates 1,2,3,4,5"
            }
        ]
    },
    6: {
        "title": "Lists",
        "theory": """
        Lists store multiple values in one variable:

        fruits = ["apple", "banana", "cherry"]
        numbers = [1, 2, 3, 4, 5]

        Access elements by index (starts at 0):
            fruits[0]    # "apple"
            fruits[-1]   # "cherry" (last)

        Useful methods:
            fruits.append("grape")  # add to end
            len(fruits)           # number of elements
        """,
        "exercises": [
            {
                "question": "Create a list with 3 colors and print each with a loop",
                "answer": 'colors = ["red", "blue", "green"]\nfor c in colors:\n    print(c)',
                "hint": "Create a list with strings and use for to iterate"
            }
        ]
    },
    7: {
        "title": "Functions",
        "theory": """
        Functions organize and reuse your code:

        def greet(name):
            return f"Hello, {name}!"

        message = greet("Ana")
        print(message)  # "Hello, Ana!"

        The word def defines a function. return sends the result.
        """,
        "exercises": [
            {
                "question": "Create a function that takes a number and returns its double",
                "answer": "def double(n):\n    return n * 2",
                "hint": "Use def to define the function and return for the result"
            }
        ]
    },
    8: {
        "title": "Strings and Text Methods",
        "theory": """
        Strings have many useful methods:

        text = "  hello world  "
        text.upper()        # "  HELLO WORLD  "
        text.strip()        # "hello world"
        text.replace("world", "Python")  # "  hello Python  "
        text.split()        # ["hello", "world"]
        "python".upper()     # "PYTHON"
        "PYTHON".lower()     # "python"
        """,
        "exercises": [
            {
                "question": "Given text = 'python', print it in uppercase",
                "answer": "text = 'python'\nprint(text.upper())",
                "hint": "Use the .upper() method of the string"
            }
        ]
    },
    9: {
        "title": "Dictionaries",
        "theory": """
        Dictionaries store data in key-value pairs:

        person = {
            "name": "Ana",
            "age": 25,
            "city": "Lima"
        }

        Access values by key:
            person["name"]  # "Ana"

        Methods:
            person.keys()    # all keys
            person.values()  # all values
            person.items()   # key-value pairs
        """,
        "exercises": [
            {
                "question": "Create a student dictionary with 'name' and 'grade' keys, print the grade",
                "answer": 'student = {"name": "Ana", "grade": 90}\nprint(student["grade"])',
                "hint": "Create the dictionary with {} and access with []"
            }
        ]
    },
    10: {
        "title": "File Handling",
        "theory": """
        Python can read and write files easily:

        # Write
        with open("file.txt", "w") as f:
            f.write("Hello world")

        # Read
        with open("file.txt", "r") as f:
            content = f.read()

        with open() ensures the file is closed automatically.
        """,
        "exercises": [
            {
                "question": "Create a file 'greeting.txt' containing 'Learning Python'",
                "answer": 'with open("greeting.txt", "w") as f:\n    f.write("Learning Python")',
                "hint": "Use open() with mode 'w' and the write() method"
            }
        ]
    },
    11: {
        "title": "List Comprehensions",
        "theory": """
        List comprehensions are concise ways to create lists:

        # Create squares of 1 to 5
        squares = [x**2 for x in range(1, 6)]
        # [1, 4, 9, 16, 25]

        # With condition
        evens = [x for x in range(10) if x % 2 == 0]
        # [0, 2, 4, 6, 8]

        One of Python's most powerful features.
        """,
        "exercises": [
            {
                "question": "Create a list with the squares of numbers 1 to 4",
                "answer": "squares = [x**2 for x in range(1, 5)]",
                "hint": "Use range(1, 5) and x**2 inside a list comprehension"
            }
        ]
    },
    12: {
        "title": "Try/Except - Error Handling",
        "theory": """
        Errors can stop your program. Use try/except to handle them:

        try:
            number = int(input("Enter a number: "))
            print(f"It is a number: {number}")
        except ValueError:
            print("That is not a valid number!")

        You can also use finally which always runs.
        """,
        "exercises": [
            {
                "question": "Write a try/except that tries to convert 'abc' to int",
                "answer": "try:\n    x = int('abc')\nexcept ValueError:\n    print('Error')",
                "hint": "Use try with int() and except ValueError to catch the error"
            }
        ]
    }
}

TOTAL_LESSONS = len(LESSONS)

# ============================================================
# MAIN MENU
# ============================================================

def main_menu(scores):
    while True:
        print_header("MAIN MENU")
        scores = load_scores()
        print_progress(len(scores["completed_lessons"]), TOTAL_LESSONS)
        print(f"  Total score: {scores['total_score']}")
        print(f"  Current streak: {scores['streak']}")
        print(f"  Lessons done: {len(scores['completed_lessons'])}/{TOTAL_LESSONS}")
        print()
        print("  1. View all lessons")
        print("  2. Start next lesson")
        print("  3. Repeat a lesson")
        print("  4. Play quick quiz")
        print("  5. View statistics")
        print("  6. View final project")
        print("  7. Exit")
        print()
        choice = get_input("  Choose an option: ")

        if choice == "1":
            show_all_lessons(scores)
        elif choice == "2":
            start_next_lesson(scores)
        elif choice == "3":
            repeat_lesson(scores)
        elif choice == "4":
            quiz_mode(scores)
        elif choice == "5":
            show_stats(scores)
        elif choice == "6":
            show_final_project(scores)
        elif choice == "7":
            print("\n  Thanks for learning with Python Learn!")
            print("  Keep practicing every day!\n")
            sys.exit(0)
        else:
            print("  Invalid option. Try again.")
            time.sleep(1)

def show_all_lessons(scores):
    print_header("ALL LESSONS")
    print_progress(len(scores["completed_lessons"]), TOTAL_LESSONS)
    print()
    for i in range(1, TOTAL_LESSONS + 1):
        status = "DONE" if i in scores["completed_lessons"] else "TODO"
        print(f"  [{status}] Lesson {i}: {LESSONS[i]['title']}")
    print()
    get_input("  Press Enter to go back...")

def start_next_lesson(scores):
    completed = set(scores["completed_lessons"])
    next_lessons = [i for i in range(1, TOTAL_LESSONS + 1) if i not in completed]
    if not next_lessons:
        print_header("CONGRATULATIONS!")
        print("  You have completed all lessons!")
        print(f"  Final score: {scores['total_score']}")
        get_input("  Press Enter to go back...")
        return
    next_lesson = next_lessons[0]
    run_lesson(next_lesson, scores)

def repeat_lesson(scores):
    print_header("REPEAT LESSON")
    completed = set(scores["completed_lessons"])
    available = [i for i in range(1, TOTAL_LESSONS + 1) if i in completed]
    if not available:
        print("  You have not completed any lesson yet.")
        get_input("  Press Enter to go back...")
        return
    print("  Choose a lesson to repeat:")
    for i in available:
        print(f"    {i}. {LESSONS[i]['title']}")
    print()
    try:
        choice = int(get_input("  Lesson number: "))
        if choice in available:
            run_lesson(choice, scores)
        else:
            print("  Invalid option.")
            time.sleep(1)
    except ValueError:
        print("  You must enter a number.")
        time.sleep(1)

def run_lesson(lesson_num, scores):
    lesson = LESSONS[lesson_num]
    print_header(f"LESSON {lesson_num}: {lesson['title']}")
    print(lesson["theory"])
    print("-" * 60)
    print("  EXERCISES")
    print("-" * 60)
    print()

    for idx, exercise in enumerate(lesson["exercises"], 1):
        print(f"  Exercise {idx}: {exercise['question']}")
        print(f"  Hint: {exercise['hint']}")
        print()
        user_code = get_input("  Write your code here: ")

        if user_code.strip() == "":
            print("  You didn't write anything. Try again.")
            continue

        print(f"\n  Your code:\n    {user_code}")
        print()

        try:
            exec(user_code, {})
            print("  Code executed successfully!")
        except Exception as e:
            print(f"  Error: {e}")
            print("  Try again or use 'skip' to continue.")

        if lesson_complete(scores, lesson_num):
            print(f"\n  Lesson {lesson_num} completed! +10 points")
            print(f"  Streak: {scores['streak']}")

        print()

    get_input("  Press Enter to go back...")

def quiz_mode(scores):
    print_header("QUICK QUIZ")
    keys = list(LESSONS.keys())
    random.shuffle(keys)
    selected = keys[:5]
    correct = 0

    for lesson_num in selected:
        lesson = LESSONS[lesson_num]
        print(f"\n  Lesson {lesson_num}: {lesson['title']}")
        print(f"  Quick answer: {lesson['exercises'][0]['hint']}")
        answer = get_input("  Your answer (yes/no): ").strip().lower()
        if answer in ["s", "si", "yes"]:
            correct += 1

    print(f"\n  Result: {correct}/5 correct")
    if correct == 5:
        print("  Perfect! You are a Python master!")
    elif correct >= 3:
        print("  Good job! Keep practicing.")
    else:
        print("  Keep studying! You can do better.")

    scores["total_score"] += correct * 5
    save_scores(scores)
    get_input("\n  Press Enter to go back...")

def show_stats(scores):
    scores = load_scores()
    print_header("STATISTICS")
    print(f"  Total score: {scores['total_score']}")
    print(f"  Current streak: {scores['streak']}")
    print(f"  Lessons completed: {len(scores['completed_lessons'])}/{TOTAL_LESSONS}")
    print(f"  Percentage: {len(scores['completed_lessons'])/TOTAL_LESSONS*100:.1f}%")
    print()
    if scores["completed_lessons"]:
        print("  Completed lessons:")
        for lid in sorted(scores["completed_lessons"]):
            print(f"    Lesson {lid}: {LESSONS[lid]['title']}")
    print()
    get_input("  Press Enter to go back...")

def show_final_project(scores):
    print_header("FINAL PROJECT")
    print("""
  You have completed the Python course! Now create a project.
  Here are some ideas:

  1. Number guessing game
  2. To-do list
  3. Expense calculator
  4. Weather app (using APIs)
  5. Rock Paper Scissors

  Choose a project and start building!
  Python is your tool!

  Base code for the guessing game:

    import random
    number = random.randint(1, 100)
    attempts = 0
    while True:
        attempts += 1
        guess = int(input("Guess (1-100): "))
        if guess == number:
            print(f"You got it in {attempts} attempts!")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
    """)
    get_input("  Press Enter to go back...")

# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    ensure_data_dir()
    scores = load_scores()

    print_slow("  Welcome to Python Learn!", 0.05)
    time.sleep(0.5)
    print_slow("  Learn Python with interactive lessons.", 0.05)
    time.sleep(0.5)
    print_slow("  100% free!", 0.05)
    time.sleep(0.5)
    get_input("  Press Enter to continue...")
    main_menu(scores)
