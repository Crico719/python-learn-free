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
    return {"completed_topics": [], "total_score": 0, "streak": 0}
def save_scores(scores):
    with open(SCORE_FILE, "w") as f: json.dump(scores, f, indent=2)
def clear_screen(): os.system("cls" if os.name == "nt" else "clear")
def print_header(title):
    clear_screen(); print("=" * 60); print(f"  PYTHON LEARN - {title}"); print("=" * 60); print()
def print_progress(c, t):
    f = int(c/t*30); bar = "#"*f + "-"*(30-f); print(f"  [{bar}] {c}/{t}"); print()
def get_input(prompt):
    try: return input(prompt).strip()
    except (EOFError, KeyboardInterrupt): print("Goodbye!"); sys.exit(0)
def complete_topic(scores, lid, tid):
    key = f"{lid}_{tid}"
    if key not in scores["completed_topics"]:
        scores["completed_topics"].append(key); scores["streak"] += 1
        scores["total_score"] += 5; save_scores(scores); return True
    return False
def load_course():
    with open(COURSE_FILE) as f: return json.load(f)
LESSONS = load_course()
def total_topics():
    return sum(len(l.get("topics", [{"exercises": l.get("exercises", [])}])) for l in LESSONS.values())
def get_all_topics():
    topics = []
    for lid in sorted(LESSONS.keys(), key=int):
        l = LESSONS[lid]
        tps = l.get("topics", [])
        if not tps: tps = [{"title": l["title"], "exercises": l.get("exercises", [])}]
        for tid, t in enumerate(tps):
            topics.append((lid, tid, l["title"], t["title"]))
    return topics
def main_menu(scores):
    while True:
        print_header("MAIN MENU")
        scores = load_scores()
        done = len(scores["completed_topics"]); total = total_topics()
        print_progress(done, total)
        print(f"  Score: {scores['total_score']} | Streak: {scores['streak']}")
        print(f"  Done: {done}/{total} topics")
        print("  1. Start next topic")
        print("  2. View lessons")
        print("  3. Quick quiz")
        print("  4. Statistics")
        print("  5. Run projects")
        print("  6. Exit")
        choice = get_input("  Choose: ")
        if choice == "1": start_next(scores)
        elif choice == "2": show_lessons(scores)
        elif choice == "3": quiz(scores)
        elif choice == "4": stats(scores)
        elif choice == "5": projects_menu()
        elif choice == "6": print("Goodbye!"); sys.exit(0)
        time.sleep(0.3)
def start_next(scores):
    done = set(scores["completed_topics"])
    remaining = [(l,t,lt,tt) for l,t,lt,tt in get_all_topics() if f"{l}_{t}" not in done]
    if not remaining:
        print_header("CONGRATULATIONS!"); print(f"  Score: {scores['total_score']}"); get_input("  Press Enter..."); return
    run_topic(scores, remaining[0][0], remaining[0][1], remaining[0][2], remaining[0][3])
def show_lessons(scores):
    print_header("LESSONS")
    for lid in sorted(LESSONS.keys(), key=int):
        l = LESSONS[lid]
        tps = l.get("topics", [])
        if not tps: tps = [{"title": l["title"], "exercises": l.get("exercises", [])}]
        print(f"  Lesson {lid}: {l['title']} ({len(tps)} topics)")
    get_input("  Press Enter...")
def run_topic(scores, lid, tid, lt, tt):
    lid = str(lid); l = LESSONS[lid]
    tps = l.get("topics", [])
    if not tps: tps = [{"title": l["title"], "exercises": l.get("exercises", [])}]
    topic = tps[tid]
    print_header(f"LESSON {lid}: {lt}")
    print(f"  Topic {tid+1}: {tt}")
    desc = topic.get("description", "")
    if desc: print(f"  {desc}")
    print("-" * 40)
    ex_list = topic.get("exercises", [])
    for i, ex in enumerate(ex_list, 1):
        print(f"  Exercise {i}: {ex['question']}")
        print(f"  Hint: {ex['hint']}")
        code = get_input("  Your code: ")
        if code.strip():
            try: exec(code, {}); print("  OK!")
            except Exception as e: print(f"  Error: {e}")
        if complete_topic(scores, lid, tid):
            print(f"  +5 points! Streak: {scores['streak']}")
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
    done = len(scores["completed_topics"]); total = total_topics()
    pct = f"{done/total*100:.1f}" if total > 0 else "0"
    print(f"  Score: {scores['total_score']} | Streak: {scores['streak']}")
    print(f"  Progress: {done}/{total} topics ({pct}%)")
    get_input("  Press Enter...")
