#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, json, random, time, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ANSI Colors
R = "\033[91m"; G = "\033[92m"; Y = "\033[93m"; B = "\033[94m"
M = "\033[95m"; C = "\033[96m"; W = "\033[97m"; D = "\033[90m"
BR = "\033[1;91m"; BG = "\033[1;92m"; BY = "\033[1;93m"
BB = "\033[1;94m"; BM = "\033[1;95m"; BC = "\033[1;96m"; BW = "\033[1;97m"
RESET = "\033[0m"; BOLD = "\033[1m"; DIM = "\033[2m"

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
    clear_screen()
    print(BB + "═" * 60 + RESET)
    print(BB + "  🐍 PYTHON LEARN" + RESET + "  " + BM + title + RESET)
    print(BB + "═" * 60 + RESET)
    print()

def print_progress(c, t):
    f = int(c/t*30)
    bar = BG + "█"*f + D + "░"*(30-f) + RESET
    pct = f"{c/t*100:.1f}" if t > 0 else "0"
    print(f"  {G}{bar}{RESET} {BG}{c}/{t}{RESET} ({G}{pct}%{RESET})")
    print()

def print_box(text, color=None):
    c = color or BC
    print(c + "  ╭" + "─" * 58 + "╮" + RESET)
    for line in text.split("\n"):
        padding = 58 - len(line)
        left = "│ " + line
        right = " " * padding + "│"
        print(c + left + RESET + c + right + RESET)
    print(c + "  ╰" + "─" * 58 + "╯" + RESET)
    print()

def get_input(prompt):
    try: return input(B + prompt + RESET).strip()
    except (EOFError, KeyboardInterrupt): print("\n" + D + "Goodbye! 👋" + RESET); sys.exit(0)

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

def show_welcome():
    clear_screen()
    print()
    print(C + "    ╔════════════════════════════════════════════════╗" + RESET)
    print(C + "    ║                                                ║" + RESET)
    print(BM + "    ║     🐍  PYTHON LEARN  🐍                     ║" + RESET)
    print(C + "    ║     Curso interactivo gratuito               ║" + RESET)
    print(C + "    ║     Inspirado en Mimo                        ║" + RESET)
    print(C + "    ║                                                ║" + RESET)
    print(C + "    ║     90 lecciones | 14 proyectos | Todo gratis ║" + RESET)
    print(C + "    ║                                                ║" + RESET)
    print(C + "    ╚════════════════════════════════════════════════╝" + RESET)
    print()
    time.sleep(0.5)
    print(BG + "  ⚡ Empieza tu carrera de programación!" + RESET)
    time.sleep(0.5)
    print(DIM + "  Aprende Python con lecciones interactivas" + RESET)
    time.sleep(0.5)
    print(DIM + "  Sin costo, sin compromiso, solo código 🚀" + RESET)
    print()
    get_input(f"  {G}▶ Presiona Enter para empezar...{RESET}")

def main_menu(scores):
    while True:
        clear_screen()
        print(BB + "═" * 60 + RESET)
        print(BB + "  🐍 PYTHON LEARN" + RESET + "  " + BW + "MENÚ PRINCIPAL" + RESET)
        print(BB + "═" * 60 + RESET)
        scores = load_scores()
        done = len(scores["completed_topics"]); total = total_topics()
        print_progress(done, total)
        print(f"  {G}⭐ Puntaje:{RESET} {BG}{scores['total_score']}{RESET}  {M}🔥 Racha:{RESET} {BG}{scores['streak']}{RESET}")
        print(f"  {C}📚 Progreso:{RESET} {BG}{done}/{total}{RESET}")
        print()
        print(f"  {BW}1.{RESET} {G}▶ Siguiente tema{RESET}")
        print(f"  {BW}2.{RESET} {C}📖 Ver todas las lecciones{RESET}")
        print(f"  {BW}3.{RESET} {M}⚡ Quiz rápido{RESET}")
        print(f"  {BW}4.{RESET} {Y}📊 Estadísticas{RESET}")
        print(f"  {BW}5.{RESET} {BR}🛠️  Proyectos{RESET}")
        print(f"  {BW}6.{RESET} {D}🚪 Salir{RESET}")
        print()
        choice = get_input(f"  {BY}Elige: {RESET}")
        if choice == "1": start_next(scores)
        elif choice == "2": show_lessons(scores)
        elif choice == "3": quiz(scores)
        elif choice == "4": stats(scores)
        elif choice == "5": projects_menu()
        elif choice == "6":
            print()
            print(D + "  👋 ¡Hasta luego! Sigue practicando cada día! 🐍" + RESET)
            print(D + "  🌟 ¡Tu futuro como programador te espera! 🚀" + RESET)
            sys.exit(0)
        time.sleep(0.3)

