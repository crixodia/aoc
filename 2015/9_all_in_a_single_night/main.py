from itertools import permutations
from collections import defaultdict


def read_input(file):
    cities = set()
    weights = defaultdict(dict)
    with open(file, "r") as f:
        for line in f:
            row = line.replace("\n", "")
            row = row.replace(" ", "")

            C, w = row.split("=")
            ca, cb = C.split("to")

            cities.add(ca)
            cities.add(cb)

            weights[ca][cb] = int(w)
            weights[cb][ca] = int(w)
    return cities, weights


def solve(input):
    cities, weights = input
    possible_paths = list(permutations(cities, len(cities)))
    distances = []
    for path in possible_paths:
        d = 0
        i = 0
        for j in range(1, len(path)):
            w = weights[path[i]][path[j]]
            d += w
            i += 1
        distances.append(d)
    return min(distances), max(distances)


input = read_input("input.txt")
ans = solve(input)
print(ans)
