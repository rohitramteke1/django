# from django.test import TestCase

# Create your tests here.
from .texttohtml import formatHtml
with open("text.txt","r") as f:
            lines=f.read()

print(lines)

print(formatHtml("Asit is my name Explain <h1>24</h1>"))