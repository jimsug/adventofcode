import re

with open("2020/day_02/input_02a.txt") as f:
    i = f.read().strip().split("\n")

def find_valid_passwords_v2(input):
    o = 0
    for x in input:
        y = re.split(r'[ \-:]', x)
        if (y[2] == y[4][int(y[0])-1]) ^ (y[2] == y[4][int(y[1])-1]):
            o += 1

    return o
print(find_valid_passwords_v2(i))
