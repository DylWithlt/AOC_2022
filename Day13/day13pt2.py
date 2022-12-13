from itertools import zip_longest as izip_longest
import sys
from copy import deepcopy

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


class Packet(object):
    def __init__(self, data):
        self.data = data

    def __gt__(self, other):
        return compare(deepcopy(self.data), deepcopy(other.data)) == "F"

    def __lt__(self, other):
        return compare(deepcopy(self.data), deepcopy(other.data)) == "T"

    def __repr__(self):
        return f"Packet({str(self.data)})"


with open('./Day13/input.txt', 'r') as f:

    div1 = Packet([[2]])
    div2 = Packet([[6]])

    all_packets = [div1, div2]

    for i, group in enumerate(grouper(f, 3, '')):
        pair = [eval(x) for x in group[0:2]]

        all_packets.append(Packet(pair[0]))
        all_packets.append(Packet(pair[1]))

    print(all_packets)

    all_packets.sort()

    print("Result")
    print(all_packets)
    print((all_packets.index(div1) + 1) * (all_packets.index(div2) + 1))