def start_next(scores):
    done = set(scores["completed_topics"])
    remaining = [(l,t,lt,tt) for l,t,lt,tt in get_all_topics() if f"{l}_{t}" not in done]
    if not remaining:
        clear_screen()
        print(C + "    ╔════════════════════════════════════════════════╗" + RESET)
        print(BG + "    ║          🎉 ¡FELICIDADES! 🎉                ║" + RESET)
        print(C + "    ║                                                ║" + RESET)
        print(BG + f"    ║  ¡Completaste todo el curso!                  ║" + RESET)
        print(BG + f"    ║  Puntaje final: {scores['total_score']}           ║" + RESET)
        print(BG + f"    ║  Racha: {scores['streak']} lecciones             ║" + RESET)
        print(C + "    ║                                                ║" + RESET)
        print(C + "    ╚════════════════════════════════════════════════╝" + RESET)
        print()
        print(BG + "  🐍 Ahora eres un programador de Python! 🚀" + RESET)
        print(DIM + "  ¡Sigue construyendo cosas con lo que aprendiste!" + RESET)
        get_input(f"  {G}▶ Presiona Enter...{RESET}")
        return
    lid, tid, lt, tt = remaining[0]
    run_topic(scores, lid, tid, lt, tt)

def show_lessons(scores):
    print_header("TODAS LAS LECCIONES")
    scores = load_scores()
    done = set(scores["completed_topics"])
    for lid in sorted(LESSONS.keys(), key=int):
        l = LESSONS[lid]
        tps = l.get("topics", [])
        if not tps: tps = [{"title": l["title"], "exercises": l.get("exercises", [])}]
        icon = "🟢" if all(f"{lid}_{t}" in done for t in range(len(tps))) else ("🟡" if any(f"{lid}_{t}" in done for t in range(len(tps))) else "🔴")
        print(f"  {icon} Lección {lid}: {BW}{l['title']}{RESET} ({len(tps)} temas)")
    print()
    get_input(f"  {G}▶ Presiona Enter...{RESET}")

def run_topic(scores, lid, tid, lt, tt):
    lid = str(lid); l = LESSONS[lid]
    tps = l.get("topics", [])
    if not tps: tps = [{"title": l["title"], "exercises": l.get("exercises", [])}]
    topic = tps[tid]
    print_header(f"LECCIÓN {lid}")
    print(f"  {BM}{lt}{RESET}")
    print(f"  {C}▸ Tema {tid+1}: {BW}{tt}{RESET}")
    desc = topic.get("description", "")
    if desc: print(f"  {D}{desc}{RESET}")
    print(f"  {D}{'─' * 50}{RESET}")
    ex_list = topic.get("exercises", [])
    for i, ex in enumerate(ex_list, 1):
        print(f"\n  {Y}Ejercicio {i}: {RESET}{ex['question']}")
        print(f"  {D}💡 Pista: {ex['hint']}{RESET}")
        code = get_input(f"  {G}Escribe tu código: {RESET}")
        if code.strip():
            try: exec(code, {}); print(f"  {G}✅ ¡Correcto!{RESET}")
            except Exception as e: print(f"  {R}❌ Error: {e}{RESET}")
        if complete_topic(scores, lid, tid):
            print(f"  {BG}+5 puntos! 🔥 Racha: {scores['streak']}{RESET}")
    print()
    if "project_code" in l:
        print(f"  {BC}💻 Código del proyecto:{RESET}")
        print(f"  {D}{l['project_code']}{RESET}")
    get_input(f"  {G}▶ Presiona Enter...{RESET}")

def quiz(scores):
    print_header("QUIZ RÁPIDO ⚡")
    keys = list(LESSONS.keys()); random.shuffle(keys); sel = keys[:5]; correct = 0
    print(f"  {M}Responderás 5 preguntas de lecciones aleatorias{RESET}\n")
    for k in sel:
        print(f"  {C}Lección {k}: {LESSONS[k]['title']}{RESET}")
        a = get_input(f"  {BY}¿La conoces? (si/no): {RESET}")
        if a in ["s","si","yes"]: correct += 1
    print()
    if correct == 5: print(f"  {BG}🏆 ¡Perfecto! Eres un crack de Python!{RESET}")
    elif correct >= 3: print(f"  {G}👍 ¡Buen trabajo! Sigue practicando.{RESET}")
    else: print(f"  {Y}📚 ¡Sigue estudiando! Puedes hacerlo mejor.{RESET}")
    scores["total_score"] += correct*5; save_scores(scores)
    get_input(f"  {G}▶ Presiona Enter...{RESET}")

