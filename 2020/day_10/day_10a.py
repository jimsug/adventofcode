with open("2020/day_10/input.txt") as f:
    input = [int(i) for i in f.read().strip().split("\n")]

input.append(0)
input.append(max(input)+3)
input.sort()

diffArray = [input[i]-input[i-1] for i in range(1, len(input))]
print(diffArray.count(1)*diffArray.count(3))
