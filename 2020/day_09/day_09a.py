import itertools
with open("2020/day_09/input_09.txt") as f:
    input = [int(i) for i in f.read().strip().split("\n")]


for x in range(25, len(input)):
    if not (input[x] in [sum(i) for i in itertools.combinations(input[x-25:x], 2)]):
        print(input[x])
        break
