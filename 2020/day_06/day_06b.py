with open("2020/day_06/input_06.txt") as f:
    input = [a.split("\n") for a in f.read().strip().split("\n\n")]

totalLen = 0
for a in input:
    thisList = a[0]
    for b in a:
        thisList = [value for value in thisList if value in b]

    totalLen += len(thisList)

print(totalLen)
