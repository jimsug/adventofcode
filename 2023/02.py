from aocd import get_data
import re
p = get_data(year=2023, day=2).splitlines()
maximums = {
    "red":12,
    "green":13,
    "blue":14
}

part_one_sums = 0
part_two_powers = []
for l in p:
    possible = True
    mins = {
        "red":0,
        "green":0,
        "blue":0
    }


    games = l.split(":")[-1].replace("; ", ", ")
    game_number = int(l.split(":")[0].split(" ")[-1])

    shown = [c.split(" ") for c in games.strip().split(", ")]
    for s in shown:
        if int(s[0]) > maximums[s[1]]:
            possible = False

        mins[s[1]] = max(mins[s[1]], int(s[0]))

    if possible:
        part_one_sums += game_number

    part_two_powers.append(mins["red"] * mins["green"] * mins["blue"])

print(part_one_sums)
print(sum(part_two_powers))