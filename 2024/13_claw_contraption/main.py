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


def scale_vect(alpha, vetc):
    new_vect = []
    for el in vetc:
        new_vect.append(alpha * el)

    return tuple(new_vect)


puzzle = read_input()
print(puzzle)
