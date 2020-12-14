demo = False
import operator as op
from sympy.ntheory.modular import crt
with open("2020/day_13/demo.txt" if demo else "2020/day_13/input.txt") as f:
  input = f.read().strip().split("\n")

minTs = int(input[0])

buses = list(set(input[1].split(",")))
buses.remove("x")
buses = [int(x) for x in buses]
buses.sort()
earliest = {}

for x in buses:
    i = 0
    while i < minTs:
      i+=x

    earliest[x] = i

earliestbus = [key for key in earliest if all(earliest[temp] >= earliest[key] for temp in earliest)][0]
earliesttime = earliest[earliestbus]
print("Part 1:", (earliesttime - minTs) * earliestbus)

ln2 = input[1]

times, buses = zip(*((i, int(bus)) for i, bus in enumerate(ln2.split(',')) if bus != 'x'))

print("Part 2:", crt(buses, map(op.neg, times))[0])
