def read_input(input_path: str) -> list:
    lines = open(input_path, "r").read().split("\n")
    return [int(x) for x in lines]


def solve(input: list, target: int = 2020) -> tuple:  # classic two sum
    difs = dict()

    for val in input:
        difs[target-val] = val

    for key, val in difs.items():
        if key in input:
            return key, val

    return None, None


def solve2(input: list, target: int = 2020) -> tuple:  # classic three sum
    difs = dict()

    for val in input:
        difs[target-val] = val

    for key, val in difs.items():
        x, y = solve(input, key)
        if x and y:
            return val, x, y

    return None, None, None


input = read_input("input.txt")

x, y = solve(input)
ans1 = x*y

x, y, z = solve2(input)
ans2 = x*y*z

ans = (ans1, ans2)
print(ans)
