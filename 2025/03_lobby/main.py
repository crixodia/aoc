def read_input(filename: str = "input.txt") -> list:
    return [s.replace("\n", "") for s in open(filename, "r").readlines()]


def solve(puzzle):  # DEPRECATED
    total_joltage = 0
    for bank in puzzle:
        bank_integers = [int(c) for c in bank]

        first_max = max(bank_integers[:-1])
        first_max_idx = bank_integers.index(first_max)

        bank_integers = bank_integers[first_max_idx+1:]
        second_max = max(bank_integers)

        total_joltage += first_max * 10 + second_max

    return total_joltage


def solve2(puzzle, num_batteries=12):
    total_joltage = 0
    for bank in puzzle:
        bank_integers = [int(c) for c in bank]

        current_joltage = 0

        for i in range(num_batteries):
            index_limit = num_batteries - i - 1

            current_max = max(
                bank_integers[:-index_limit]
                if index_limit > 0 else
                bank_integers
            )

            current_max_id = bank_integers.index(current_max)
            current_joltage += current_max * (10 ** index_limit)

            bank_integers = bank_integers[current_max_id + 1:]

        total_joltage += current_joltage

    return total_joltage


puzzle = read_input()
ans = (solve2(puzzle, num_batteries=2), solve2(puzzle, num_batteries=12))
print(ans)
