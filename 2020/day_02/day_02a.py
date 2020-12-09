import re

with open("2020/day_02/input_02a.txt") as f:
    i = f.read().strip().split("\n")

def count_valid_passwords(input):
    o = 0
    for x in input:
        y = re.split(r'[ \-:]', x)
        z = len(re.findall(y[2], y[4]))
        if (z >= int(y[0])) and (z <= int(y[1])):
            o += 1

    return o

print(count_valid_passwords(i))
