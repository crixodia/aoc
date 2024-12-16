from pprint import pprint


def read_input(input_file="input.txt"):
    grid, moves = [], []
    is_moves = False
    with open(input_file, "r") as f:
        for line in f.readlines():
            if line == "\n":
                is_moves = True
            elif is_moves:
                moves.append(line.replace("\n", ""))
            else:
                grid.append(list(line.replace("\n", "")))

    return grid, moves


def get_move(move: str, i, j):
    ii, jj = 0, 0
    match move:
        case ">":
            jj += 1
        case "<":
            jj -= 1
        case "v":
            ii += 1
        case "^":
            ii -= 1

    return i + ii, j + jj


def get_current_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                return i, j

    return -1, -1


def solve(puzzle):
    grid, moves = puzzle
    i, j = get_current_pos(grid)

    for move in moves:
        for m in move:
            ii, jj = get_move(m, i, j)
            if grid[ii][jj] == "#":
                continue

            to_move = []
            x, y = ii, jj
            not_move = False
            while grid[x][y] == "O":
                to_move.append((x, y))
                x, y = get_move(m, x, y)
                if grid[x][y] == "#":
                    not_move = True

            if not_move:
                continue

            for x, y in to_move[::-1]:
                xx, yy = get_move(m, x, y)
                grid[xx][yy] = "O"
                grid[x][y] = "."

            grid[ii][jj] = "@"
            grid[i][j] = "."
            i, j = ii, jj

    gps_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                gps_sum += 100*i + j

    return gps_sum


puzzle = read_input()
ans = (solve(puzzle))
print(ans)
