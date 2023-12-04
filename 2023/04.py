from aocd.models import Puzzle
import re
pz = Puzzle(year=2023, day=4)

# p = pz.examples[0].input_data.splitlines()
p = pz.input_data.splitlines()

winnings = []
score = 0

# count the number of wins and (part 1) score them
for line in range(len(p)):
    game, draws = p[line].split(":")
    win, card = draws.split("|")
    wins = [int(c) for c in win.strip().split(" ") if c]
    cards = [int(c) for c in card.strip().split(" ") if c]
    winners = sum([1 for c in cards if c in wins])
    if winners > 0:
        score += 2**(winners-1)

    winnings.append(winners)

counts = [1]*len(winnings) # we get one of each card

# for each card, count the wins, and then add the number of
# that card we have to the following card(s), if any
for w in range(len(winnings)):
    if winnings[w] > 0:
        for i in range(w+1, w + winnings[w] + 1):
            counts[i] += counts[w]

print("Part 1:", score)
print("Part 2:", sum(counts))