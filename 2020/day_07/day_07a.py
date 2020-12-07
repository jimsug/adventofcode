import re

with open("2020/day_07/input_07.txt") as x:
    input = [g.split(" bags contain") for g in x.read().strip().split("\n")]

find_stack = ['shiny gold']
count_bags = 0
found_stack = []
while True:
    search_bag = find_stack.pop()
    for i in input:
        if search_bag in i[1]:
            count_bags+=1
            find_stack.append(i[0])
            found_stack.append(i[0])

    if len(find_stack) == 0:
        break

print(len(set(found_stack)))
