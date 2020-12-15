#!/usr/bin/python3

input = [19,0,5,1,10,13]
targets = [2020, 3*(10**7)]
for a in range(len(targets)):

    seen = [-1]*targets[a]
    mem = [-1]*targets[a]
    for i in range(len(input)):
        seen[input[i]] = i
        mem[i] = input[i]

    i = len(input) - 1

    for j in range(i, targets[a]-1):
        mem[j+1] = j - seen[mem[j]] if seen[mem[j]] >= 0 else 0
        seen[mem[j]] = j

    print("Part {} ({}th item):".format(a+1, len(mem)), mem[-1])
