# -*- coding: utf-8 -*-
import random
import os

def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    limit = 7

    print("=" * 40)
    print("  NUMBER GUESSING GAME")
    print(f"  You have {limit} attempts")
    print("=" * 40)

    while attempts < limit:
        try:
            guess = int(input("\n  Guess a number (1-100): "))
            attempts += 1

            if guess == number:
                print(f"\n  You got it in {attempts} attempts!")
                print(f"  Points: {100 - (attempts - 1) * 10}")
                return True
            elif guess < number:
                print(f"  Too low ({limit - attempts} attempts left)")
            else:
                print(f"  Too high ({limit - attempts} attempts left)")
        except ValueError:
            print("  Please enter a valid number.")
            attempts -= 1

    print(f"\n  Out of attempts. The number was {number}")
    return False

def todo_list():
    tasks = []
    while True:
        print("\n" + "=" * 40)
        print("  TO-DO LIST")
        print("=" * 40)
        for i, task in enumerate(tasks, 1):
            status = "DONE" if task["done"] else "TODO"
            print(f"  {i}. [{status}] {task['text']}")
        print()
        print("  1. Add task")
        print("  2. Mark as done")
        print("  3. Delete task")
        print("  4. View pending")
        print("  5. Exit")

        option = input("\n  Choose: ").strip()

        if option == "1":
            text = input("  What task to add? ").strip()
            if text:
                tasks.append({"text": text, "done": False})
        elif option == "2":
            idx = int(input("  Task number to mark: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
        elif option == "3":
            idx = int(input("  Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
        elif option == "4":
            pending = [t for t in tasks if not t["done"]]
            print(f"\n  Pending: {len(pending)}")
        elif option == "5":
            break

def calculator():
    print("=" * 40)
    print("  CALCULATOR")
    print("=" * 40)
    while True:
        print("\n  Operations: +, -, *, /")
        print("  'exit' to quit")
        expr = input("  Enter operation (e.g: 5 + 3): ").strip()
        if expr.lower() == "exit":
            break
        try:
            result = eval(expr)
            print(f"  = {result}")
        except:
            print("  Invalid operation.")

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("=" * 40)
    print("  ROCK PAPER SCISSORS")
    print("=" * 40)
    scores = {"you": 0, "pc": 0}

    while True:
        print(f"\n  You: {scores['you']} | PC: {scores['pc']}")
        choice = input("  Rock/paper/scissors (or 'exit'): ").strip().lower()
        if choice == "exit":
            break
        if choice not in options:
            print("  Choose rock, paper, or scissors.")
            continue
        pc = random.choice(options)
        print(f"  PC chose: {pc}")
        if choice == pc:
            print("  Tie!")
        elif (choice == "rock" and pc == "scissors") or \
             (choice == "paper" and pc == "rock") or \
             (choice == "scissors" and pc == "paper"):
            print("  You win!")
            scores["you"] += 1
        else:
            print("  PC won.")
            scores["pc"] += 1

def main():
    print("\n  Python Projects - Learn by doing!\n")

    while True:
        print("=" * 40)
        print("  AVAILABLE PROJECTS")
        print("=" * 40)
        print("  1. Number Guessing Game")
        print("  2. To-Do List")
        print("  3. Calculator")
        print("  4. Rock Paper Scissors")
        print("  5. Exit")
        print()

        option = input("  Choose a project (1-5): ").strip()

        if option == "1":
            guessing_game()
        elif option == "2":
            todo_list()
        elif option == "3":
            calculator()
        elif option == "4":
            rock_paper_scissors()
        elif option == "5":
            print("\n  Goodbye! Python Snake!\n")
            break
        else:
            print("  Invalid option.")

if __name__ == "__main__":
    main()
