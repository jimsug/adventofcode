from aocd.models import Puzzle

p = Puzzle(year=2021, day=3)

input = [ x[0] for x in [l.strip().split(" ") for l in p.input_data.split("\n")]]

calcs = [0] * len(input[0])
for i in input:
    for x in range(len(input[0])):
        calcs[x] += 1 if int(i[x]) == 1 else -1

oxygen = [x for x in input]
scrubber = [x for x in input]


for x in range(len(input[0])):
    if len(oxygen) > 1:
        oxygen = [y for y in oxygen if y[x] == str(1 if sum([1 if y == '1' else -1 for y in [z[x] for z in oxygen] ]) >= 0 else 0)]
    if len(scrubber) > 1:
        scrubber = [y for y in scrubber if y[x] == str(0 if sum([1 if y == '1' else -1 for y in [z[x] for z in scrubber] ]) >= 0 else 1)]


gamma = int(''.join('1' if x < 0 else '0' for x in calcs), 2)
epsilon = int(''.join('1' if x > 0 else '0' for x in calcs), 2)

print(gamma, epsilon, gamma * epsilon)
print(int(str(oxygen[0]), 2), int(str(scrubber[0]), 2), int(str(oxygen[0]), 2) * int(str(scrubber[0]), 2))
