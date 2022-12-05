import re

stacks = {
    1: ['H', 'T', 'Z', 'D'],
    2: ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],
    3: ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],
    4: ['L', 'C', 'N', 'F', 'H', 'Z'],
    5: ['G', 'L', 'F', 'Q', 'S'],
    6: ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],
    7: ['Z', 'F', 'J'],
    8: ['D', 'L', 'V', 'Z', 'R', 'H', 'Q'],
    9: ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']
}


with open('./Day5/input.txt', 'r') as f:
    for line in f.readlines():
        digits = re.findall("\d+", line.strip())

        times = int(digits[0])
        src = int(digits[1])
        dst = int(digits[2])
        #print(times, src, dst)

        middle_man = []
        for x in range(times):
            new = stacks[src].pop()
            middle_man.append(new)

        for x in range(times):
            stacks[dst].append(middle_man.pop())

    for x in stacks:
        print(x, stacks[x])
