
with open("2019/input_01.txt") as f:
    input = [int(i) for i in f.read().strip().split("\n")]

def calcFuel(mod):
    return int(mod/3)-2

print("Part 1", sum([calcFuel(i) for i in input]))

def calcFuelV2(mod):
    fuel = int(mod/3)-2
    if fuel > 0:
        return fuel + calcFuelV2(fuel)
    else:
        return 0

print("Part 2", sum([calcFuelV2(i) for i in input]))
