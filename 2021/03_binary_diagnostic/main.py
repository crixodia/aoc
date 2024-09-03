def read_input(input_path: str) -> list:
    return open(input_path, "r").read().splitlines()


def solve(binary_records: list) -> tuple:
    n = len(binary_records[0])

    zeros = [0] * n
    ones = [0] * n

    for record in binary_records:
        for i in range(n):
            if record[i] == "0":
                zeros[i] += 1
            else:
                ones[i] += 1

    most_common = ["1" if zeros[i] <= ones[i] else "0" for i in range(n)]
    least_common = ["0" if zeros[i] <= ones[i] else "1" for i in range(n)]

    return "".join(most_common), "".join(least_common)


def solve2(binary_records: list) -> tuple:
    n = len(binary_records[0])

    oxygen_generation_rate = binary_records.copy()
    co2_scrubber_rate = binary_records.copy()

    for i in range(n):
        most_common = solve(oxygen_generation_rate)[0]
        least_common = solve(co2_scrubber_rate)[1]

        if len(oxygen_generation_rate) > 1:
            oxygen_generation_rate = list(
                filter(
                    lambda x: x[i] == most_common[i],
                    oxygen_generation_rate
                )
            )

        if len(co2_scrubber_rate) > 1:
            co2_scrubber_rate = list(
                filter(
                    lambda x: x[i] == least_common[i],
                    co2_scrubber_rate
                )
            )

    return "".join(oxygen_generation_rate), "".join(co2_scrubber_rate)


puzzle_input = read_input("input.txt")

gamma_rate, epsilon_rate = solve(puzzle_input)
oxygen_generation_rate, co2_scrubber_rate = solve2(puzzle_input)

ans1 = int(gamma_rate, 2) * int(epsilon_rate, 2)
ans2 = int(oxygen_generation_rate, 2) * int(co2_scrubber_rate, 2)

ans = (ans1, ans2)
print(ans)
