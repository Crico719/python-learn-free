#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Update course.json to have topic/subtopic structure like Mimo."""
import json

with open('data/course.json') as f:
    course = json.load(f)

# Define topics for each lesson (topic_name, subtopics_list)
# Each subtopic = (title, description, exercise_question, exercise_answer, hint)

topics_update = {
    "1": [
        ("Nombres de variables", "Elige nombres descriptivos para tus variables",
         'name = "Ana"\nprint(name)', 'Use meaningful variable names', 'Follow Python naming rules'),
        ("Valores de variables", "Asigna diferentes tipos de datos",
         'age = 25\nheight = 1.70\nprint(age, height)', 'Assign int, float, string', 'Each variable holds one value'),
        ("Consola", "Usa print() para mostrar valores",
         'print("Hello World")', 'Use print() function', 'Text must be inside quotes'),
    ],
    "2": [
        ("Operaciones con variables", "Suma, resta, multiplica y divide",
         'a = 10\nb = 3\nprint(a + b, a - b, a * b, a / b)', 'Use + - * / operators', 'Operators work like math'),
        ("Reasignación", "Cambia el valor de una variable",
         'x = 5\nx = 10\nprint(x)', 'Just assign a new value', 'Variables can change'),
    ],
    "3": [
        ("Verdadero y falso", "Entiende los valores booleanos",
         'is_active = True\nprint(is_active)', 'Use True or False (capital)', 'Only two possible values'),
        ("Comparaciones booleanas", "Compara valores para obtener True/False",
         'print(5 > 3)\nprint(5 == 5)\nprint(5 != 3)', 'Use >, ==, != operators', 'Comparison returns True or False'),
    ],
    "4": [
        ("Igualdad", "Compara si dos valores son iguales",
         'print(10 == 10)\nprint(10 == 5)', 'Use == for equality', 'Double equals sign'),
        ("Desigualdad", "Compara si valores son diferentes",
         'print(10 != 5)\nprint(10 != 10)', 'Use != for inequality', 'Not equal operator'),
        ("Mayor y menor", "Compara tamaño de valores",
         'print(5 > 3)\nprint(3 < 5)\nprint(5 >= 5)', 'Use >, <, >=, <=', 'Greater than, less than operators'),
    ],
    "5": [
        ("F-strings", "Inserta variables dentro de texto",
         'name = "Ana"\nprint(f"Hello {name}")', 'Use f before the string', 'Curly braces {} hold variables'),
        ("Métodos de texto", "Transforma strings con métodos",
         'text = "hello"\nprint(text.upper())\nprint(text.capitalize())', 'Use .upper(), .lower(), .capitalize()', 'Methods come after dot'),
    ],
    "6": [
        ("Tipos de datos", "Identifica int, float, bool, str",
         'print(type(10))\nprint(type(3.14))\nprint(type(True))\nprint(type("text"))', 'Use type() function', 'Each type is different'),
        ("Conversiones", "Convierte entre tipos de datos",
         'print(int("5"))\nprint(float(3))\nprint(str(10))', 'Use int(), float(), str()', 'Convert between types'),
        ("Consolidación", "Practica todos los conceptos básicos",
         'name = "Ana"\nage = 25\nprint(f"{name} is {age}")', 'Combine all concepts', 'Practice makes perfect'),
    ],
    "7": [
        ("Saludo del bot", "Crea un bot que saluda",
         'name = input("What is your name? ")\nprint(f"Hello, {name}!")', 'Use input() and f-string', 'input() gets user text'),
        ("Interacción básica", "Haz que el bot responda",
         'name = input("Name: ")\nprint(f"Nice to meet you, {name}!")\nprint("I am your Python bot.")', 'Multiple print() calls', 'Build a conversation flow'),
    ],
}

for lid, topics in topics_update.items():
    if lid in course:
        course[lid]["topics"] = []
        for topic_title, topic_desc, ex_q, ex_a, ex_h in topics:
            course[lid]["topics"].append({
                "title": topic_title,
                "description": topic_desc,
                "exercises": [{
                    "question": ex_q,
                    "answer": ex_a,
                    "hint": ex_h
                }]
            })

with open('data/course.json', 'w', encoding='utf-8') as f:
    json.dump(course, f, indent=2, ensure_ascii=False)

print(f"Updated {sum(1 for k in topics_update if k in course)} lessons with topics!")
print(f"Total lessons in course: {len(course)}")
