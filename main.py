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
    result = mult(soma, h)
    area = div(result, 2)
    return area

def getCapitalizedWithPoint(s) -> str:
    s = s.capitalize()
    if s.endswith('.'):  
        return s
    else:
        return s + '.'

