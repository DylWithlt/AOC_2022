from itertools import zip_longest as izip_longest


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def get_value(c):
    oc = ord(c)
    if oc > 96:
        return oc - 96
    else:
        return oc - 38


with open('./Day3/input.txt', 'r') as f:
    total = 0

    for lines in grouper(f, 3, ''):
        assert (len(lines) == 3)
        l1, l2, l3 = lines[0].strip(), lines[1].strip(), lines[2].strip()
        intersect = set(l1) & set(l2) & set(l3)
        total += get_value(intersect.pop())

    print(total)
