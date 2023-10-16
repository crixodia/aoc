from collections import defaultdict
from itertools import permutations


def read_input(file):
    attendees = set()
    happiness = defaultdict(dict)

    with open(file, "r") as f:
        for line in f:
            s = line.replace("\n", "")
            s = s.replace(".", "")
            s = s.replace("would ", "")

            s = s.replace("happiness units by sitting next to ", "")

            name, gain, hap, next = s.split(" ")

            hap = int(hap) if gain == "gain" else -int(hap)
            attendees.add(name)
            happiness[name][next] = hap

    return attendees, happiness


def solve(pinput):
    attendees, happiness = pinput

    arrangements = list(permutations(attendees))
    total_happiness = []

    for arrang in arrangements:
        hap = 0

        A = list(arrang)
        A.append(A[0])

        for i in range(1, len(A)):
            hap += happiness[A[i - 1]][A[i]]
            hap += happiness[A[i]][A[i - 1]]

        total_happiness.append(hap)

    return max(total_happiness)


def solve2(pinput):
    attendees, happiness = pinput

    for name in attendees:
        happiness[name]["crixodia"] = 0
        happiness["crixodia"][name] = 0

    attendees.add("crixodia")

    new_pinput = (attendees, happiness)
    return solve(new_pinput)


puzzle_input = read_input("input.txt")
ans1 = solve(puzzle_input)
ans2 = solve2(puzzle_input)

ans = (ans1, ans2)
print(ans)
