# importing required constants from consts.py
from consts import TWO

def calculatePerimeter(dimensions):
    l = dimensions['l']
    b = dimensions['b']
    return TWO * (l + b)