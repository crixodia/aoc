def read_input(input_file="input.txt"):
    test_values = []
    equation = []

    lines = open(input_file, "r").readlines()

    for line in lines:
        test, eq = line.replace("\n", "").split(":")
        test = int(test)

        eq = [int(x) for x in eq.strip().split()]

        test_values.append(test)
        equation.append(eq)

    return test_values, equation


def binary_traversal(root, values, target):
    if values == [] and root == target:
        return True

    if values == []:
        return False

    new_values = values.copy()

    next_value = new_values.pop(0)

    add_value = root + next_value
    mul_value = root * next_value

    return any([
        binary_traversal(add_value, new_values, target),
        binary_traversal(mul_value, new_values, target)
    ])


def ternary_traversal(root, values, target):
    if values == [] and root == target:
        return True

    if values == []:
        return False

    new_values = values.copy()

    next_value = new_values.pop(0)

    add_value = root + next_value
    mul_value = root * next_value
    con_value = int(str(root) + str(next_value))

    return any([
        ternary_traversal(add_value, new_values, target),
        ternary_traversal(mul_value, new_values, target),
        ternary_traversal(con_value, new_values, target),
    ])


def solve(puzzle):
    test_values, equations = puzzle

    binary_tcr = 0
    ternary_tcr = 0
    for i, tv in enumerate(test_values):
        root = equations[i].pop(0)
        if binary_traversal(root, equations[i], tv):
            binary_tcr += tv

        if ternary_traversal(root, equations[i], tv):
            ternary_tcr += tv

    return binary_tcr, ternary_tcr


puzzle = read_input()
ans = solve(puzzle)
print(ans)
