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
        print(i, A, B, C, output, program[i])
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

    print(A, B, C)
    return "".join(output)


puzzle = read_input()
ans = (solve(puzzle), )
print(ans)
