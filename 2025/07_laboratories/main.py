from functools import lru_cache
from collections import defaultdict


def read_input(filename: str = "input.txt"):
    return [
        list(x.replace("\n", ""))
        for x in open(filename, "r").readlines()
    ]


def count_paths(tree, start, end):
    @lru_cache(None)
    def dfs(node):
        if node == end:
            return 1
        total = 0
        for nxt in tree.get(node, []):
            total += dfs(nxt)
        return total
    return dfs(start)


def solve(puzzle):
    idx_to_process = []
    splits = 0

    tree = defaultdict(list)

    for i, row in enumerate(puzzle):
        for j, col in enumerate(row):
            if col == "^":
                for k in [j+1, j-1]:
                    if all([k != "|", j-1 >= 0, j+1 < len(row), puzzle[i-1][j] in ["S", "|"]]):
                        splits += 1
                        puzzle[i][k] = "|"

                        tree[(i-1, j)].append((i, k))
            elif j in idx_to_process:
                puzzle[i][j] = "|"
                tree[(i-1, j)].append((i, j))

        idx_to_process = [k for k in range(len(row)) if row[k] in ["S", "|"]]

    total_paths = 0
    first_node = (0, puzzle[0].index("S"))
    for j in range(len(puzzle[-1])):
        if puzzle[-1][j] == "|":
            total_paths += count_paths(tree, first_node, (len(puzzle)-1, j))

    return splits//2, total_paths


puzzle = read_input()
ans = (solve(puzzle))
print(ans)
