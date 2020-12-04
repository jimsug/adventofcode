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
        for b in c:
            for a in b:
                if a[0] in thisFields:
                    thisFields.remove(a[0])
        if len(thisFields) == 0:
            validCount += 1

print("valid passport(s): {}".format(validCount))
