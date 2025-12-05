def read_input(filename: str = "input.txt"):
    data = [s.replace("\n", "") for s in open(filename, "r").readlines()]
    break_idx = data.index("")

    ingredient_range = [s.split("-") for s in data[:break_idx]]
    ingredient_range = [(int(x), int(y)) for x, y in ingredient_range]

    ingredient_ids = [int(s) for s in data[break_idx+1:]]

    return ingredient_range, ingredient_ids


def is_in_range(val: int, r: tuple) -> bool:
    return r[0] <= val <= r[1]


def solve(puzzle):
    irs, iids = puzzle
    fresh_ingredients = 0

    for id in iids:
        for r in irs:
            if is_in_range(id, r):
                fresh_ingredients += 1
                break

    return fresh_ingredients


def solve2_high_memory(puzzle):  # DEPRECATED
    irs, _ = puzzle

    all_ids = set()
    for r in irs:
        all_ids = all_ids.union(set(range(r[0], r[1] + 1)))

    print(all_ids)
    return len(all_ids)


def are_intersected(A, B):
    return is_in_range(A[1], B)


def solve2(puzzle):
    irs, _ = puzzle

    i = 0
    while i < len(irs):
        A = irs[i]
        j = i + 1
        while j < len(irs):
            B = irs[j]
            if are_intersected(A, B) or are_intersected(B, A) and i != j:
                min_merge = min(A + B)
                max_merge = max(A + B)
                # print("Comparing", A, B, (min_merge, max_merge))
                irs.pop(j)
                irs.pop(i)
                i -= 1
                irs.append((min_merge, max_merge))
                break
            j += 1
        i += 1
    return sum([x[1] - x[0] + 1 for x in irs])


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
