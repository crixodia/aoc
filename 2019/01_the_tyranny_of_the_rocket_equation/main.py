def read_input(input_path: str) -> list:
    lines = open(input_path).read().split("\n")
    return [int(x) for x in lines]


def solve(input: list) -> int:
    return list(map(lambda x: max((x//3) - 2, 0), input))


def solve2(input: list) -> int:
    fuel_requirements = solve(input)
    total_fuel = sum(fuel_requirements)

    while any(map(lambda x: x > 2, fuel_requirements)):
        fuel_requirements = solve(fuel_requirements)
        total_fuel += sum(fuel_requirements)

    return total_fuel


input = read_input("input.txt")
ans1 = sum(solve(input))
ans2 = solve2(input)

ans = (ans1, ans2)
print(ans)
