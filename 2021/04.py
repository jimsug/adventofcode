from aocd.models import Puzzle
import numpy as np
from numpy import array, where, zeros
p = Puzzle(year=2021, day=4).input_data

numbers = [int(n) for n in p.split('\n\n')[0].split(',')]

class Card:
    rows = array([])
    grid = array([])

    def __init__(self, rows:list):
        self.rows = array(rows)
        self.grid = zeros((5,5), dtype=int)

    def __str__(self):
        return str(self.rows)

    def state(self):
        return str(self.grid)

    def mark_if_present(self, number:int):
        locs = where(self.rows == number)
        if locs:
            x,y = locs
            if x.size > 0 and y.size > 0:
                self.grid[x[0]][y[0]] = 1

        return self

    def win(self)-> bool:
        # check columns
        if any([x == 5 for x in np.sum(self.grid, 0)]):
            return True
        # check rows
        elif any([x == 5 for x in np.sum(self.grid, 1)]):
            return True

        return False

    def score(self, winning:int) -> int:
        unmarked = 0
        for x in range(5):
            for y in range(5):
                if self.grid[y][x] == 0:
                    unmarked += self.rows[y][x]

        return unmarked * winning

cards = [ Card([[int(n) for n in r.split(' ') if n] for r in c.split('\n')]) for c in p.split('\n\n')[1:]]

winner = 0

for n in numbers:
    if winner == 1:
        break

    for c in cards:
        c.mark_if_present(n)
        if c.win():
            winner = 1
            print(c.score(n))
            break

winner = 0
for n in numbers:
    if winner == 1:
        break

    for c in cards:
        c.mark_if_present(n)
        if all( [ c.win() for c in cards ] ):
            winner = 1
            print(c.score(n))
            break
