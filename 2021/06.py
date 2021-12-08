from aocd.models import Puzzle
p = Puzzle(year=2021, day=6).input_data
# p = "3,4,3,1,2"
initial_state = [ int(i) for i in p.split(",") ]

fish_age = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for fish in initial_state:
    fish_age[fish] += 1

for i in range(80):
    fish_age.append(fish_age.pop(0))
    fish_age[6] += fish_age[8]

print(sum(fish_age))

for i in range(176):
    fish_age.append(fish_age.pop(0))
    fish_age[6] += fish_age[8]

print(sum(fish_age))
