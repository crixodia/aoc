import json


def read_input(file):
    f = open(file, "r")
    return json.load(f)


def solve(doc):
    count = 0
    if isinstance(doc, int):
        count += doc
    elif isinstance(doc, dict):
        values = list(doc.values())
        count += solve(values)
    elif isinstance(doc, list):
        for el in doc:
            count += solve(el)
    return count


def solve2(doc):
    count = 0
    if isinstance(doc, int):
        count += doc
    elif isinstance(doc, dict):
        values = list(doc.values())
        if "red" in values:
            return 0
        count += solve2(values)
    elif isinstance(doc, list):
        for el in doc:
            count += solve2(el)
    return count


puzzle_input = read_input("input.json")
ans1 = solve(puzzle_input)
ans2 = solve2(puzzle_input)

ans = (ans1, ans2)
print(ans)
