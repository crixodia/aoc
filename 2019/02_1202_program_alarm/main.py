import operator

OPERATIONS = {
    1: operator.add,
    2: operator.mul,
}


def read_input(input_path: str) -> list:
    values = open(input_path, "r").read().split(",")
    missing = [0]*(4-(len(values) % 4))
    return list(map(int, values)) + missing


def solve(instructions: list, x: int, y: int) -> int:
    instructions[1] = x
    instructions[2] = y

    for i in range(0, len(instructions), 4):
        op, var_a, var_b, var_o = instructions[i:i+4]

        if op == 99:
            break

        apply_operation = OPERATIONS[op]

        instructions[var_o] = apply_operation(
            instructions[var_a],
            instructions[var_b]
        )

    return instructions[0]


def solve2(instructions: list, target: int) -> int:
    n = len(instructions)
    for x in range(n):
        for y in range(n):
            I = [x for x in instructions]
            output = solve(I, x, y)

            if output == target:
                return 100 * x + y


puzzle_input = read_input("input.txt")
ans1 = solve(puzzle_input, 12, 2)

puzzle_input = read_input("input.txt")
ans2 = solve2(puzzle_input, 19690720)

ans = (ans1, ans2)
print(ans)
