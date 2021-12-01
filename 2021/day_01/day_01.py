# figure out how quickly the depth increases
# count the number of times a depth increases from the previous measurement

from re import L


with open("./day_01/input_1.txt") as f:
    input = [int(l.strip()) for l in f.readlines()]

increases = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        increases += 1

print(increases)

wincreases = 0
for i in range(3, len(input)):
    if sum(input[i-3:i]) > sum(input[i-4:i-1]):
        wincreases += 1

print(wincreases)
