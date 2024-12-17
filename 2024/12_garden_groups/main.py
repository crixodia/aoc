from itertools import combinations


def read_input(input_file="input.txt"):
    return [list(x.replace("\n", "")) for x in open(input_file, "r").readlines()]


def __get_region__(dir, plot, visited):
    i, j = dir
    rows, cols = len(plot), len(plot[0])

    neighbors = list(filter(
        lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols,
        [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    ))

    for n in neighbors:
        if n in visited:
            continue

        ii, jj = n
        if plot[ii][jj] == plot[i][j]:
            visited.add(n)
            visited.update(__get_region__(n, plot, visited))

    return visited


def get_region(dir, plot):
    return list(__get_region__(dir, plot, {dir}))


def is_region_inside(R1, R2):
    for i, j in R2:
        ns = filter(lambda x: x[0] == i, R1)
        we = filter(lambda x: x[1] == j, R1)

        ns = combinations(ns, 2)
        we = combinations(we, 2)

        for n, s in ns:
            _, ny = n
            _, sy = s

            if not (ny < i < sy or sy < i < ny):
                continue

            for w, e in we:
                wx, _ = w
                ex, _ = e

                if not (wx < j < ex or ex < j < wx):
                    continue

                return False

    return True


def solve(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])

    all_visited = set()
    areas = []
    perimeters = []

    region_borders = dict()

    for i in range(rows):
        for j in range(cols):
            if (i, j) in all_visited:  # is part of other region
                continue

            r = get_region((i, j), puzzle)

            border = set()
            all_visited.update(r)

            areas.append(len(r))
            perimeters.append(0)

            while r != []:
                ii, jj = r.pop(0)
                neighbors = list(
                    filter(
                        lambda x: puzzle[x[0]][x[1]] == puzzle[i][j],
                        filter(
                            lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols,
                            [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]
                        )
                    )
                )

                perimeters[-1] += 4 - len(neighbors)

                if len(neighbors) < 4:
                    border.add((ii, jj))

            region_borders[(i, j)] = border

    parent_child = dict()
    for k, v in region_borders.items():
        for kk, vv in region_borders.items():
            if k == kk:
                continue

            if is_region_inside(v, vv):
                parent_child[k] = kk

    print(parent_child)
    print(list(region_borders.keys()))

    return sum([areas[i] * perimeters[i] for i in range(len(areas))])


puzzle = read_input()
ans = (solve(puzzle), )
print(ans)
