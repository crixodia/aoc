from operator import imul
from functools import reduce


def read_input(input_path: str) -> list:
    lines = open(input_path, "r").read().split()
    return [list(x) for x in lines]


def sum_tuple(A: tuple, B: tuple) -> tuple:
    return tuple([A[i] + B[i] for i in range(len(A))])


def solve(grid: list, slope: tuple) -> int:
    x, y = (0, 0)
    trees = 0
    while y < len(grid) - 1:

        x, y = sum_tuple((x, y), slope)
        x = x % len(grid[0])

        if grid[y][x] == "#":
            trees += 1

    return trees


def solve2(grid: list, slopes: list) -> int:
    return reduce(
        imul,
        map(
            lambda s: solve(grid, s),
            slopes
        )
    )


puzzle_input = read_input("input.txt")

ans1 = solve(puzzle_input, (3, 1))
ans2 = solve2(puzzle_input, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

ans = (ans1, ans2)
print(ans)
