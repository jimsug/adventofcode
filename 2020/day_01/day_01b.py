#!/usr/bin python

from itertools import combinations

f = open("2020/day_01/input_01a.txt")

input = [int(x) for x in f.read().split('\n')[:-1]]

for i in combinations(input, 3):
    if sum(i) == 2020:
        print("{0} + {1} + {2} = {3};  {0} x {1}  x {2} = {4}".format(i[0], i[1], i[2], sum(i),  i[0]*i[1]*i[2]))