def projects_menu():
    print_header("PROJECTS")
    print("  1. Bot Part 1")
    print("  2. Bot Part 2")
    print("  3. RPS Part 1")
    print("  4. RPS Part 2")
    print("  5. To-Do List")
    print("  6. Food Ordering")
    print("  7. Draw a Card")
    print("  8. Damage Calculator")
    print("  9. Sensor Validator")
    print("  0. Back")
    c = get_input("  Choose: ")
    codes = {
        "1": "name = input('What is your name? ')\nprint(f'Hello, {name}!')",
        "2": "print('Bot: Hello!')\nname = input('Bot: What is your name? ')\nprint(f'Bot: Nice to meet you, {name}!')\nmood = input('Bot: How are you? ')\nif mood.lower() == 'good': print('Bot: Great!')\nelse: print('Bot: Hope you feel better!')\nprint(f'Bot: Goodbye {name}!')",
        "3": "import random\noptions = ['rock','paper','scissors']\npc = random.choice(options)\nyou = input('rock/paper/scissors: ')\nprint(f'PC: {pc}')\nif you == pc: print('Tie!')\nelif (you=='rock' and pc=='scissors') or (you=='paper' and pc=='rock') or (you=='scissors' and pc=='paper'): print('You win!')\nelse: print('PC wins!')",
        "4": "import random\noptions = ['rock','paper','scissors']\nscore = 0\nfor _ in range(3):\n    pc = random.choice(options)\n    you = input('rock/paper/scissors: ')\n    if you == pc: print('Tie!')\n    elif (you=='rock' and pc=='scissors') or (you=='paper' and pc=='rock') or (you=='scissors' and pc=='paper'): score+=1; print('You win!')\n    else: print('PC wins!')\nprint(f'Final: {score}/3')",
        "5": "tasks = []\nwhile True:\n    task = input('Add task (or quit): ')\n    if task == 'quit': break\n    tasks.append(task)\n    print(f'Task added!')\nprint(f'Total: {len(tasks)}')",
        "6": "menu = {'pizza': 10, 'pasta': 8, 'salad': 5}\nfor item, price in menu.items(): print(f'{item}: ${price}')",
        "7": "import random\nsuits = ['Hearts','Diamonds','Clubs','Spades']\nranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']\ndeck = [(r,s) for s in suits for r in ranks]\nrandom.shuffle(deck)\nprint(f'Deck has {len(deck)} cards')\ncard = deck.pop()\nprint(f'You drew: {card[0]} of {card[1]}')",
        "8": "import random, math\nattack = random.randint(10, 50)\ndefense = random.randint(5, 25)\ndamage = max(0, attack - defense + math.floor(random.gauss(0, 5)))\nprint(f'Damage: {damage}')",
        "9": "import random\nclass InvalidReadingError(Exception): pass\nreadings = []\nfor i in range(10):\n    try:\n        val = random.uniform(-10, 50)\n        if val < 0 or val > 40: raise InvalidReadingError(f'Invalid: {val}')\n        readings.append(val)\n        print(f'Reading {i+1}: {val:.2f}')\n    except InvalidReadingError as e: print(f'Error: {e}')\nprint(f'Valid: {len(readings)}/10')",
    }
    if c in codes: print("\n  >>> " + codes[c] + "\n")
    get_input("  Press Enter...")
if __name__ == "__main__":
    print("  Welcome to Python Learn!")
    time.sleep(0.3)
    print("  Mimo-style course - topics, subtopics, 100% free!")
    time.sleep(0.3)
    get_input("  Press Enter to continue...")
    main_menu(load_scores())
