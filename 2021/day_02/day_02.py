from aocd.models import Puzzle
p = Puzzle(year=2021, day=2)
input = [l.strip().split(" ") for l in p.input_data.split("\n")]

pos = 0
dep = 0
aim = 0
dep2 = 0

for l in input:
    if l[0] == 'forward':
        pos += int(l[1])
        dep2 += aim*int(l[1])
    elif l[0] == 'down':
        dep += int(l[1])
        aim += int(l[1])
    elif l[0] == 'up':
        dep -= int(l[1])
        aim -= int(l[1])

print(pos, dep, pos * dep)
print(pos, dep2, pos * dep2)
