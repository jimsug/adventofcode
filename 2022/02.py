from aocd import data
scoring = {
    'X':1,
    'Y':2,
    'Z':3
}

conv = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

wins = {
    'X': 'Z',
    'Y': 'X',
    'Z': 'Y'
}

lose = {
    'Z': 'X',
    'X': 'Y',
    'Y': 'Z'
}


score = 0
score2 = 0
for i in data.split('\n'):
    a, b = i.split(' ')
    if conv[a] == b:
        score+=3
    if conv[a] == wins[b]:
        score+=6
    score+=scoring[b]

    me = ''
    if b == 'Z':
        # print("L: ", conv[a], [k for k,v in wins.items() if v == conv[a]][0])
        score2+= scoring[lose[conv[a]]]
        score2+=6
    if b == 'Y':
        score2+= scoring[conv[a]]
        score2+=3
    if b == 'X':
        # print("W: ", conv[a], wins[conv[a]])
        score2+=scoring[wins[conv[a]]]

print(score)
print(score2)