import operator


def read_input(file: str) -> str:
    s = ''
    with open(file, 'r') as f:
        s = f.readline()
    return s


def solve(instructions: str) -> int:
    current = (0, 0)
    positions = [current]
    moves = {'>': (1, 0), 'v': (0, -1), '<': (-1, 0), '^': (0, 1)}
    for c in instructions:
        current = tuple(map(operator.add, moves[c], current))
        if current not in positions:
            positions.append(current)

    return len(positions)


def split_instructions(instructions: str) -> list[str]:
    return [instructions[::2], instructions[1::2]]


def solve_2(instructions_s: list[str]) -> int:
    current = (0, 0)
    positions = [current]
    moves = {'>': (1, 0), 'v': (0, -1), '<': (-1, 0), '^': (0, 1)}
    for instructions in instructions_s:
        current = (0, 0)
        for c in instructions:
            current = tuple(map(operator.add, moves[c], current))
            if current not in positions:
                positions.append(current)

    return len(positions)


print(solve('>'), solve_2(split_instructions('>')))
print(solve('^>v<'), solve_2(split_instructions('^>v<')))
print(solve('^v^v^v^v^v'), solve_2(split_instructions('^v^v^v^v^v')))
print(solve('^v'), solve_2(split_instructions('^v')))

print(
    solve(read_input('input.txt')),
    solve_2(split_instructions(read_input('input.txt')))
)
