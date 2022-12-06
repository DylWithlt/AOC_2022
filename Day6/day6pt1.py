

with open('./Day6/input.txt', 'r') as f:
    lastFour = []
    counter = 0
    for letter in f.read():
        if len(lastFour) < 4:
            lastFour.append(letter)
            counter += 1
            continue

        if len(set(lastFour)) < 4:
            lastFour.pop(0)
            lastFour.append(letter)
            counter += 1
        else:
            break
    print(counter)
