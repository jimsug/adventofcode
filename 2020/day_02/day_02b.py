import re

with open("2020/day_02/input_02a.txt") as f:
    i = f.read().strip().split("\n")
    o = 0
    for x in i:
        y = re.split('[ \-:]', x)
        if (y[2] == y[4][int(y[0])-1]) ^ (y[2] == y[4][int(y[1])-1]):
            o += 1

print(o)
