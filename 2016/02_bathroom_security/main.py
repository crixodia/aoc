def read_input(input_path: str) -> list:
    lines = open(input_path, "r").read()
    lines = lines.split("\n")

    return lines


___ = None

KEYPAD1 = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

KEYPAD2 = [
    [___, ___, "1", ___, ___],
    [___, "2", "3", "4", ___],
    ["5", "6", "7", "8", "9"],
    [___, "A", "B", "C", ___],
    [___, ___, "D", ___, ___]
]

MOVES = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}


def get_next(move: str, x: int, y: int, keypad: list) -> int:

    n = len(keypad) - 1

    delta_x, delta_y = MOVES[move]
    new_x = x + delta_x
    new_y = y + delta_y

    if new_x < 0 or new_x > n:
        new_x = x

    if new_y < 0 or new_y > n:
        new_y = y

    if keypad[new_y][new_x]:
        return new_x, new_y

    return x, y


def solve(input: list, keypad: list, init: tuple) -> str:
    bathroom_code = ""

    x, y = init
    for line in input:
        for c in line:
            x, y = get_next(c, x, y, keypad)

        bathroom_code += keypad[y][x]

    return bathroom_code


input = read_input("input.txt")
ans1 = solve(input, KEYPAD1, (1, 1))
ans2 = solve(input, KEYPAD2, (0, 2))

ans = (ans1, ans2)
print(ans)
