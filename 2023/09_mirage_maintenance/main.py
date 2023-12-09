def read_input(file="input.txt"):
    report = []
    with open(file, "r") as f:
        for line in f:
            line = line.replace("\n", "").split(" ")
            report.append([int(c) for c in line])

    return report


def get_diffs(numbers):
    diffs = [numbers[0]]

    current_seed = [i for i in numbers]
    while not all([x == 0 for x in current_seed]):
        new_seed = []
        for i in range(1, len(current_seed)):
            new_seed.append(current_seed[i] - current_seed[i - 1])

        current_seed = new_seed
        diffs.append(new_seed[0])

    return diffs


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def next_value(diffs, n):
    m = len(diffs)
    S = 0
    for i in range(len(diffs)):
        P = 1
        for j in range(1, i + 1):
            P = P * (n - j)

        S = S + P * diffs[i] // factorial(i)
    return S


def solve(puzzle):
    S, E = 0, 0
    for line in puzzle:
        diffs = get_diffs(line)
        n = len(line)
        S = S + next_value(diffs, n + 1)

        # Part 2
        E = E + next_value(diffs, 0)
    return S, E


puzzle = read_input()
ans = solve(puzzle)
print(ans)
