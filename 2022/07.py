from aocd import data
from aocd.models import Puzzle

data == '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

dirsizes = {}
currdir = ["root"]

for line in data.split("\n"):
    args = line.split(" ")
    if args[0] == "$":
        if args[1] == "ls":
            pass
        elif args[1] == "cd":
            if args[2] == "/":
                currdir = ["root"]
            elif args[2] == "..":
                currdir.pop()
            else:
                currdir.append(args[2])
    else:
        if args[0] == "dir":
            pass
        else:
            for i in range(1, len(currdir) + 1):
                try:
                    dirsizes["/".join(currdir[0:i])] += int(args[0])
                except KeyError:
                    dirsizes["/".join(currdir[0:i])] = int(args[0])

# print(dirsizes)

filter1 = [v for v in dirsizes.values() if v <= 100000]
# print(filter1)
print(sum([v for v in filter1]))

needed_space = 30000000 - (70000000 - dirsizes["root"])
print(f'needed space: {needed_space}')
filter2 = [v for v in dirsizes.values() if v >= needed_space]
print(min(filter2))