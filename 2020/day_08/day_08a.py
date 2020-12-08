with open("2020/day_08/input_08.txt") as f:
    input = [[i.split(" ")[0], int(i.split(" ")[1])] for i in f]

instructions = {}

for c in range(len(input)):
    instructions[c] = input[c]

def find_score(instructions):
    score = 0
    nexti = 0
    for i in range(len(instructions)):
        try:
            step = instructions.pop(nexti)
        except KeyError:
            return score
        operation = step[0]
        arg = step[1]
        if operation in ['nop', 'acc']:
            nexti += 1
        if operation == 'acc':
            score += arg
        if operation == 'jmp':
            nexti += arg

    return False

print(find_score(instructions))
