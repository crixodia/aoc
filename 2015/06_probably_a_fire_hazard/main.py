def read_input(file):
    rows = []
    with open(file, "r") as f:
        for line in f:
            row = line.replace("\n", "")
            row = row.replace(" through ", ",")
            row = row.replace("turn on ", "1,")
            row = row.replace("turn off ", "-1,")
            row = row.replace("toggle ", "2,")
            row = row.split(",")

            rows.append([int(x) for x in row])
    # state, x, y, X, Y
    return rows


def solve(rows):
    grid = [[False] * 1000 for _ in range(1000)]

    # 3 for 🤮 not the best solution
    for row in rows:
        state, x, y, X, Y = row
        for i in range(x, X + 1):
            for j in range(y, Y + 1):
                if state == 1:  # Turn on
                    grid[i][j] = True
                elif state == -1:  # Turn off
                    grid[i][j] = False
                else:
                    grid[i][j] = not grid[i][j]

    return sum(list(map(sum, grid)))


def solve2(rows):
    grid = [[0] * 1000 for _ in range(1000)]

    # 3 for 🤮 not the best solution
    for row in rows:
        state, x, y, X, Y = row
        for i in range(x, X + 1):
            for j in range(y, Y + 1):
                if state == -1 and grid[i][j] == 0:
                    continue

                grid[i][j] = grid[i][j] + state

    return sum(list(map(sum, grid)))


input = read_input("input.txt")
ans = (solve(input), solve2(input))
print(ans)
