from statistics import median, mean
from aocd.models import Puzzle
p = Puzzle(year=2021, day=7).input_data

input = [ int(i) for i in p.split(',') ]

med = median(input)

fuel_needed = sum([abs(med - i) for i in input])
def fuel_use(n):
    use = 0
    for i in range(1, n + 1):
        use += i
    return use

# the median is the closest point to all points, right?
print(fuel_needed)

# brute force way of doing this, but it works
print(min([sum([fuel_use(abs(x - n)) for n in input]) for x in range( min(input), max(input) + 1)]))
