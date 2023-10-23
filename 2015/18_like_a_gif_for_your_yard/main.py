from copy import deepcopy


def read_input(file="input.txt"):
    content = []

    with open(file, "r") as f:
        for line in f:
            r = line.replace("\n", "")
            content.append(list(r))

    rows, cols = len(content), len(content[0])
    grid = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if content[i][j] == "#":
                grid[i][j] = True

    return grid


def print_grid(grid):
    n = len(grid)
    for i in range(n):
        g = ["#" if x else "." for x in grid[i]]
        print(*g, sep="")


def valid_position(position, n):
    x, y = position
    return not (x in [-1, n] or y in [-1, n])


def count_living(grid):
    count = 0
    for row in grid:
        count += sum(row)
    return count


def next_state(grid):
    n = len(grid)
    next_grid = deepcopy(grid)

    for i in range(n):
        for j in range(n):
            n_count = 0
            positions = [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
            ]

            positions = filter(
                lambda x: valid_position(x, n),
                positions,
            )

            for idx in positions:
                x, y = idx
                n_count += grid[x][y]

            if n_count == 3 and not grid[i][j]:
                next_grid[i][j] = True
            elif not (n_count in [2, 3] and grid[i][j]):
                next_grid[i][j] = False

    return next_grid


def stuck(grid, positions):
    for pos in positions:
        x, y = pos
        grid[x][y] = True
    return grid


def game_of_life(grid, steps):
    for i in range(steps):
        grid = next_state(grid)
    living = count_living(grid)
    return living


def game_of_life_stuck(grid, steps):
    rows, cols = len(grid), len(grid[0])
    stuck_pos = [(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)]
    for i in range(steps):
        grid = stuck(grid, stuck_pos)
        grid = next_state(grid)
        grid = stuck(grid, stuck_pos)

    living = count_living(grid)
    return living


STEPS = 100
puzzle_input = read_input()
ans1 = game_of_life(puzzle_input, STEPS)
ans2 = game_of_life_stuck(puzzle_input, STEPS)

ans = (ans1, ans2)
print(ans)
