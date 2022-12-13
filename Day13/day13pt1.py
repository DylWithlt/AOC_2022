from itertools import zip_longest as izip_longest
import sys

sys.setrecursionlimit(100)


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)


def compare(left, right):

    if type(left) is int and type(right) is int:
        if left < right:
            return "T"
        elif left > right:
            return "F"
        else:
            return "C"

    if not (type(left) is list):
        left = [left]
    if not (type(right) is list):
        right = [right]

    while len(left) > 0 and len(right) > 0:
        comp = compare(left.pop(0), right.pop(0))
        if comp == "C":
            continue
        else:
            return comp
    if len(left) > 0:
        return "F"
    elif len(right) > 0:
        return "T"
    else:
        return "C"


with open('./Day13/input.txt', 'r') as f:

    rights = 0

    for i, group in enumerate(grouper(f, 3, '')):
        pair = [eval(x) for x in group[0:2]]

        left = pair[0]
        right = pair[1]

        comp = compare(left, right)
        if comp == "T":
            print(i + 1, comp)
            rights += i + 1
    print(rights)
