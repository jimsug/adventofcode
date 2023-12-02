from aocd.models import Puzzle
import re
p = Puzzle(year=2023, day=1).input_data.split("\n")

convs = {
    "one":"one1one",
    "two":"two2two",
    "three":"three3three",
    "four":"four4four",
    "five":"five5five",
    "six":"six6six",
    "seven":"seven7seven",
    "eight":"eight8eight",
    "nine":"nine9nine"
}

print("part one:", sum(10*a[0] + a[-1] for a in [[int(d) for d in i if d.isdigit()] for i in p]))

nums = []
for j in p:
    i = j
    for b, a in convs.items():
        i = i.replace(b, a)

    nums.append([int(c) for c in i if c.isdigit()])

print("part two:", sum([10*a[0] + a[-1] for a in nums]))