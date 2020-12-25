import numpy

with open("2020/day_20/input.txt") as f:
    input = {k[0]:k[1].split("\n") for k in [[j.strip() for j in i.split(":")] for i in f.read().strip().split("\n\n")]}

edges = {}

for k, v in input.items():
    edge = {'t':[], 'b':[], 'l':[], 'r':[]}
    t = [ c for c in v[0] ].copy()
    t2 = t.copy()
    t2.reverse()
    edge['t'].append(''.join(t))
    edge['t'].append(''.join(t2))
    b = [c for c in v[-1]].copy()
    b2 = b.copy()
    b2.reverse()
    edge['b'].append(''.join(b))
    edge['b'].append(''.join(b2))
    l = [e[0] for e in v]
    l2 = l.copy()
    l2.reverse()
    edge['l'].append(''.join(l))
    edge['l'].append(''.join(l2))
    r = [e[-1] for e in v]
    r2 = r.copy()
    r2.reverse()
    edge['r'].append(''.join(r))
    edge['r'].append(''.join(r2))
    edges[k] = edge

alledges = [list(e.values()) for e in edges.values()]
# unique_edges = [[f[0] for f in e.values()] for e in edges.values()]
# print(unique_edges)

matches = {}
tilemap = {}
for tile, edgess in edges.items():
    edgematches = set()
    edge = {'t':[], 'b':[], 'l':[], 'r':[]}
    for orientation, edgeref in edgess.items():
        for stile, stedge in edges.items():
            for sorientation, sedgeref in stedge.items():
                if edgeref[0] in sedgeref and tile != stile:
                    edgematches.add(stile)
                    edge[orientation] = [edgeref[0], stile, sorientation, sedgeref.index(edgeref[0])]
    tilemap[tile] = edge
    matches[tile] = edgematches

score = 1
corners = []
for m, n in matches.items():
    if len(n) == 2:
        score*=int(m.split( )[1])
        corners.append({m:n})

print("Part 1:", score)

start = tilemap[list(corners[0].keys())[0]]

field = numpy.zeros()

print(len(tilemap))
