import copy

with open("2019/input_02.txt") as f:
    input = [int(i) for i in f.read().strip().split(",")]
    backup = copy.deepcopy(input)

nextop = 0
input[1] = 12
input[2] = 2
while nextop <= len(input):
    instruction = input[nextop]
    if instruction == 1:
        input[input[nextop+3]] = input[input[nextop+1]] + input[input[nextop+2]]
    elif instruction == 2:
        input[input[nextop+3]] = input[input[nextop+1]] * input[input[nextop+2]]
    elif instruction == 99:
        break
    else:
        print("error")
    nextop+=4

print("Part 1", input[0])
target = input[0]

i=0
j=0
continuenext = True
while continuenext:
    while continuenext:
        nextop = 0
        input = copy.deepcopy(backup)
        input[1] = i
        input[2] = j
        while nextop <= len(input):
            instruction = input[nextop]
            if instruction == 1:
                input[input[nextop+3]] = input[input[nextop+1]] + input[input[nextop+2]]
            elif instruction == 2:
                input[input[nextop+3]] = input[input[nextop+1]] * input[input[nextop+2]]
            elif instruction == 99:
                break
            else:
                print("error")
            nextop+=4

        if input[0] == target:
            print("Part 2", input[0], 100 * i + j)
            continuenext = False
