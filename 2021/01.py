# figure out how quickly the depth increases
# count the number of times a depth increases from the previous measurement
from aocd.models import Puzzle
p = Puzzle(year=2021, day=1)
input = [int(l.strip()) for l in p.input_data.split("\n")]

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

# single line? I *guess*
print(sum([1 if input[i] > input[i-1] else 0 for i in range(1, len(input))]), sum([1 if sum(input[i-3:i]) > sum(input[i-4:i-1]) else 0 for i in range(3, len(input))]))
