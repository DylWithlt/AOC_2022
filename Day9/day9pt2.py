from introcs import Vector2
import math


root2 = math.sqrt(2)
with open('./Day9/input.txt', 'r') as f:
    grid = {}
    lastRope = []
    rope = []

    print((Vector2(1, 2) - Vector2(0, 0)).length())

    for x in range(10):
        rope.append(Vector2())
    lastRope = rope.copy()

    def shouldMove(i):
        if i == 0:
            return False

    def move(i):
        vec = (rope[i-1] - rope[i])
        length = vec.length()
        if length > 1.5:
            unit = vec.normalize()
            if length <= 2:
                rope[i] += unit
            elif length > 2:
                rope[i] += Vector2(-1 if unit.x < 0 else 1, -
                                   1 if unit.y < 0 else 1)

    for line in f.readlines():
        data = line.strip().split()
        dir = data[0]
        for x in range(int(data[1])):
            if dir == "U":
                rope[0] += Vector2(0, 1)
            elif dir == "D":
                rope[0] += Vector2(0, -1)
            elif dir == "R":
                rope[0] += Vector2(1, 0)
            elif dir == "L":
                rope[0] += Vector2(-1, 0)

            for i in range(1, 10):
                move(i)
                if i == 9:
                    serialized = str(rope[i].x) + "_" + str(rope[i].y)
                    grid[serialized] = True
    print(len(grid.values()))
