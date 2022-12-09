from introcs import Vector2
import math

root2 = math.sqrt(2)
with open('./Day9/input.txt', 'r') as f:
    grid = {"0_0": True}

    count = 0
    T = Vector2()
    H = Vector2()
    lastH = H

    for line in f.readlines():
        data = line.strip().split()
        dir = data[0]
        for x in range(int(data[1])+1):
            lastH = H.copy()
            if dir == "U":
                H += Vector2(0, 1)
            elif dir == "D":
                H += Vector2(0, -1)
            elif dir == "R":
                H += Vector2(1, 0)
            elif dir == "L":
                H += Vector2(-1, 0)

            if (T - H).length() > 1.5:
                T = lastH
                serialized = str(T.x) + "_" + str(T.y)
                if not (serialized in grid):
                    count += 1
                    grid[serialized] = True

    print(count)
