from abc import ABC
from re import A
from aocd.models import Puzzle
# p = Puzzle(year=2021, day=8).input_data
p = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\nedbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc\nfgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg\nfbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\naecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea\nfgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb\ndbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe\nbdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef\negadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb\ngcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
input = [[j.strip().split() for j in i.split("|")] for i in p.split("\n")]

# 0 = abcefg   tuvxyz
# 1 = cf
# 2 = acdeg
# 3 = acdfg    u
# 4 = bcdf     uvwy
# 5 = abdfg    tuwyz
# 6 = abdefg   tuwxyz
# 7 = acf      tvy
# 8 = abcdefg  tuvwxyz
# 9 = abcdfg   tuvwyz

true_masks = {
    "ABCEFG": 0,
    "CF": 1,
    "ACDEG": 2,
    "ACDFG": 3,
    "BCDF": 4,
    "ABDFG": 5,
    "ABDEFG": 6,
    "ACF": 7,
    "ABCDEFG": 8,
    "ABCDFG": 9,
}
'''
1.  Find the 7
2.  Find the 1 = this will let you identify A, because there will be one extra segment in 7
3.  Find the 8 (this doesn't give any new info, but that's fine)
4.  Find the 4 =
5.  Find the 9 - it'll be the one with exactly two segments that differ from 4
6.  Using 9 and 4 you can find G, because you know what A is
7.  Find the 6 - this one has one different from 9, which is E
8.  Find the 5, which is the one missing E
9.  Find the 2, which is the one with E but missing B - it has C, instead
10. Find 3, which is a 2 but with an F instead of an E
11. Zero is the last one, and the difference between it and 8 is D
'''



def count_common(w1:str, w2:str) -> int:
    return len(list(set([c for c in w1]) & set([c for c in w2])))


def solve_row(args:list)->dict:
    wiring = {}
    data, digits = args
    seven = [i for i in data if len(i) == 3][0]
    data.remove(seven)

    one = [i for i in data if len(i) == 2][0]
    data.remove(one)

    wiring['A'] = [i for i in seven if i not in one][0]

    four = [i for i in data if len(i) == 4][0]
    data.remove(four)

    nine = [i for i in data if len(i) == 6 and wiring['A'] in i and count_common(i, four) == 4][0]
    data.remove(nine)

    wiring['G'] = [i for i in nine if i != wiring['A'] and i not in four][0]

    six = [i for i in data if len(i) == 6 and count_common(i, nine) == 5][0]
    data.remove(six)

    wiring['E'] = [i for i in six if i not in nine][0]

    five = [i for i in data if len(i) == 5 and wiring ['E'] not in i and count_common(i, six)][0]
    data.remove(five)
    print(five)
    print(data)
    print(wiring)

    two = [i for i in data if len(i) == 5 and wiring['E'] in i and count_common(i, five) == 3][0]
    data.remove(two)

    wiring['C'] = [i for i in two if i not in five and i != wiring['E']][0]

    eight = [i for i in data if len(i) == 7][0]
    data.remove(eight)

    zero = [i for i in data if len(i) == 6][0]
    data.remove(zero)

    three = data[0]

    wiring['F'] = [c for c in three if c not in two][0]

    wiring['D'] = [c for c in eight if c not in zero][0]

    wiring['B'] = [i for i in five if i not in two and i != wiring['C'] and i != wiring['F']][0]

    wiring = {v:k for k, v in wiring.items()}
    output = []
    for d in digits:
        t = []
        for c in d:
            t.append(wiring[c])

        t.sort()
        t = "".join(t)
        output.append(t)

    return output

digits = []

for l in input:
    digits.append([true_masks[i] for i in solve_row(l)])

print(digits)
