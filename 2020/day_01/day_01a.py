#!/usr/bin python

from itertools import combinations

f = open("2020/day_01/input_01a.txt")

input = [int(x) for x in f.read().split('\n')[:-1]]

for i in combinations(input, 2):
    if i[0] + i[1] == 2020:
        print("{0} + {1} = {2}; {0} x {1} = {3}".format(i[0], i[1], i[0] + i[1], i[0] * i[1] ))
