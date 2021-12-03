from aocd.models import Puzzle
p = Puzzle(year=2021, day=2)
input = [l.strip().split(" ") for l in p.input_data.split("\n")]

pos = 0
aim = 0
dep = 0

for l in input:
    if l[0] == 'forward':
        pos += int(l[1])
        dep += aim*int(l[1])
    elif l[0] == 'down':
        aim += int(l[1])
    elif l[0] == 'up':
        aim -= int(l[1])

print(pos, aim, pos * aim)
print(pos, dep, pos * dep)
