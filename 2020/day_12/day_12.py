with open("2020/day_12/input.txt") as f:
# with open("2020/day_12/demo.txt") as f:
  input = f.read().strip().split('\n')

dir = 0

pos = [0, 0] # x, y

for instruction in input:
  verb = instruction[0]
  arg = int(instruction[1:])
  if verb in "LR":
    rot = arg/90
    dir = (dir + ( rot * (1 if verb == "R" else -1) )) % 4
  elif verb in "NS":
    pos[1] += (arg * (-1 if verb == "N" else 1))
  elif verb in "WE":
    pos[0] += (arg * (-1 if verb == "W" else 1))
  elif dir == 0:
    pos[0] += arg

  elif dir == 2:
    pos[0] -= arg

  elif dir == 1:
    pos[1] += arg

  elif dir == 3:
    pos[1] -= arg

print("Part 1: ", sum([abs(x) for x in pos]), pos)

pos = [0, 0]
waypoint = [10, -1]

for instruction in input:
  verb = instruction[0]
  arg = int(instruction[1:])
  if verb in "LR":
    rot = (arg/90) % 4
    if verb == "L" and rot == 1:
      rot = 3
    elif verb == "L" and rot == 3:
      rot = 1

    print(rot)

    if rot == 1:
      waypoint = [-waypoint[1], waypoint[0]]
    elif rot == 2:
      waypoint = [-waypoint[0], -waypoint[1]]
    elif rot == 3:
      waypoint = [waypoint[1], -waypoint[0]]

  elif verb in "NS":
    waypoint[1] += (arg * (-1 if verb == "N" else 1))
  elif verb in "WE":
    waypoint[0] += (arg * (-1 if verb == "W" else 1))
  else:
    pos[0]= pos[0] + (waypoint[0]*arg)
    pos[1]= pos[1] + (waypoint[1]*arg)

  print(instruction, waypoint, pos)

print("Part 2: ", sum([abs(x) for x in pos]), pos)
