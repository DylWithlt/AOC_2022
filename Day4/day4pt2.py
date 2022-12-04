import re

with open('./Day4/input.txt', 'r') as f:
    count = 0
    for line in [x.strip() for x in f.readlines()]:
        digits = re.findall("\d+", line)

        x1 = int(digits[0])
        y1 = int(digits[1])
        x2 = int(digits[2])
        y2 = int(digits[3])

        if x1 <= x2 and x2 <= y1 or x2 <= x1 and x1 <= y2 or x1 <= x2 and y1 >= y2 or x2 <= x1 and y2 >= y1:
            count += 1

    print(count)
