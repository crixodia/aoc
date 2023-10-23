from itertools import combinations


def read_input(file="input.txt"):
    containers = []
    with open(file, "r") as f:
        for line in f:
            containers.append(int(line.replace("\n", "")))

    return containers


def solve(p_input, litters):
    n = len(p_input)
    all = []
    for i in range(1, n + 1):
        current = combinations(p_input, i)
        current = filter(lambda x: sum(x) == litters, current)
        all = all + list(current)

    return len(all), all


def solve2(all_comb):
    min_len = min(map(len, all_comb))
    min_con = filter(lambda x: len(x) == min_len, all_comb)
    
    return len(list(min_con))


puzzle_input = read_input()
ans1, all = solve(puzzle_input, 150)
ans2 = solve2(all)

ans = (ans1, ans2)
print(ans)
