import numpy, copy
demo = False
with open( "2020/day_17/demo.txt" if demo else "2020/day_17/input.txt" ) as f:
    input = [[1 if c == '#' else 0 for c in d] for d in f.read().strip().split('\n')]

lim = 6
field = numpy.zeros((1+(2*lim),len(input[0])+(2*lim),len(input)+(2*lim)), dtype=int)

for y in range(len(input)):
    for z in range(len(input[y])):
        field[lim][y+lim][z+lim] = input[y][z]

lastStep = copy.deepcopy(field)
i = 0
aOffs = (-1, 0, 1)
while i < lim:

    nextStep = copy.deepcopy(lastStep)
    for x in range(len(lastStep)):
        for y in range(len(lastStep[0])):
            for z in range(len(lastStep[0][0])):

                score = 0
                for xOff in aOffs:
                    for yOff in aOffs:
                        for zOff in aOffs:
                            if xOff == yOff == zOff == 0:
                                continue
                            elif 0 <= x+xOff < len(lastStep) and 0 <= y+yOff < len(lastStep[0]) and 0 <= z+zOff < len(lastStep[0][0]):
                                score+= lastStep[x+xOff][y+yOff][z+zOff]
                if lastStep[x][y][z] == 1 and score in [2, 3]:
                    nextStep[x][y][z] = 1
                elif lastStep[x][y][z] == 0 and score == 3:
                    nextStep[x][y][z] = 1
                else:
                    nextStep[x][y][z] = 0

    lastStep = copy.deepcopy(nextStep)
    i+=1

print("Part 1:", sum([sum([sum([z for z in y]) for y in x]) for x in nextStep]))

nfield = numpy.zeros(shape=(1+(2*lim),len(input[0])+(2*lim),len(input)+(2*lim),1+(2*lim)), dtype=int)


for y in range(len(input)):
    for z in range(len(input[y])):
        nfield[lim][y+lim][z+lim][lim] = input[y][z]

lastStep = copy.deepcopy(nfield)
i = 0
while i < lim:

    nextStep = copy.deepcopy(lastStep)
    for x in range(len(lastStep)):
        for y in range(len(lastStep[0])):
            for z in range(len(lastStep[0][0])):
                for w in range(len(lastStep[0][0][0])):
                    score = 0
                    for xOff in aOffs:
                        for yOff in aOffs:
                            for zOff in aOffs:
                                for wOff in aOffs:
                                    if xOff == yOff == zOff == wOff == 0:
                                        continue
                                    elif 0 <= x+xOff < len(lastStep) and 0 <= y+yOff < len(lastStep[0]) and 0 <= z+zOff < len(lastStep[0][0]) and 0 <= w+wOff < len(lastStep[0][0][0]):
                                        score+= lastStep[x+xOff][y+yOff][z+zOff][w+wOff]

                    if lastStep[x][y][z][w] == 1 and score in [2, 3]:
                        nextStep[x][y][z][w] = 1
                    elif lastStep[x][y][z][w] == 0 and score == 3:
                        nextStep[x][y][z][w] = 1
                    else:
                        nextStep[x][y][z][w] = 0
    lastStep = copy.deepcopy(nextStep)
    i+=1

print("Part 2:", sum([sum([sum([sum([w for w in z]) for z in y]) for y in x]) for x in nextStep]))
