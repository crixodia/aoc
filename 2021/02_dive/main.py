def read_input(input_path: str) -> list:
    lines = open(input_path, "r").read().splitlines()
    instructions, steps = [], []
    for line in lines:
        ins, step = line.split()
        instructions.append(ins)
        steps.append(int(step))

    return instructions, steps


def solve(instructions: list, steps: list) -> int:
    horizontal, depth = 0, 0

    for i in range(len(instructions)):
        match(instructions[i]):
            case "forward":
                horizontal += steps[i]
            case "down":
                depth += steps[i]

            case "up":
                depth -= steps[i]

    return horizontal * depth


def solve2(instructions: list, steps: list) -> int:
    horizontal, depth, aim = 0, 0, 0

    for i in range(len(instructions)):
        match(instructions[i]):
            case "forward":
                horizontal += steps[i]
                depth += aim * steps[i]

            case "down":
                aim += steps[i]

            case "up":
                aim -= steps[i]

    return horizontal * depth


puzzle_input = read_input("input.txt")
ans1 = solve(*puzzle_input)
ans2 = solve2(*puzzle_input)

ans = (ans1, ans2)
print(ans)