def stats(scores):
    scores = load_scores(); print_header("ESTADÍSTICAS 📊")
    done = len(scores["completed_topics"]); total = total_topics()
    pct = f"{done/total*100:.1f}" if total > 0 else "0"
    print(f"  {G}⭐ Puntaje total:{RESET} {BG}{scores['total_score']}{RESET}")
    print(f"  {M}🔥 Racha actual:{RESET} {BG}{scores['streak']}{RESET}")
    print(f"  {C}📚 Progreso:{RESET} {BG}{done}/{total}{RESET} ({G}{pct}%{RESET})")
    if scores["completed_topics"]:
        print(f"\n  {BW}Últimos temas completados:{RESET}")
        recent = sorted(scores["completed_topics"], key=lambda x: int(x.split("_")[0]))[-5:]
        for key in recent:
            lid, tid = key.split("_")
            print(f"    {G}✅ Lección {lid}, Tema {tid}{RESET}")
    print()
    get_input(f"  {G}▶ Presiona Enter...{RESET}")

def projects_menu():
    while True:
        print_header("PROYECTOS 🛠️")
        print(f"  {BR}1.{RESET} 🤖 Bot Parte 1")
        print(f"  {BR}2.{RESET} 🤖 Bot Parte 2")
        print(f"  {BR}3.{RESET} ✊✋✌️ RPS Parte 1")
        print(f"  {BR}4.{RESET} ✊✋✌️ RPS Parte 2")
        print(f"  {BR}5.{RESET} 📝 To-Do List")
        print(f"  {BR}6.{RESET} 🍕 Sistema de Pedidos")
        print(f"  {BR}7.{RESET} 🃏 Draw a Card")
        print(f"  {BR}8.{RESET} 💥 Calculadora de Daños")
        print(f"  {BR}9.{RESET} 📡 Sensor Validator")
        print(f"  {D}0.{RESET} Volver")
        c = get_input(f"  {BY}Elige: {RESET}")
        if c == "0": return
        codes = {
            "1": f"{G}name = input('What is your name? ')\nprint(f'Hello, {name}!'){RESET}",
            "2": f"{G}print('Bot: Hello!')\nname = input('Bot: What is your name? ')\nprint(f'Bot: Nice to meet you, {name}!'){RESET}",
            "3": f"{G}import random\noptions = ['rock','paper','scissors']\npc = random.choice(options)\nyou = input('rock/paper/scissors: ')\nprint(f'PC: {pc}')\nif you == pc: print('Tie!'){RESET}",
            "4": f"{G}import random\noptions = ['rock','paper','scissors']\nscore = 0\nfor _ in range(3):\n    pc = random.choice(options)\n    you = input('rock/paper/scissors: ')\n    if you == pc: print('Tie!')\n    elif (you=='rock' and pc=='scissors') or (you=='paper' and pc=='rock') or (you=='scissors' and pc=='paper'): score+=1; print('You win!')\n    else: print('PC wins!')\nprint(f'Final: {score}/3'){RESET}",
            "5": f"{G}tasks = []\nwhile True:\n    task = input('Add task (or quit): ')\n    if task == 'quit': break\n    tasks.append(task)\n    print(f'Task added!'){RESET}",
            "6": f"{G}menu = {{'pizza': 10, 'pasta': 8, 'salad': 5}}\nfor item, price in menu.items(): print(f'{item}: ${price}'){RESET}",
            "7": f"{G}import random\nsuits = ['Hearts','Diamonds','Clubs','Spades']\nranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']\ndeck = [(r,s) for s in suits for r in ranks]\nrandom.shuffle(deck)\nprint(f'Deck has {len(deck)} cards')\ncard = deck.pop()\nprint(f'You drew: {card[0]} of {card[1]}'){RESET}",
            "8": f"{G}import random, math\nattack = random.randint(10, 50)\ndefense = random.randint(5, 25)\ndamage = max(0, attack - defense + math.floor(random.gauss(0, 5)))\nprint(f'Damage: {damage}'){RESET}",
            "9": f"{G}import random\nclass InvalidReadingError(Exception): pass\nreadings = []\nfor i in range(10):\n    try:\n        val = random.uniform(-10, 50)\n        if val < 0 or val > 40: raise InvalidReadingError(f'Invalid: {val}')\n        readings.append(val)\n        print(f'Reading {i+1}: {val:.2f}')\n    except InvalidReadingError as e: print(f'Error: {e}')\nprint(f'Valid: {len(readings)}/10'){RESET}",
        }
        if c in codes: print(f"\n  {BC}{'─'*50}{RESET}\n  {codes[c]}\n  {BC}{'─'*50}{RESET}\n")
        get_input(f"  {G}▶ Presiona Enter...{RESET}")

if __name__ == "__main__":
    show_welcome()
    main_menu(load_scores())
