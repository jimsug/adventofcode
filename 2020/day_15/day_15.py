#!/usr/bin/python3

input = [19,0,5,1,10,13]
targets = [2020, 3*(10**7)]
for a in range(len(targets)):
    seen = {}
    for i in range(len(input)):
        seen[input[i]] = i

    i = len(input) - 1

    thisloop = input.copy()
    while i < targets[a]-1:
        try:
            nextn = i - seen[thisloop[i]]
        except KeyError:
            nextn = 0

        seen[thisloop[i]] = i

        thisloop.append(nextn)
        i+=1

    print("Part {} ({}th item):".format(a+1, len(thisloop)), thisloop[-1])
