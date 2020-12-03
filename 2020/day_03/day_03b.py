opts = [[1,1], [3,1], [5,1], [7,1], [1,2]]
o = 1
with open("2020/day_03/input_03.txt") as f:
    input = [[c for c in i] for i in f.read().strip().split("\n")]
    for m in opts:
        x = 1
        y = 1
        z = 0
        while (y + m[1] - 1) <= len(input):
            if input[y-1][(x - 1 ) % 31 ] == "#":
                z+=1

            x+=m[0]
            y+=m[1]


        o*=z

print(o)
