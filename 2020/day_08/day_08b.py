import copy

with open("2020/day_08/input_08.txt") as f:
    input = [[i.split(" ")[0], int(i.split(" ")[1])] for i in f]

instructions = {}

for c in range(len(input)):
    instructions[c] = input[c]

jmpnop = []
nopjmp = []

for j, k in instructions.items():
    if k[0] == 'jmp':
        jmpnop.append(j)
    if k[0] == 'nop':
        nopjmp.append(j)


def check_fix(instructions, line, mode):
    score = 0
    nexti = 0
    target = len(instructions) - 1
    for i in range(len(instructions)):
        if nexti == target:
            debugged = True
        else:
            debugged = False
        try:
            step = instructions.pop(nexti)
        except KeyError:
            return False
        operation = step[0]
        arg = step[1]
        if operation == 'nop':
            if mode == 0 and nexti == line:
                nexti += arg
            else:
                nexti += 1
        if operation == 'acc':
            nexti += 1
            score += arg
        if operation == 'jmp':
            if mode == 1 and nexti == line:
                nexti += 1
            else:
                nexti += arg

        if debugged:
            return score

    return False

def find_bug(instructions, bugs):
    for i in range(len(bugs)):
        for j in bugs[i]:
            debugged = check_fix(copy.deepcopy(instructions), j, i)
            if debugged:
                return debugged

print(find_bug(instructions, [nopjmp, jmpnop]))
