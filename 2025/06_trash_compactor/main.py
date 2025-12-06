def read_input(filename: str = "input.txt"):
    sheet = []
    with open(filename, "r") as f:
        for line in f:
            row = line.replace("\n", "").split(" ")
            while "" in row:
                row.pop(row.index(""))

            row = [int(x) if x not in ["*", "+"] else x for x in row]
            sheet.append(row)

    return sheet


def read_input2(mask, filename: str = "input.txt"):
    sheet = []
    with open(filename, "r") as f:
        for line in f:
            row = line.replace("\n", "")
            new_row = []
            for sidx, eidx in mask:
                new_row.append(
                    row[sidx:eidx]
                    if row[sidx:eidx].replace(" ", "") not in ["+", "*"]
                    else row[sidx:eidx].replace(" ", "")
                )

            sheet.append(new_row)

    return sheet


def transpose(M):
    rows, cols = len(M), len(M[0])
    T = [[None] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            T[j][i] = M[i][j]

    return T


def mul(numbers: list[int | float]) -> int | float:
    m = 1
    for n in numbers:
        m *= n

    return m


def solve(puzzle):
    T = transpose(puzzle)
    grand_total = 0

    mask = []
    last_idx = 0

    for problem in T:

        numbers, op = problem[:-1], problem[-1]
        grand_total += mul(numbers) if op == "*" else sum(numbers)

        current_idx = max(map(lambda x: len(str(x)), numbers))
        mask.append((last_idx, last_idx + current_idx))
        last_idx += current_idx + 1

    return grand_total, mask


def solve2(puzzle):
    T = transpose(puzzle)
    grand_total = 0

    for problem in T:
        numbers, op = problem[:-1], problem[-1]

        numbers = [
            int("".join(x).replace(" ", ""))
            for x in transpose(
                [list(x) for x in numbers]
            )
        ]

        grand_total += mul(numbers) if op == "*" else sum(numbers)

    return grand_total


puzzle = read_input()
ans1, mask = solve(puzzle)

puzzle2 = read_input2(mask)
ans2 = solve2(puzzle2)

ans = (ans1, ans2)
print(ans)
