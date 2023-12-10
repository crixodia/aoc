from time import sleep


def read_input(file="input.txt"):
    instructions = []
    with open(file, "r") as f:
        for line in f:
            instructions.append(line.replace("\n", ""))
    return instructions


def evaluate(ins, param, A, B):
    match ins:
        case "hlf":
            if param == "a":
                A = A // 2
            else:
                B = B // 2
        case "tpl":
            if param == "a":
                A = 3 * A
            else:
                B = 3 * B
        case "inc":
            if param == "a":
                A += 1
            else:
                B += 1
    return A, B


def solve(instructions, a=0, b=0):
    i = 0
    ins_count = len(instructions)
    while i < ins_count:
        if instructions[i].count(","):
            ins, param = instructions[i].replace(", ", ",").split()
        else:
            ins, param = instructions[i].split()
        match ins:
            case "jmp":
                i += int(param) - 1
            case "jie":
                r, val = param.split(",")
                r = a if r == "a" else b
                if r % 2 == 0:
                    i += int(val) - 1
            case "jio":
                r, val = param.split(",")
                r = a if r == "a" else b
                if r == 1:
                    i += int(val) - 1
            case _:
                a, b = evaluate(ins, param, a, b)
        i += 1

    return b


puzzle = read_input()

ans1 = solve(puzzle)
ans2 = solve(puzzle, 1)
ans = (ans1, ans2)

print(ans)
