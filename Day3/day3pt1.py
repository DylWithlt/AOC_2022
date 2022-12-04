
def get_value(c):
    oc = ord(c)
    if oc > 96:
        return oc - 96
    else:
        return oc - 38


with open('./Day3/input.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        fst, snd = line[:len(line)//2], line[len(line)//2:]
        intersection = [c for c in fst if c in snd]
        intersection = intersection[0]
        print(intersection, ord(intersection))
        total += get_value(intersection)
    print(total)
