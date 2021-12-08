from aocd.models import Puzzle
import itertools

import numpy
p = Puzzle(year=2021, day=5).input_data
# p = "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2"

class Point:
    x: int = 0
    y: int = 0

    def __init__(self, coords:list):
        self.x, self.y = coords

    def __str__(self):
        return f"Point: ({self.x}, {self.y})"


class Line:
    start: Point = None
    end: Point = None

    def __init__(self, points:list):
        self.start, self.end = points

    def __str__(self):
        return f"Line: {self.start} -> {self.end}"

    def x(self):
        return [self.start.x, self.end.x]

    def y(self):
        return [self.start.y, self.end.y]

input = [ Line([ Point([int(k) for k in j.strip().split(",")]) for j in i.split("->")]) for i in p.split("\n")]
part1 = [ l for l in input if (l.start.x == l.end.x or l.start.y == l.end.y) ]

def ambirange(a, b):
    if b >= a:
        return range(a, b + 1, 1)
    else:
        return reversed(range(b, a + 1, 1))

def markgrid(lines:list) -> numpy.ndarray:
    x = [i.start.x for i in lines]
    x.extend([i.end.x for i in lines])
    y = [i.start.y for i in lines]
    y.extend([i.end.y for i in lines])
    grid = numpy.zeros(shape=(max(x) + 2, max(y) + 2), dtype=int)

    for line in lines:
        dx = abs(line.start.x - line.end.x)
        dy = abs(line.start.y - line.end.y)
        xp = 0 if line.start.x == line.end.x else (1 if line.start.x < line.end.x else -1)
        yp = 0 if line.start.y == line.end.y else (1 if line.start.y < line.end.y else -1)

        for i in range(0, 1 + (dx if yp == 0 else dy)):
            grid[line.start.y + (i * yp)][line.start.x + (i * xp)] += 1


    return grid

grid = markgrid(part1)
print(grid)
unique, counts = numpy.unique(grid, return_counts=True)
print(dict(zip(unique, counts)))
multiple = sum([counts[x] for x in unique if x > 1])
print(multiple)

grid2 = markgrid(input)
unique2, counts2 = numpy.unique(grid2, return_counts=True)
print(dict(zip(unique2, counts2)))
multiple2 = sum([counts2[x] for x in unique2 if x > 1])
print(multiple2)
