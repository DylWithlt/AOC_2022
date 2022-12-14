
with open('./Day14/input.txt', 'r') as f:
    grid = {}

    def draw_line(pt1, pt2):
        if pt1[0] == pt2[0]:
            dir = -1 if pt1[1] > pt2[1] else 1
            for y in range(pt1[1], pt2[1] + dir, dir):
                grid[(pt1[0], y)] = "#"
        elif pt1[1] == pt2[1]:
            dir = -1 if pt1[0] > pt2[0] else 1
            for x in range(pt1[0], pt2[0]+dir, dir):
                grid[(x, pt1[1])] = "#"
        else:
            grid[pt1] = "#"

    highest_y = 0

    for x in f.readlines():
        segments = x.strip().split(' ')
        while '->' in segments:
            segments.remove('->')
        segments = [eval("(" + x + ")") for x in segments]
        for x in range(len(segments) - 1):
            highest_y = max(highest_y, segments[x][1])
            draw_line(segments[x], segments[x+1])

    def print_grid():
        for y in range(0, 10):
            line = []
            for x in range(493, 504):
                line.append(grid[(x, y)] if (x, y) in grid else ".")
            print("".join(line))
    print_grid()

    sand_start = (500, 0)
    sand_count = 0

    def sand_fall():
        pos = sand_start
        down = tuple((pos[0], pos[1] + 1))
        while True:
            if pos[1] > highest_y:
                return "Void"
            if not (down in grid):
                pos = tuple(down)
                down = tuple((pos[0], pos[1] + 1))
            else:
                down_left = tuple((down[0] - 1, down[1]))
                down_right = tuple((down[0] + 1, down[1]))
                if not (down_left in grid):
                    pos = tuple(down_left)
                    down = tuple((pos[0], pos[1] + 1))
                elif not (down_right in grid):
                    pos = tuple(down_right)
                    down = tuple((pos[0], pos[1] + 1))
                else:
                    grid[pos] = "o"
                    return "Stopped"

            print(down)

    result = sand_fall()
    while result != "Void":
        sand_count += 1
        result = sand_fall()

    print(sand_count)
