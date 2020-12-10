with open("2020/day_10/input.txt") as f:
    input = [int(i) for i in f.read().strip().split("\n")]

input.sort()

joltage = 0
i = 0

diffArray = [input[i]-input[i-1] for i in range(1, len(input))]
diffArray.append(3)
diffArray.append(min(input)-0)

diffArray.sort()
print(diffArray.count(1)*diffArray.count(3))
