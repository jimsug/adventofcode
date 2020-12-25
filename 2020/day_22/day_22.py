import copy
demo = False
with open("2020/day_22/demo.txt" if demo else "2020/day_22/input.txt") as f:
    input = f.read().strip().split("\n\n")

p1 = [int(i) for i in input[0][1:].strip().split("\n")[1:]]
p2 = [int(i) for i in input[1][1:].strip().split("\n")[1:]]

while all([p1, p2]):
    cards = [p1.pop(0), p2.pop(0)]
    if cards[0] > cards[1]:
        p1+= cards
    else:
        p2+= [cards[1], cards[0]]

if p1:
    wset = p1.copy()
else:
    wset = p2.copy()

wset.reverse()
score = 0
for i in range(len(wset)):
    score+=(i+1)*wset[i]

print(wset)
print("Part 1:", score)

p = [ [int(i) for i in input[0][1:].strip().split("\n")[1:]], [int(i) for i in input[1][1:].strip().split("\n")[1:]]]

def hashDeck(cards) -> int:
    score = 0
    for i in range(len(cards)):
        score+=(i+1)*cards[i]
    return score

def playGame(decks):
    rounds = []
    print('a', rounds)
    while all(decks):
        print('b', decks)
        deckHash = sum([hashDeck(d) for d in decks])
        if deckHash in rounds:
            return [0, decks]
        else:
            rounds.append(deckHash)
            d1, d2 = decks[0], decks[1]
            c1, c2 = d1.pop(0), d2.pop(0)
            print(c1, c2, d1, d2, len(d1), len(d2))
            if (c1 > len(d1)) or (c2 > len(d2)):
                if c1 > c2:
                    winner = [0, [c1, c2]]
                else:
                    winner = [1, [c2, c1]]
            else:
                winner = playGame([copy.deepcopy(d1[:c1]), copy.deepcopy(d2[:c2])])

        if winner[0] == 0:
            d1 += [c1, c2]
        else:
            d2 += [c2, c1]
        decks = [d1, d2]
        print('c', decks)
    print('d', decks)
    return [0 if decks[0] else 1, decks]

print('e', p)
win = playGame(copy.deepcopy(p))
p1 = win[1][win[0]]
p1.reverse()
print('f', p1, len(p1))
print(sum([len(x) for x in p]))
print("Part 2:", hashDeck(p1))
