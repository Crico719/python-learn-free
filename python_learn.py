#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, json, random, time, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
SCORE_FILE = os.path.join(DATA_DIR, "scores.json")
COURSE_FILE = os.path.join(DATA_DIR, "course.json")
os.makedirs(DATA_DIR, exist_ok=True)

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE) as f: return json.load(f)
    return {"total_score": 0, "completed_lessons": [], "streak": 0}

def save_scores(scores):
    with open(SCORE_FILE, "w") as f: json.dump(scores, f, indent=2)

def clear_screen(): os.system("cls" if os.name == "nt" else "clear")

def print_header(title):
    clear_screen()
    print("=" * 60); print(f"  PYTHON LEARN - {title}"); print("=" * 60); print()

def print_progress(c, t):
    f = int(c/t*30); print(f"  [{'#'*f+'-'*(30-f)}] {c}/{t} lessons"); print()

def get_input(prompt):
    try: return input(prompt).strip()
    except (EOFError, KeyboardInterrupt): print("Goodbye!"); sys.exit(0)

def complete(scores, lid):
    if lid not in scores["completed_lessons"]:
        scores["completed_lessons"].append(lid); scores["streak"] += 1
        scores["total_score"] += 10; save_scores(scores); return True
    return False

def load_course():
    with open(COURSE_FILE) as f: return json.load(f)

LESSONS = load_course()
TOTAL_LESSONS = len(LESSONS)

def main_menu(scores):
    while True:
        print_header("MAIN MENU")
        scores = load_scores()
        print_progress(len(scores["completed_lessons"]), TOTAL_LESSONS)
        print(f"  Score: {scores['total_score']} | Streak: {scores['streak']}")
        print(f"  Done: {len(scores['completed_lessons'])}/{TOTAL_LESSONS}")
        print("  1. View all lessons")
        print("  2. Start next lesson")
        print("  3. Repeat a lesson")
        print("  4. Quick quiz")
        print("  5. Statistics")
        print("  6. Run projects")
        print("  7. Exit")
        choice = get_input("  Choose: ")
        if choice == "1": show_all(scores)
        elif choice == "2": start_next(scores)
        elif choice == "3": repeat(scores)
        elif choice == "4": quiz(scores)
        elif choice == "5": stats(scores)
        elif choice == "6": projects_menu()
        elif choice == "7": print("Goodbye!"); sys.exit(0)
        time.sleep(0.3)

def show_all(scores):
    print_header("ALL LESSONS")
    print_progress(len(scores["completed_lessons"]), TOTAL_LESSONS)
    for lid in sorted(LESSONS.keys(), key=int):
        s = "DONE" if lid in scores["completed_lessons"] else "TODO"
        l = LESSONS[lid]
        icon = "[P]" if l.get("type") == "PROJECT_GUIDED" else ("[R]" if l.get("type") == "PRACTICE" else "")
        print(f"  [{s}] {lid}. {l['title']} {icon}")
    get_input("  Press Enter...")

def start_next(scores):
    done = set(scores["completed_lessons"])
    remaining = [i for i in sorted(LESSONS.keys(), key=int) if i not in done]
    if not remaining:
        print_header("CONGRATULATIONS!"); print(f"  Score: {scores['total_score']}"); get_input("  Press Enter..."); return
    run_lesson(remaining[0], scores)

def repeat(scores):
    print_header("REPEAT"); done = set(scores["completed_lessons"])
    if not done: print("No lessons done yet!"); get_input("  Press Enter..."); return
    print("Choose a lesson:")
    for lid in sorted(done, key=int): print(f"  {lid}. {LESSONS[lid]['title']}")
    try:
        c = int(get_input("  Number: "))
        if str(c) in done: run_lesson(c, scores)
        else: print("Invalid!")
    except ValueError: print("Enter a number!")

def run_lesson(lid, scores):
    lid = str(lid); l = LESSONS[lid]
    print_header(f"LESSON {lid}: {l['title']}")
    if "type" in l and l["type"] == "PROJECT_GUIDED":
        print(f"  *** GUIDED PROJECT - Part {l.get('project_part', '?')} ***")
    for i, ex in enumerate(l.get("exercises", []), 1):
        print(f"  {i}. {ex['question']}")
        print(f"  Hint: {ex['hint']}")
        code = get_input("  Your code: ")
        if code.strip():
            try: exec(code, {}); print("  OK!")
            except Exception as e: print(f"  Error: {e}")
        if complete(scores, lid): print(f"  +10 points! Streak: {scores['streak']}")
    if "project_code" in l:
        print("\n  Project code:\n" + l["project_code"])
    get_input("  Press Enter...")

def quiz(scores):
    print_header("QUICK QUIZ")
    keys = list(LESSONS.keys()); random.shuffle(keys); sel = keys[:5]; correct = 0
    for k in sel:
        print(f"  Lesson {k}: {LESSONS[k]['title']}")
        a = get_input("  Know it? (yes/no): ")
        if a in ["s","si","yes"]: correct += 1
    print(f"  {correct}/5 correct!"); scores["total_score"] += correct*5; save_scores(scores)
    get_input("  Press Enter...")

def stats(scores):
    scores = load_scores(); print_header("STATISTICS")
    print(f"  Score: {scores['total_score']} | Streak: {scores['streak']}")
    print(f"  Done: {len(scores['completed_lessons'])}/{TOTAL_LESSONS}")
    if scores["completed_lessons"]:
        print("  Completed lessons:")
        for lid in sorted(scores["completed_lessons"]): print(f"    {lid}. {LESSONS[lid]['title']}")
    get_input("  Press Enter...")

