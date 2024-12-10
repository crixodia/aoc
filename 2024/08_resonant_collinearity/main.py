from pprint import pprint
from itertools import combinations
from math import sqrt


def read_input(input_file="input.txt"):
    lines = open(input_file, "r").readlines()
    return [list(line.replace("\n", "")) for line in lines]


def solve(puzzle):
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
        pairs = list(combinations(nodes[node], 2))

        for pair in pairs:
            x2, y2 = pair[0]
            x1, y1 = pair[1]

            v = (x2-x1, y2-y1)
            d = sqrt((y2-y1)**2 + (x2-x1)**2)
            u = (v[0]/d, v[1]/d)

            a = (int(+2*d*u[0] + x1), int(+2*d*u[1] + y1))
            b = (int(-2*d*u[0] + x2), int(-2*d*u[1] + y2))

            antinodes.add(a)
            antinodes.add(b)

    antinodes_num = 0
    visited = []
    for antinode in antinodes:
        x, y = antinode
        if 0 <= x < cols and 0 <= y < rows and antinode not in visited:
            antinodes_num += 1
            visited.append(antinode)
            if puzzle[y][x] == ".":
                puzzle[y][x] = "#"

    for i in range(rows):
        print(puzzle[i])
    return antinodes_num


puzzle = read_input()
ans = (solve(puzzle),)
print(ans)
# pprint(puzzle)
