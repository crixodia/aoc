from functools import lru_cache


def read_input(input_file="input.txt"):
    program = []
    registers = []
    is_program = False
    with open(input_file, "r") as f:
        for line in f.readlines():
            if line == "\n":
                is_program = True
                continue

            if is_program:
                program = [int(x) for x in line.replace("\n", "").split(":")[
                    1].strip().split(",")]

            else:
                registers.append(
                    int(line.replace("\n", "").split(":")[1].strip()))

    return registers, program


def get_combo(op_code, A, B, C):
    if 0 <= op_code <= 3:
        return op_code
    elif op_code == 4:
        return A
    elif op_code == 5:
        return B
    elif op_code == 6:
        return C


def solve(puzzle):
    registers, program = puzzle
    A, B, C = registers
    i = 0
    output = []
    while i < len(program):
        op_code = program[i+1]
        combo = get_combo(op_code, A, B, C)
        match(program[i]):
            case 0:
                A //= 2 ** combo
            case 1:
                B ^= op_code
            case 2:
                B = combo % 8
            case 3:
                if A != 0:
                    i = op_code
                    continue
            case 4:
                B ^= C
            case 5:
                output.append(str(combo % 8))
            case 6:
                B = A // 2 ** combo
            case 7:
                C = A // 2 ** combo

        i += 2

    return ",".join(output)


def reverse_program(i, program, current, A, B, C):
    if i == -1 or program == current:
        return current, A, B, C

    p = 5
    current_l = []
    for op_code in range(7):
        a, b, c = A, B, C
        if 0 <= op_code <= 3:
            pass
        elif op_code == 4:
            a, b, c = program[i], B, C
        elif open == 5:
            a, b, c = A, program[i], C
        else:
            a, b, c = A, B, program[i]

        new_current, a, b, c = reverse_program(i-1, program, current, a, b, c)
        current_l.append("".join([
            new_current,
            str(p),
            str(op_code)
        ]))

    return current, A, B, C


puzzle = read_input()
ans = (solve(puzzle), reverse_program(2, "505154", "", 10, 0, 0))
print(ans)
