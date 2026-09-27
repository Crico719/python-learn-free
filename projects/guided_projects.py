# -*- coding: utf-8 -*-
"""
Guided Projects from the Python Learn course.
Build these step by step!
"""

def bot_part1():
    """Part 1: Simple bot that greets the user."""
    print("=" * 40)
    print("  BOT - PART 1")
    print("  Build a simple greeting bot")
    print("=" * 40)

    name = input("Bot: What is your name? ")
    print(f"Bot: Hello, {name}! Nice to meet you!")
    print("Bot: I am your Python bot. How can I help?")

def bot_part2():
    """Part 2: Interactive bot using input()."""
    print("=" * 40)
    print("  BOT - PART 2")
    print("  Make the bot interactive!")
    print("=" * 40)

    print("Bot: Hello! I am your Python bot.")
    name = input("Bot: What is your name? ")
    print(f"Bot: Nice to meet you, {name}!")

    mood = input("Bot: How are you feeling? ")
    if mood.lower() == "good":
        print("Bot: Great! I am happy too!")
    elif mood.lower() == "bad":
        print("Bot: I am sorry to hear that.")
        print("Bot: Want to hear a joke?")
        jokes = ["Why did the programmer go broke? He used up all his cache!",
                 "Why do programmers prefer dark mode? Because light attracts bugs!"]
        print(f"  {random.choice(jokes)}")
    else:
        print("Bot: I hope you feel better soon!")

    print(f"Bot: Goodbye {name}!")

import random

def lunch_party_organizer():
    """Optional project: Lunch party organizer."""
    print("=" * 40)
    print("  LUNCH PARTY ORGANIZER")
    print("=" * 40)

    guests = []
    food_preferences = {}

    while True:
        name = input("\n  Add guest name (or 'done'): ").strip()
        if name.lower() == 'done':
            break
        guests.append(name)
        preference = input(f"  Food preference for {name}: ").strip()
        food_preferences[name] = preference

    print(f"\n  Party guests: {len(guests)}")
    for guest in guests:
        print(f"    {guest}: {food_preferences[guest]}")

def school_grades():
    """Optional project: School grades program."""
    print("=" * 40)
    print("  SCHOOL GRADES PROGRAM")
    print("=" * 40)

    student = input("  Student name: ").strip()
    grades = []
    for i in range(3):
        grade = float(input(f"  Grade {i+1}: "))
        grades.append(grade)

    average = sum(grades) / len(grades)
    status = "Passed" if average >= 70 else "Failed"

    print(f"\n  Report for {student}")
    print(f"  Grades: {grades}")
    print(f"  Average: {average:.2f}")
    print(f"  Status: {status}")

def main():
    print("\n  Python Guided Projects\n")

    while True:
        print("=" * 40)
        print("  CHOOSE A PROJECT")
        print("=" * 40)
        print("  1. Bot - Part 1 (guided)")
        print("  2. Bot - Part 2 (guided)")
        print("  3. Lunch Party Organizer (optional)")
        print("  4. School Grades Program (optional)")
        print("  5. Exit")
        print()

        option = input("  Choose (1-5): ").strip()

        if option == "1":
            bot_part1()
        elif option == "2":
            bot_part2()
        elif option == "3":
            lunch_party_organizer()
        elif option == "4":
            school_grades()
        elif option == "5":
            print("\n  Goodbye! Python Snake!\n")
            break
        else:
            print("  Invalid option.")

if __name__ == "__main__":
    main()
