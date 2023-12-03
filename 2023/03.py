from aocd.models import Puzzle
import re
pz = Puzzle(year=2023, day=3)

# p = pz.examples[0].input_data.splitlines()
p = pz.input_data.splitlines()
p = [[c for c in line] for line in p]

p.insert(0, ['.']*len(p[0]))
p.append(['.']*len(p[0]))

for l in p:
    l.append('.')
    l.insert(0, '.')

isNum = False
isPart = False
isGearPart = False
total = 0
gearTotal = 0
gearLocs = {}
# gearLoc = []
num = ''
for r in range(1, len(p) - 1):
    if num.isnumeric() and isPart:
        total+=int(num)
        if len(gearLoc) > 0:
            for gLoc in list(set(gearLoc)):
                if gLoc in gearLocs:
                    gearLocs[gLoc].append(int(num))
                else:
                    gearLocs[gLoc] = [int(num)]

    num = ''
    gearLoc = []
    isPart = False
    for c in range(1, len(p[r]) - 1):
        if not p[r][c].isdigit():
            if num.isnumeric() and isPart:
                total+=int(num)
                if len(gearLoc) > 0:
                    for gLoc in list(set(gearLoc)):
                        if gLoc in gearLocs:
                            gearLocs[gLoc].append(int(num))
                        else:
                            gearLocs[gLoc] = [int(num)]

            num = ''
            gearLoc = []
            isPart = False
        else:
            num += p[r][c]

        if num:
            for dx in range( -1, 2):
                for dy in range( -1, 2):
                    if p[r + dx][c + dy] not in '1234567890.':
                        isPart = True
                        if p[r + dx][c + dy] == '*':
                            gearLoc.append(str(r+dx) + ":" + str(c+dy))

for k,v in gearLocs.items():
    if len(v) == 2:
        gearTotal+=v[0]*v[1]

print(total)
print(gearTotal)