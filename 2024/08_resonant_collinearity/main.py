from itertools import combinations
from math import sqrt


def read_input(input_file="input.txt"):
    lines = open(input_file, "r").readlines()
    return [list(line.replace("\n", "")) for line in lines]


def solve(puzzle, any_grid=False):

    rows, cols = len(puzzle), len(puzzle[0])
    nodes = dict()

    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] == ".":
                continue

            if puzzle[i][j] not in nodes:
                nodes[puzzle[i][j]] = [(j, i)]
            else:
                nodes[puzzle[i][j]].append((j, i))

    antinodes = set()
    for node in nodes:
        pairs = set(combinations(nodes[node], 2))

        for pair in pairs:
            x1, y1 = pair[0]
            x2, y2 = pair[1]

            # Geometry Ñ=
            v = (x2-x1, y2-y1)
            d = sqrt((y2-y1)**2 + (x2-x1)**2)
            u = (v[0]/d, v[1]/d)

            k = 1 if any_grid else 2
            while True:
                # Must round due Python and computer floating number things
                ax = int(round(+k*d*u[0] + x1, 2))
                ay = int(round(+k*d*u[1] + y1, 2))

                if 0 <= ax < cols and 0 <= ay < rows:
                    antinodes.add((ax, ay))
                else:
                    break
                if not any_grid:
                    break

                k += 1

            k = 1 if any_grid else 2
            while True:

                bx = int(round(-k*d*u[0] + x2, 2))
                by = int(round(-k*d*u[1] + y2, 2))

                if 0 <= bx < cols and 0 <= by < rows:
                    antinodes.add((bx, by))
                else:
                    break
                if not any_grid:
                    break
                k += 1

    return len(antinodes)


puzzle = read_input()
ans = (solve(puzzle), solve(puzzle, True))
print(ans)
