def read_input(filename: str = "input.txt") -> list[int]:
    doc = open(filename, "r").readlines()
    return [-1 * int(x[1:]) if x[0] == "L" else int(x[1:]) for x in doc]


def solve(puzzle):
    dial_pos = 50
    zero_pointing = 0

    for ins in puzzle:
        _, dial_pos = divmod(dial_pos + ins, 100)

        if dial_pos == 0:
            zero_pointing += 1

    return zero_pointing


def solve2(puzzle):
    dial_pos = 50
    all_zero_pointing = 0

    for ins in puzzle:
        sign = -1 if ins < 0 else +1
        for _ in range(abs(ins)):
            dial_pos += sign * 1

            if dial_pos == 100:
                dial_pos = 0
            elif dial_pos == -1:
                dial_pos = 99

            if dial_pos == 0:
                all_zero_pointing += 1

    return all_zero_pointing


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
