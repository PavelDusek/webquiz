# coding: utf-8
import re

from jinja2 import Template

questions = []
question = {
    "section": "Section 1",
    "number": "1",
    "text": "The planet we live on is named:",
    "a": "Earth",
    "b": "Pluto",
    "c": "Venus",
    "d": "Aldebaran",
    "solution": "a",
}
questions.append(question)

with open("quiz.html.jinja") as f:
    html = f.read()
template = Template(html)
with open("quiz.html", "w") as f:
    f.write(template.render(questions = questions))

