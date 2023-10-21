from collections import defaultdict
from itertools import product


def read_input(file="input.txt"):
    ingredients = defaultdict(dict)
    with open(file, "r") as f:
        for line in f:
            row = line.replace("\n", "")
            row = row.replace(": capacity ", ",")
            row = row.replace(" durability ", "")
            row = row.replace(" flavor ", "")
            row = row.replace(" texture ", "")
            row = row.replace(" calories ", "")

            ing, cap, dur, fla, tex, cal = row.split(",")
            ingredients[ing]["capacity"] = int(cap)
            ingredients[ing]["durability"] = int(dur)
            ingredients[ing]["flavor"] = int(fla)
            ingredients[ing]["texture"] = int(tex)
            ingredients[ing]["calories"] = int(cal)

    return ingredients


def get_score(ingredients, weights):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0

    for i, ing in enumerate(list(ingredients.keys())):
        capacity += weights[i] * ingredients[ing]["capacity"]
        durability += weights[i] * ingredients[ing]["durability"]
        flavor += weights[i] * ingredients[ing]["flavor"]
        texture += weights[i] * ingredients[ing]["texture"]

    score = capacity * durability * flavor * texture
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0

    return score


def get_calories(ingredients, weights):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for i, ing in enumerate(list(ingredients.keys())):
        capacity += weights[i] * ingredients[ing]["capacity"]
        durability += weights[i] * ingredients[ing]["durability"]
        flavor += weights[i] * ingredients[ing]["flavor"]
        texture += weights[i] * ingredients[ing]["texture"]
        calories += weights[i] * ingredients[ing]["calories"]

    score = capacity * durability * flavor * texture
    if min([capacity, durability, flavor, texture]) < 0:
        score = 0

    return calories, score


def solve(pinput):
    n = len(pinput.keys())
    pos = filter(lambda x: sum(x) == 100, product(range(0, 101), repeat=n))
    scores = [get_score(pinput, p) for p in pos]
    return max(scores)


def solve2(pinput, max_cal=None):
    n = len(pinput.keys())
    pos = filter(lambda x: sum(x) == 100, product(range(0, 101), repeat=n))
    scores = [get_calories(pinput, p) for p in pos]
    scores = filter(lambda x: x[0] == max_cal and x[1] != 0, scores)
    scores = [x[1] for x in scores]
    return max(scores)


puzzle_input = read_input()
ans1 = solve(puzzle_input)
ans2 = solve2(puzzle_input, 500)

ans = (ans1, ans2)
print(ans)
