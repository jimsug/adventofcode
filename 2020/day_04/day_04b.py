import copy
from itertools import chain
fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
]

validCount = 0

with open("2020/day_04/input_04.txt") as f:
    input = [[[z.split(":") for z in y.split(" ")] for y in list(chain(x.split("\n")))] for x in f.read().strip().split("\n\n")]
    for c in input:
        thisFields = copy.deepcopy(fields)
        thisFields.remove('cid')
        thisValidField = True
        for b in c:
            for a in b:
                if a[0] in thisFields:
                    thisFields.remove(a[0])
                    if a[0] == 'byr':
                        if int(a[1]) <1920 or int(a[1]) > 2002:
                            thisValidField = False
                    elif a[0] == 'iyr':
                        if int(a[1]) <2010 or int(a[1]) > 2020:
                            thisValidField = False
                    elif a[0] == 'eyr':
                        if int(a[1]) <2020 or int(a[1]) > 2030:
                            thisValidField = False
                    elif a[0] == 'hcl':
                        if a[1][0] != '#':
                            thisValidField = False
                        for c in a[1][1:]:
                            if not (c in 'abcdef1234567890'):
                                thisValidField = False
                    elif a[0] == 'ecl':
                        if not (a[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                            thisValidField = False
                    elif a[0] == 'pid':
                        if len(a[1]) != 9 or int(9) < 0:
                            thisValidField = False
                    elif a[0] == 'hgt':
                        if (a[1][-2:] == 'cm' and (int(a[1][:-2]) < 150 or int(a[1][:-2]) > 193)) or (a[1][-2:] == 'in' and (int(a[1][:-2]) < 59 or int(a[1][:-2]) > 76)) or (not (a[1][-2:] in ['in', 'cm'])):
                            thisValidField = False
        if len(thisFields) == 0 and thisValidField:
            validCount += 1

print("valid passport(s): {}".format(validCount))
