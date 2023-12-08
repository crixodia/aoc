from functools import reduce


def read_input(file="input.txt"):
    dirs, inst = [], dict()
    with open(file, "r") as f:
        end = ""
        for line in f:
            if line.count("="):
                line = line.replace("\n", "").replace(" ", "")
                line = line.replace("(", "").replace(")", "")
                a, b = line.split("=")
                b = b.split(",")
                inst[a] = {"L": b[0], "R": b[1]}
            elif line == "\n":
                continue
            else:
                dirs = list(line.replace("\n", ""))

    return dirs, inst


def solve(dirs, inst, current_node="AAA", target_node="ZZZ"):
    steps = 0

    for d in dirs:
        if current_node == target_node:
            return steps

        steps += 1
        current_node = inst[current_node][d]

    return steps + solve(dirs, inst, current_node, target_node)


def get_end_nodes(inst, c):
    nodes = set(inst.keys())
    return list(filter(lambda node: node.endswith(c), nodes))


def get_max_steps(dirs, inst, start_list, end_list):
    steps = []
    for start in start_list:
        for end in end_list:
            try:
                steps.append(solve(dirs, inst, start, end))
            except RecursionError:
                pass
    return steps


def gcd(a, b):  # greatest common divisor
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):  # Integer least common multiple
    return (a * b) // gcd(a, b)


def solve2(dirs, inst):
    endsA = get_end_nodes(inst, "A")
    endsZ = get_end_nodes(inst, "Z")
    steps = get_max_steps(dirs, inst, endsA, endsZ)
    return reduce(lcm, steps)


dirs, inst = read_input()

ans1 = solve(dirs, inst)
ans2 = solve2(dirs, inst)
ans = (ans1, ans2)

print(ans)
