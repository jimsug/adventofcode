from aocd import data
from aocd.models import Puzzle

def decode(input, n):
    return min( [ c for c in range(n, len(input)) if len(set(ch for ch in input[c-n:c])) == n] )

print(decode(data, 4))
print(decode(data, 14))
