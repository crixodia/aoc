from collections import Counter
from itertools import combinations


def read_input(input_path: str) -> list:
    return open(input_path).read().split("\n")


def solve(input: list) -> int:

    two, three = 0, 0

    for line in input:
        c = Counter(line)
        counts = list(c.values())

        if 2 in counts:
            two += 1

        if 3 in counts:
            three += 1

    return two * three


def get_difference(x: tuple) -> str:
    diff = ""
    a, b = x
    for i in range(len(a)):
        if a[i] == b[i]:
            diff += a[i]

    return diff


def solve2(input: list) -> str:
    max_n = len(input[0])
    return list(
        filter(
            lambda x: len(x) == max_n - 1,
            map(
                get_difference,
                combinations(input, 2)
            )
        )
    )[0]


input = read_input("input.txt")
ans1 = solve(input)
ans2 = solve2(input)

ans = (ans1, ans2)
print(ans)
