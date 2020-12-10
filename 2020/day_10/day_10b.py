with open("2020/day_10/input.txt") as f:
    input = [int(i) for i in f.read().strip().split("\n")]

input.sort()

steps = [0] * (input[-1]+1)

steps[0] = 1
print(steps)
for n in input:
    steps[n] = steps[n-3] + steps[n-2] + steps[n-1]
    print(steps[n], steps)

print(steps[-1])