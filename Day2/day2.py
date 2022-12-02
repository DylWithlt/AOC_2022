def get_score(a, b):
    if a == 'A':
        if b == 'X':
            return 3
        elif b == 'Y':
            return 6
        elif b == 'Z':
            return 0
    elif a == 'B':
        if b == 'X':
            return 0
        elif b == 'Y':
            return 3
        elif b == 'Z':
            return 6
    elif a == 'C':
        if b == 'X':
            return 6
        elif b == 'Y':
            return 0
        elif b == 'Z':
            return 3


with open('input.txt', 'r') as f:
    score = 0

    for line in f.readlines():
        msg = line.strip().split(" ")
        a = msg[0]
        b = msg[1]

        if b == 'X':
            score += 1
        elif b == 'Y':
            score += 2
        elif b == 'Z':
            score += 3
        score += get_score(a, b)

    print(score)
