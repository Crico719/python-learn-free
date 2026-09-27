#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Genera web/index.html autocontenido: HTML+CSS+JS+curso+teoria+quiz"""
import json, os, shutil
import content_a as A, content_b as B, content_c as C

os.chdir(os.path.dirname(os.path.abspath(__file__)))

T, Q = {}, {}
for m in (A, B, C):
    T.update(m.T)
    Q.update(m.Q)

course = json.load(open("data/course.json", encoding="utf-8"))

# Normaliza la forma de las preguntas a [pregunta, [opciones], correcta]
quiz = {}
for k, v in Q.items():
    quiz[k] = [list(x) for x in v]

# Secciones para la barra lateral
secs, cur = [], None
for i in range(1, 91):
    l = course.get(str(i))
    if not l:
        continue
    t = l.get("topics") or []
    title = t[0]["title"] if t else l["title"]
    kind = "p" if l.get("type") == "PROJECT_GUIDED" else "l"
    if cur is None or cur["k"] != kind:
        cur = {"k": kind, "n": title, "ls": []}
        secs.append(cur)
    cur["ls"].append(str(i))

tpl = open("web/tpl.html", encoding="utf-8").read()
out = (tpl
       .replace("__DATA__", json.dumps(course, ensure_ascii=False))
       .replace("__THEORY__", json.dumps(T, ensure_ascii=False))
       .replace("__QUIZ__", json.dumps(quiz, ensure_ascii=False))
       .replace("__SECS__", json.dumps(secs, ensure_ascii=False)))

for ph in ("__DATA__", "__THEORY__", "__QUIZ__", "__SECS__"):
    assert ph not in out, "placeholder sin reemplazar: " + ph

open("web/index.html", "w", encoding="utf-8").write(out)
shutil.copy("web/index.html", "index.html")

nq = sum(len(v) for v in quiz.values())
print("OK  web/index.html  %d bytes" % len(out.encode("utf-8")))
print("    lecciones=%d  teorias=%d  quizzes=%d  preguntas=%d  secciones=%d"
      % (len(course), len(T), len(quiz), nq, len(secs)))
