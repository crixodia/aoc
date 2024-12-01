from collections import Counter


def read_input(input_file="input.txt"):
    locations_a = []
    locations_b = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.replace("   ", " ")

            A, B = line.split()
            A, B = int(A), int(B)

            locations_a.append(A)
            locations_b.append(B)

    return locations_a, locations_b


def solve(puzzle):
    LA, LB = puzzle

    LA.sort()
    LB.sort()

    distances = []
    for i in range(len(LA)):
        distances.append(abs(LA[i] - LB[i]))

    return sum(distances)


def solve2(puzzle):
    # It doesn't matter that the arrays are sorted
    LA, LB = puzzle

    counter_lb = Counter(LB)
    similarity = []

    for i in range(len(LA)):
        similarity.append(counter_lb.get(LA[i], 0)*LA[i])

    return sum(similarity)


puzzle = read_input()

ans = (solve(puzzle), solve2(puzzle))
print(ans)
