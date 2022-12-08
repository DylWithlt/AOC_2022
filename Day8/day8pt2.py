

with open('./Day8/input.txt', 'r') as f:
    grid = []

    def scenic_score(x, y):
        value = int(grid[x][y])
        print(x, y, value)

        if x == 0:
            return 1
        elif x == len(grid[x])-1:
            return 1
        if y == 0:
            return 1
        if y == len(grid)-1:
            return 1

        n = 0
        e = 0
        s = 0
        w = 0

        m_x = x - 1
        while m_x >= 0:
            valueAt = int(grid[m_x][y])
            if valueAt >= value:
                break
            w += 1
            m_x -= 1

        m_x = x + 1
        while m_x < len(grid[x]):
            valueAt = int(grid[m_x][y])
            e += 1
            if valueAt >= value:
                break

            m_x += 1

        m_y = y - 1
        while m_y >= 0:
            valueAt = int(grid[x][m_y])
            n += 1
            if valueAt >= value:
                break

            m_y -= 1

        m_y = y + 1
        while m_y < len(grid):
            valueAt = int(grid[x][m_y])
            s += 1
            if valueAt >= value:
                break

            m_y += 1

        print(n, e, s, w)
        return n * e * s * w

    for line in f.readlines():
        grid.append(line.strip())

    count = 0
    scores = []
    for x in range(len(grid)):
        for y in range(len(line)):
            scores.append(scenic_score(x, y))

    print(max(scores))
