import re


def read_input(input_file="input.txt"):
    lex = re.compile(r"\d+")
    claws = []
    current_claw = dict()
    with open(input_file, "r") as f:
        for l in f.readlines():
            if l == "\n":
                continue

            x, y = re.findall(lex, l)
            x, y = int(x), int(y)

            if l.startswith("Button A:"):
                current_claw["A"] = (x, y)
            elif l.startswith("Button B"):
                current_claw["B"] = (x, y)
            else:
                current_claw["P"] = (x, y)
                claws.append(current_claw)
                current_claw = dict()
    return claws


def solve(puzzle, offset=0):
    sum_tokens = 0
    for claw in puzzle:
        Ax, Ay = claw["A"]
        Bx, By = claw["B"]
        Px, Py = claw["P"]

        Px += offset
        Py += offset

        b = round((Ax*Py - Ay*Px)/(By*Ax-Ay*Bx), 2)
        a = round((Px - b*Bx) / Ax, 2)

        if str(a).split(".")[1] != "0" or str(b).split(".")[1] != "0":
            continue

        sum_tokens += 3*a + b

    return int(sum_tokens)


puzzle = read_input()
ans = (solve(puzzle), solve(puzzle, 10000000000000))
print(ans)
