from aocd import get_data
import re
p = get_data().splitlines()
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


    games = l.split(":")[-1].split(";")
    game_number = int(l.split(":")[0].split(" ")[-1])

    for game in games:
        shown = [c.split(" ") for c in game.strip().split(", ")]
        # print(game_number, shown)
        for s in shown:
            if int(s[0]) > maximums[s[1]]:
                possible = False

            mins[s[1]] = max(mins[s[1]], int(s[0]))

    if possible:
        part_one_sums += game_number

    part_two_powers.append(mins["red"] * mins["green"] * mins["blue"])
    # print(part_two_powers[-1], [int(v) for v in mins.values()], l)



# print(part_one_sums)
# print(part_two_powers)
print(sum(part_two_powers))