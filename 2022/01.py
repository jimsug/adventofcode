from aocd.models import Puzzle
p = Puzzle(year=2022, day=1).input_data

for i in p.split("\n\n"):
    totals = [sum([int(n) for n in i.split("\n")]) for i in p.split("\n\n")]

totals.sort()

print(f'Part 1: {totals[-1]}')

print(f'Part 2: {sum(totals[-3:])}')