def projects_menu():
    while True:
        print_header("PROJECTS")
        print("  1. Bot Part 1")
        print("  2. Bot Part 2")
        print("  3. RPS Part 1")
        print("  4. RPS Part 2")
        print("  5. To-Do List Part 1")
        print("  6. To-Do List Part 2")
        print("  7. Food Ordering Part 1")
        print("  8. Food Ordering Part 2")
        print("  9. Draw a Card Part 1")
        print("  10. Draw a Card Part 2")
        print("  11. Damage Calculator Part 1")
        print("  12. Sensor Validator Part 1")
        print("  0. Back")
        c = get_input("  Choose: ")
        if c == "0": return
        codes = {
            "1": "name = input('What is your name? ')\nprint(f'Hello, {name}!')",
            "2": "print('Bot: Hello!')\nname = input('Bot: What is your name? ')\nprint(f'Bot: Nice to meet you, {name}!')\nmood = input('Bot: How are you? ')\nif mood.lower() == 'good': print('Bot: Great!')\nelse: print('Bot: Hope you feel better!')\nprint(f'Bot: Goodbye {name}!')",
            "3": "import random\noptions = ['rock','paper','scissors']\npc = random.choice(options)\nyou = input('rock/paper/scissors: ')\nprint(f'PC: {pc}')\nif you == pc: print('Tie!')\nelif (you=='rock' and pc=='scissors') or (you=='paper' and pc=='rock') or (you=='scissors' and pc=='paper'): print('You win!')\nelse: print('PC wins!')",
            "4": "import random\noptions = ['rock','paper','scissors']\nscore = 0\nfor _ in range(3):\n    pc = random.choice(options)\n    you = input('rock/paper/scissors: ')\n    if you == pc: print('Tie!')\n    elif (you=='rock' and pc=='scissors') or (you=='paper' and pc=='rock') or (you=='scissors' and pc=='paper'): score+=1; print('You win!')\n    else: print('PC wins!')\nprint(f'Final: {score}/3')",
            "5": "tasks = []\nwhile True:\n    task = input('Add task (or quit): ')\n    if task == 'quit': break\n    tasks.append(task)\n    print(f'Task added!')\nprint(f'Total: {len(tasks)}')",
            "6": "tasks = []\nwhile True:\n    print('\\n1.Add 2.Remove 3.Show 4.Quit')\n    cmd = input('Choose: ')\n    if cmd == '1': tasks.append(input('Task: '))\n    elif cmd == '2':\n        if tasks: tasks.pop(int(input('Num: '))-1)\n    elif cmd == '3': print(tasks)\n    elif cmd == '4': break",
            "7": "menu = {'pizza': 10, 'pasta': 8, 'salad': 5}\nprint('Menu:')\nfor item, price in menu.items(): print(f'  {item}: ${price}')\norder = input('What would you like? ')\nif order in menu: print(f'Your {order} costs ${menu[order]}')\nelse: print('Not on menu')",
            "8": "cuisines = {'italian': {'pizza': 10, 'pasta': 8}, 'mexican': {'taco': 5, 'burrito': 8}, 'japanese': {'sushi': 12, 'ramen': 9}}\nfor cuisine, items in cuisines.items():\n    print(f'\\n{cuisine.title()}:')\n    for item, price in items.items(): print(f'  {item}: ${price}')\nprint('Total cuisines:', len(cuisines))",
            "9": "import random\nsuits = ['Hearts','Diamonds','Clubs','Spades']\nranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']\ndeck = [(r,s) for s in suits for r in ranks]\nrandom.shuffle(deck)\nprint(f'Deck has {len(deck)} cards')\ncard = deck.pop()\nprint(f'You drew: {card[0]} of {card[1]}')",
            "10": "import random\nsuits = ['Hearts','Diamonds','Clubs','Spades']\nranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']\nvalues = {str(i): i for i in range(2,11)}; values.update({'A':11,'J':10,'Q':10,'K':10})\ndeck = [(r,s) for s in suits for r in ranks]\nrandom.shuffle(deck)\ntotal = 0\nfor _ in range(2):\n    card = deck.pop()\n    total += values[card[0]]\n    print(f'Drew {card[0]} of {card[1]} -> Total: {total}')\nprint(f'Final total: {total}')",
            "11": "import random, math\nattack = random.randint(10, 50)\ndefense = random.randint(5, 25)\ndamage = max(0, attack - defense + math.floor(random.gauss(0, 5)))\nprint(f'Attack: {attack}, Defense: {defense}, Damage: {damage}')",
            "12": "import random\nclass InvalidReadingError(Exception): pass\ndef read_sensor():\n    val = random.uniform(-10, 50)\n    if val < 0 or val > 40: raise InvalidReadingError(f'Invalid reading: {val}')\n    return val\nreadings = []\nfor i in range(10):\n    try:\n        r = read_sensor()\n        readings.append(r)\n        print(f'Reading {i+1}: {r:.2f}')\n    except InvalidReadingError as e: print(f'Error: {e}')\nif readings: print(f'Valid readings: {len(readings)}/10')",
        }
        if c in codes: print("\n  >>> "+codes[c]+"\n")
        else: print("Invalid!")
        get_input("  Press Enter...")

if __name__ == "__main__":
    print("  Welcome to Python Learn!")
    time.sleep(0.3)
    print("  Mimo-style course - 90 lessons, 100% free!")
    time.sleep(0.3)
    get_input("  Press Enter to continue...")
    main_menu(load_scores())
