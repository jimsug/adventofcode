import copy
# with open("2020/day_11/demo.txt") as f:
with open("2020/day_11/input.txt") as f:
    input = [[c for c in d] for d in f.read().strip().split("\n")]

nextit = True
seats = copy.deepcopy(input)
while nextit:
    newseats = copy.deepcopy(seats)
    unchanged = True
    for row in range(len(seats)):
        height = len(seats) - 1
        for col in range(len(seats[row])):
            if seats[row][col] in "#L":
                width = len(seats[row]) - 1
                n  = 1 if (row > 0 )and seats[row-1][col] == "#" else 0
                ne = 1 if (row > 0 )and (col < width )and seats[row-1][col+1] == "#" else 0
                e  = 1 if (col < width )and seats[row][col+1] == "#" else 0
                se = 1 if (row < height )and (col < width )and seats[row+1][col+1] == "#" else 0
                s  = 1 if (row < height )and seats[row+1][col] == "#" else 0
                sw = 1 if (col > 0 )and (row < height )and seats[row+1][col-1] == "#" else 0
                w  = 1 if (col > 0 )and seats[row][col-1] == "#" else 0
                nw = 1 if (row > 0 )and (col > 0 )and seats[row-1][col-1] == "#" else 0

                score = sum([n, ne, e, se, s, sw, w, nw])
                if seats[row][col] == "#" and score >= 4:
                    newseats[row][col] = "L"
                    unchanged = False
                elif seats[row][col] == "L" and score == 0:
                    newseats[row][col] = "#"
                    unchanged = False

    if unchanged:
        nextit = False

    seats = copy.deepcopy(newseats)

print("Part 1:", sum ([row.count("#") for row in seats]))
print("")

nextit = True
seats = input.copy()
while nextit:
    newseats = copy.deepcopy(seats)
    unchanged = True
    for row in range(len(seats)):
        height = len(seats) - 1
        for col in range(len(seats[row])):
            n, ne, e, se, s, sw, w, nw = 0, 0, 0, 0, 0, 0, 0, 0
            x = 1
            nextView = True
            while row - x >= 0 and nextView == True:
                if seats[row-x][col] in 'L#':
                    nextView = False
                    if seats[row-x][col] == '#':
                        n = 1
                x += 1
            x = 1
            nextView = True
            while row - x >= 0 and col + x <= width and nextView == True:
                if seats[row-x][col+x] in 'L#':
                    nextView = False
                    if seats[row-x][col+x] == '#':
                        ne = 1
                x += 1
            x = 1
            nextView = True
            while col + x <= width and nextView == True:
                if seats[row][col+x] in 'L#':
                    nextView = False
                    if seats[row][col+x] == '#':
                        e = 1
                x += 1
            x = 1
            nextView = True
            while row + x <= height and col + x <= width and nextView == True:
                if seats[row+x][col+x] in 'L#':
                    nextView = False
                    if seats[row+x][col+x] == '#':
                        se = 1
                x += 1
            x = 1
            nextView = True
            while row + x <= height and nextView == True:
                if seats[row+x][col] in 'L#':
                    nextView = False
                    if seats[row+x][col] == '#':
                        s = 1
                x += 1
            x = 1
            nextView = True
            while row + x <= height and col - x >= 0 and nextView == True:
                if seats[row+x][col-x] in 'L#':
                    nextView = False
                    if seats[row+x][col-x] == '#':
                        sw = 1
                x += 1
            x = 1
            nextView = True
            while col - x >= 0 and nextView == True:
                if seats[row][col-x] in 'L#':
                    nextView = False
                    if seats[row][col-x] == '#':
                        w = 1
                x += 1
            x = 1
            nextView = True
            while row - x >= 0 and col - x >= 0 and nextView == True:
                if seats[row-x][col-x] in 'L#':
                    nextView = False
                    if seats[row-x][col-x] == '#':
                        nw = 1
                x += 1

            score = sum([n, ne, e, se, s, sw, w, nw])
            if seats[row][col] == "#" and score >= 5:
                newseats[row][col] = "L"
                unchanged = False
            elif seats[row][col] == "L" and score == 0:
                newseats[row][col] = "#"
                unchanged = False

    if unchanged:
        nextit = False

    seats = copy.deepcopy(newseats)
print("")
print("Part 2:", sum ([row.count("#") for row in seats]))
