with open("2020/day_16/input.txt") as f:
    input = f.read().strip().split("\n\n")

yourticket = [ int(i) for i in input[1].split('\n')[1].split(',') ]

params = {m:set().union(*[set(range(o[0], o[1] + 1)) for o in n]) for m, n in {j[0]:[[int(l) for l in k.strip().split('-')] for k in j[1].strip().split('or') ] for j in [ i.strip().split(":") for i in input[0].strip().split('\n')]}.items()}

nearbytickets = [ [int(j) for j in i.split(',')] for i in input[2].strip().split('\n')[1:] ]

valids = set().union(*list(params.values()))

errors = []
notinvalidtickets = []
for t in nearbytickets:
    inv = False
    for i in t:
        if not i in valids:
            inv = True
            errors.append(i)
    if not inv:
        notinvalidtickets.append(t)

print("Part 1:", sum(errors))

fields = [0]*len(params.keys())
possible = []

def getNotInvalidFields(ps, vals):
    posfields = []
    for p, q in ps.items():
        if vals.issubset(q):
            posfields.append(p)
    return posfields

for i in range(len(params.keys())):
    possible.append(getNotInvalidFields(params, set([t[i] for t in notinvalidtickets])))

while any(possible):
    for i in range(len(possible)):
        if len(possible[i]) == 1:
            fields[i] = possible[i][0]
            for j in range(len(possible)):
                if fields[i] in possible[j]:
                    possible[j].remove(fields[i])

print(fields)
muls = 1
for i in range(len(fields)):
    if fields[i].startswith("departure"):
        muls*= yourticket[i]

print(muls)
