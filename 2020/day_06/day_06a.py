with open("2020/day_06/input_06.txt") as f:
    input = sum([len(set(set(c for c in a.replace("\n","")))) for a in f.read().strip().split("\n\n")])

print(input)
