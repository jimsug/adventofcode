with open("2020/day_05/input_05.txt") as f:
    input = f.read().strip().split("\n")

maxSeat = 0
minSeat = 999999999999999
seats = []
for i in input:
    seat = [[0,127], [0,7]]
    for c in i:
        if c == 'B':
            seat[0][0] = seat[0][0] + ((seat[0][1] - seat[0][0] + 1) / 2)
        elif c == 'F':
            seat[0][1] = seat[0][1] - ((seat[0][1] - seat[0][0] + 1) / 2)
        elif c == 'L':
            seat[1][1] = seat[1][1] - ((seat[1][1] - seat[1][0] + 1) / 2)
        elif c == 'R':
            seat[1][0] = seat[1][0] + ((seat[1][1] - seat[1][0] + 1) / 2)

    print(seat)
    seatNo = ((seat[0][0] * 8) + seat[1][0])
    if maxSeat < seatNo:
        maxSeat = seatNo
    if minSeat > seatNo:
        minSeat = seatNo

    seats.append(int(seatNo))

print(minSeat, maxSeat)
for x in range(int(minSeat), int(maxSeat)):
    if not (x in seats):
        print(x)
