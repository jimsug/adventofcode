from aocd import data

part1 = 0
part2 = 0

lines = data.split("\n")
chunks = [lines[i*3:(i+1)*3] for i in range((len(lines)+2)//3)]

for s in lines:
    s1, s2 = s[:len(s)//2], s[len(s)//2:]
    char = list(set([c for c in s1 if c in s2]))[0]
    part1+= ord(char) - (38 if char.isupper() else 96)

for c in chunks:
    c1, c2, c3 = c
    char = [c for c in c1 if c in c2 and c in c3][0]
    part2+= ord(char) - (38 if char.isupper() else 96)


print(part1)
print(part2)