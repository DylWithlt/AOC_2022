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


def get_new_input(a, b):
    if b == 'X':
        if a == 'A':
            return 'Z'
        elif a == 'B':
            return 'X'
        elif a == 'C':
            return 'Y'
    elif b == 'Y':
        if a == 'A':
            return 'X'
        elif a == 'B':
            return 'Y'
        elif a == 'C':
            return 'Z'
    elif b == 'Z':
        if a == 'A':
            return 'Y'
        elif a == 'B':
            return 'Z'
        elif a == 'C':
            return 'X'


with open('./Day2/input.txt', 'r') as f:
    score = 0

    for line in f.readlines():
        msg = line.strip().split(" ")
        a = msg[0]
        b = msg[1]
        b = get_new_input(a, b)

        if b == 'X':
            score += 1
        elif b == 'Y':
            score += 2
        elif b == 'Z':
            score += 3
        score += get_score(a, b)

    print(score)
