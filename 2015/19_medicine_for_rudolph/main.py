import re


def read_input(file="input.txt"):
    replace_rules = dict()
    molecule = ""

    with open(file, "r") as f:
        for line in f:
            row = line.replace("\n", "")
            row = row.replace(" ", "")

            if line.count("=>"):
                key, value = row.split("=>")

                if key in replace_rules:
                    replace_rules[key].append(value)
                else:
                    replace_rules[key] = [value]
            else:
                molecule = row

    return replace_rules, molecule


def solve(p_input):
    rules, molecule = p_input
    keys = rules.keys()
    new_molecules = set()

    for k in keys:
        idx = molecule.find(k)
        while idx != -1:
            part_a = molecule[:idx]
            part_b = molecule[idx + len(k) :]
            values = rules[k]

            for val in values:
                new_mol = part_a + val + part_b
                new_molecules.add(new_mol)

            idx = molecule.find(k, idx + 1)

    return new_molecules


# It could solve the problem but it is computationally expensive
def solve2_deprecated(p_input):
    rules, molecule = p_input

    mols = rules["e"]
    steps = 1

    while molecule not in mols:
        new_mols = []
        for i, mol in enumerate(mols):
            if len(mol) < len(molecule):
                new_p_input = (rules, mol)
                new_mols = new_mols + list(solve(new_p_input))
        mols = new_mols
        steps += 1

    return steps


# The second part was really difficult to solve
# so I had to take advantage from (I'll never overcome this 🥺):
# https://new.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju/
def solve2(p_input):
    rules, molecule = p_input

    molecule = molecule.replace("Rn", "(")
    molecule = molecule.replace("Ar", ")")
    molecule = molecule.replace("Y", ",")
    molecule = re.sub(r"[A-Z][a-z]|[A-Z]", "X", molecule)

    tokens = len(molecule)
    parenthesis = molecule.count("(") + molecule.count(")")
    commas = molecule.count(",")

    return tokens - parenthesis - 2 * commas - 1


puzzle_input = read_input()
ans1 = len(solve(puzzle_input))
ans2 = solve2(puzzle_input)

ans = (ans1, ans2)
print(ans)
