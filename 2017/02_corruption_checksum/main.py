from itertools import combinations


def read_input(input_path: str) -> list:
    lines = open(input_path, "r").read()
    lines = lines.split("\n")

    input = []
    for line in lines:
        l = line.split("\t")
        input.append([int(x) for x in l])

    return input


def solve(input: list) -> int:
    mins = [min(row) for row in input]
    maxs = [max(row) for row in input]

    checksum = 0
    for i in range(len(input)):
        checksum += maxs[i] - mins[i]

    return checksum


def solve2(input: list) -> int:
    def evenly_divide(pair: tuple) -> bool:
        x = max(pair)
        y = min(pair)

        return x % y == 0

    checksum = 0
    for line in input:
        pair = list(filter(
            evenly_divide,
            combinations(line, 2)
        ))[0]

        checksum += max(pair)//min(pair)

    return checksum


input = read_input("input.txt")
ans1 = solve(input)
ans2 = solve2(input)

ans = (ans1, ans2)
print(ans)
