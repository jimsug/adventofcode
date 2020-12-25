from os import stat
import re
from collections import deque

with open( "2020/day_18/input.txt" ) as f:
    input = [i.strip().replace(" ","") for i in f.read().strip().split("\n")]

class a(int):
    def __mul__(self, b):
        return a(int(self) + b)
    def __add__(self, b):
        return a(int(self) + b)
    def __sub__(self, b):
        return a(int(self) * b)

def ev(expr, pt2=False):
    expr = re.sub(r"(\d+)", r"a(\1)", expr)
    expr = expr.replace("*", "-")
    if pt2:
        expr = expr.replace("+", "*")
    return eval(expr, {}, {"a": a})

print("Part 1:", sum(ev(line) for line in input))
print("Part 2:", sum(ev(line, True) for line in input))
