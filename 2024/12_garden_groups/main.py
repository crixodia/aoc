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
    check = []
    for i, j in R2:
        ns = filter(lambda x: x[1] == j, R1)
        we = filter(lambda x: x[0] == i, R1)

        ns = [(x[0][0], x[1][0]) for x in combinations(ns, 2)]
        we = [(x[0][1], x[1][1]) for x in combinations(we, 2)]

        if ns == [] or we == []:
            return False

        for ns1, ns2 in ns:
            n = min(ns1, ns2)
            s = max(ns1, ns2)

            found = False

            if n < i < s:
                for we1, we2 in we:
                    w = min(we1, we2)
                    e = max(we1, we2)

                    if w < j < e:
                        check.append(True)
                        found = True
                        break
            if found:
                break

    return all != [] and all(check)


def solve(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])

    all_visited = set()

    areas = []
    perimeters = []
    region_borders = dict()
    regions = dict()

    for i in range(rows):
        for j in range(cols):
            if (i, j) in all_visited:  # is part of other region
                continue

            r = get_region((i, j), puzzle)
            regions[(i, j)] = r.copy()

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
                if k not in parent_child:
                    parent_child[k] = [kk]
                else:
                    parent_child[k].append(kk)

    all_childs = [v for k, v in parent_child.items()]
    all_childs = sum(all_childs, [])

    inmediate_childs = {}
    for k, v in parent_child.items():
        for vv in v:
            if all_childs.count(vv) == 1:
                if k not in inmediate_childs:
                    inmediate_childs[k] = [vv]
                else:
                    inmediate_childs[k].append(vv)
            all_childs.remove(vv)

    external_sides = dict()
    for r in regions:
        for i, j in r:
            neighbors = list(
                filter(
                    lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols,
                    [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                )
            )

    return sum([areas[i] * perimeters[i] for i in range(len(areas))])


puzzle = read_input()
ans = (solve(puzzle), )
print(ans)
