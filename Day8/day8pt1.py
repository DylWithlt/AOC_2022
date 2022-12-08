

with open('./Day8/input.txt', 'r') as f:
    grid = []

    def is_visible(x, y):
        value = int(grid[x][y])
        print(x, y, value)

        n = True
        e = True
        s = True
        w = True

        m_x = x - 1
        while m_x >= 0:
            valueAt = int(grid[m_x][y])
            if valueAt >= value:
                w = False
                break
            m_x -= 1

        m_x = x + 1
        while m_x < len(grid[x]):
            valueAt = int(grid[m_x][y])
            if valueAt >= value:
                e = False
                break
            m_x += 1

        m_y = y - 1
        while m_y >= 0:
            valueAt = int(grid[x][m_y])
            if valueAt >= value:
                n = False
                break
            m_y -= 1

        m_y = y + 1
        while m_y < len(grid):
            valueAt = int(grid[x][m_y])
            if valueAt >= value:
                s = False
                break
            m_y += 1

        return n or e or s or w

    for line in f.readlines():
        grid.append(line.strip())

    count = 0
    for x in range(len(grid)):
        for y in range(len(line)):
            if is_visible(x, y):
                count += 1

    print(count)
