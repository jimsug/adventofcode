from aocd import data
from aocd.models import Puzzle
from collections import deque
import re

# data = Puzzle(year=2022, day=5).example_data
stacks, instructions = data.split("\n\n")

labels = stacks.split("\n")[-1]
contents = stacks.split("\n")[:-1]
stack = {}
stack2 = {}
for i in range(len(labels)):
    c = labels[i]
    if c.isnumeric():
        stack[c] = deque([ sc[i] for sc in contents if sc[i].strip() ])
        stack2[c] = [ sc[i] for sc in contents if sc[i].strip() ]

print(stack)
patt = "move (\d+) from (\d+) to (\d+)"
for i in instructions.split("\n"):
    count_moves, from_stack, to_stack = re.fullmatch(patt, i).groups()
    count_moves = int(count_moves)
    for j in range(int(count_moves)):
        stack[to_stack].appendleft(stack[from_stack].popleft())

    stack2[to_stack][0:0] = stack2[from_stack][:count_moves]
    stack2[from_stack] = stack2[from_stack][count_moves:]



print("".join([ s[0] for k,s in stack.items()]))
print("".join([ s[0] for k,s in stack2.items()]))