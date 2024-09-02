def read_input(input_path: str) -> list:
    return list(
        map(
            int,
            open(input_path, "r").read().splitlines()
        )
    )


def solve(measurements: list) -> int:

    increases = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            increases += 1

    return increases


def solve2(measurements: list) -> int:

    increases = 0
    for i in range(1, len(measurements)):
        last_sum = sum(measurements[i-1:i+2])
        new_sum = sum(measurements[i:i+3])

        if last_sum < new_sum:
            increases += 1

    return increases


puzzle_input = read_input("input.txt")
ans1 = solve(puzzle_input)
ans2 = solve2(puzzle_input)

ans = (ans1, ans2)
print(ans)
