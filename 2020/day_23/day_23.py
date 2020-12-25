input = "198753462"
demoinput = "389125467"
demo = True
cups = [int(c) for c in (demoinput if demo else input)]

def move(cups):
    current = cups[0]
    extract = cups[1:4]
    for cup in extract:
        cups.remove(cup)
    destination = current-1
    while destination in extract:
        destination -= 1
    if destination < min(cups):
        destination = max(cups)

    target = cups.index(destination) + 1
    cups = cups[:target] + extract + cups[target:]
    cups = cups[1:] + [cups[0]]
    return cups

for i in range(10 if demo else 100):
    cups =  move(cups)


if cups.index(1) > 0:
    start = cups.index(1)
    cups = [cups[start]] + cups[start+1:] + cups[:start]

print(''.join([str(c) for c in cups[1:]]))

cups = [int(c) for c in (demoinput if demo else input)]

for i in range(len(cups)+1, 1000001):
    cups.append(i)

for i in range(10000000):
    cups = move(cups)

if cups.index(1) > 0:
    start = cups.index(1)
    cups = [cups[start]] + cups[start+1:] + cups[:start]


print(cups[1] * cups[2])
