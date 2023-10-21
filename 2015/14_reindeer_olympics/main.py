from collections import defaultdict
import time


def read_input(file="input.txt"):
    reindeers = defaultdict(dict)
    with open(file, "r") as f:
        for line in f:
            row = line.replace(" can fly", "")
            row = row.replace(" km/s for", "")
            row = row.replace(" seconds, but then must rest for", "")
            row = row.replace(" seconds.", "")
            row = row.replace("\n", "")

            name, dist, fly, rest = row.split(" ")
            reindeers[name]["dst"] = int(dist)
            reindeers[name]["fly"] = int(fly)
            reindeers[name]["rst"] = int(rest)

    return reindeers


def next_state(seconds, fly, rest):
    n, last_seconds = divmod(seconds, fly + rest)
    if n % 2 != 0:  # resting
        n += 1
    return n, last_seconds


def draw(arr):
    m = len(set(arr))
    return m == 1


def solve(reindeers, seconds):
    distances = []
    for r in reindeers.values():
        n, ls = next_state(seconds, r["fly"], r["rst"])
        d = n * r["fly"] * r["dst"]
        distances.append(d)
    return max(distances)


def solve2(reindeers, seconds):
    for i in range(1, seconds + 1):
        names = list(reindeers.keys())
        for r in names:
            if i == 1:
                reindeers[r]["total_dst"] = 0
                reindeers[r]["state"] = "flying"
                reindeers[r]["count"] = 0
                reindeers[r]["score"] = 0

            if reindeers[r]["state"] == "flying":
                if reindeers[r]["count"] == reindeers[r]["fly"]:
                    reindeers[r]["count"] = 0
                    reindeers[r]["state"] = "resting"
            elif reindeers[r]["state"] == "resting":
                if reindeers[r]["count"] == reindeers[r]["rst"]:
                    reindeers[r]["count"] = 0
                    reindeers[r]["state"] = "flying"

            if reindeers[r]["state"] == "flying":
                reindeers[r]["total_dst"] += 1 * reindeers[r]["dst"]

            reindeers[r]["count"] += 1

        total_distances = []
        names = []
        for r in list(reindeers.keys()):
            total_distances.append(reindeers[r]["total_dst"])
            names.append(r)

        winners = []
        if not draw(total_distances):
            winner_val = max(total_distances)
            total_distances.index(winner_val)
            for j, d in enumerate(total_distances):
                if d == winner_val:
                    winners.append(names[j])

        # print(i, winners)
        # time.sleep(0.5)
        for win in winners:
            reindeers[win]["score"] += 1

    scores = []
    for r in list(reindeers.keys()):
        scores.append(reindeers[r]["score"])

    print(scores)
    return max(scores)


puzzle_input = read_input()
ans1 = solve(puzzle_input, 2503)
ans2 = solve2(puzzle_input, 2503)

ans = (ans1, ans2)
print(ans)
