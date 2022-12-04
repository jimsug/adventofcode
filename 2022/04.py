from aocd import data

part1 = 0
part2 = 0
for line in data.split("\n"):
    pt1 = False
    lmin, lmax, rmin, rmax = [int(n) for p in line.split(",") for n in p.split("-")]
    if (lmin <= rmin and lmax >= rmax) or (rmin <= lmin and rmax >= lmax):
        part1+=1
        pt1 = True
    if pt1 or (rmin <= lmin <= rmax and lmax >= rmin) or (lmin <= rmin <= lmax and rmax >= lmin):
        part2+=1

print(part1)
print(part2)