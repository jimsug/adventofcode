import re

with open("2020/day_07/input_07.txt") as x:
    input = {f[0]:{g[1]:int(g[0]) for g in re.findall(r"(\d+) (.+?) bags?,?\.? ?", f[1])} for f in [g.split(" bags contain") for g in x.read().strip().split("\n")]}

def countRecurse(bag, item):
    return sum([k * countRecurse(bag, j) if k else 0 for j, k in bag[item].items()]) + 1

def countRecursively(bag, item):
    return countRecurse(bag, item) - 1

print(countRecursively(input, 'shiny gold'))
