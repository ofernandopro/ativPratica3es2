import math
import os

def add(a, b) -> int:
    return a + b

def sub(a, b) -> int:
    return a - b

def mult(a, b) -> int:
    return a * b

def div(a, b) -> int:
    return a / b

def getAreaTrapezio(l1, l2, h) -> float:
    soma = add(l1, l2)
    mult = mult(soma, h)
    area = div(mult, 2)
    return area

def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'

