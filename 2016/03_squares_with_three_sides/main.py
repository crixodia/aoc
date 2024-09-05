def read_input(input_path: str) -> list:
    return list(
        map(
            lambda x: tuple(int(x.strip()) for x in x.split()),
            open(input_path, "r").read().splitlines()
        )
    )


def is_valid_triangle(x: tuple):
    a, b, c = x
    ab, ac, bc = a+b, a+c, b+c
    return ab > c and ac > b and bc > a


def transpose(lengths: list) -> list:
    rows, cols = len(lengths), len(lengths[0])
    M = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            M[j][i] = lengths[i][j]

    return M


def solve(lengths: list) -> int:
    return len(list(filter(is_valid_triangle, lengths)))


def solve2(lengths: list) -> int:
    row_a, row_b, row_c = transpose(lengths)
    T = row_a + row_b + row_c
    return solve([tuple(T[i:i+3]) for i in range(0, len(T), 3)])


puzzle_input = read_input("input.txt")
ans1 = solve(puzzle_input)
ans2 = solve2(puzzle_input)

ans = (ans1, ans2)
print(ans)
