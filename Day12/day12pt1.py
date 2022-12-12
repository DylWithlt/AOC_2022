from introcs import Vector2
from queue import PriorityQueue
import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class Node(object):
    def __init__(self, letter, pos):
        self.letter = letter
        self.pos = pos
        self.f = 0
        self.h = 0
        self.g = 0
        self.closed = False

        self.children = []
        self.parent = None

    def get_letter(self):
        return self.letter

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def __gt__(self, other):
        return self.f > other.f

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f'Node({self.letter}, {self.pos}, {self.f})'


with open('./Day12/input.txt', 'r') as f:

    grid = []

    S = None
    E = None

    def h_heur(tile, goal):
        return math.sqrt(pow(tile.pos.x - goal.pos.x, 2.0) + pow(tile.pos.y - goal.pos.y, 2.0))

    def backtrack(node):
        print("BACKTRACKING")
        path = []

        ancestor = node.parent
        while ancestor:
            print(ancestor)
            path.append(ancestor)
            ancestor = ancestor.parent
        print(len(path))

    def greedy(start, goal):
        open = PriorityQueue()

        start.g = 0
        start.h = 0
        start.f = 0
        open.put(start)

        # N E S W
        while not open.empty():
            cur = open.get()

            # print(cur)

            if cur.letter == "E":
                backtrack(cur)
                return

            cur.closed = True
            for line in grid:
                letters = []
                for node in line:
                    if node.closed:
                        letters.append(f"{Back.RED}{node.letter}")
                    elif node in open.queue:
                        letters.append(f"{Back.GREEN}{node.letter}")
                    else:
                        letters.append(f"{Back.WHITE}{node.letter}")

                print("".join(letters))

            cur.children = [
                cur.pos + Vector2(0, -1),
                cur.pos + Vector2(0, 1),
                cur.pos + Vector2(-1, 0),
                cur.pos + Vector2(1, 0),
            ]

            child_nodes = []
            for pos in cur.children:
                if pos.y < 0 or pos.y >= len(grid) or pos.x < 0 or pos.x >= len(grid[int(pos.y)]):
                    continue
                child_nodes.append(grid[int(pos.y)][int(pos.x)])

            for child in child_nodes:

                if child.closed:
                    continue

                if not (cur.letter == "S" or (cur.letter == "z" and child.letter == "E")) and (ord(child.letter) - ord(cur.letter)) > 1:
                    continue

                g = cur.g + 1
                h = h_heur(child, goal)
                f = g + h

                if child.f < f:
                    child.parent = cur
                    child.g = g
                    child.h = h
                    child.f = f
                    if not (child in open.queue):
                        open.put(child)

        print("FAILURE")

    for y, line in enumerate(f.readlines()):

        grid.append([])
        for x, letter in enumerate(list(line.strip())):
            node = Node(letter, Vector2(x, y))
            grid[y].append(node)
            if "S" == letter:
                S = node
            if "E" == letter:
                E = node

    greedy(S, E)
