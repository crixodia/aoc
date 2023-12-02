def read_input(file="input.txt"):
    games = dict()
    with open(file, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            game, values = line.split(":")
            game = game.split(" ")

            values = values.split(";")
            values = [x.split(",") for x in values]

            games[int(game[1])] = []
            for val in values:
                D = dict()
                for record in val:
                    record = record.split(" ")
                    D[record[2]] = int(record[1])
                games[int(game[1])].append(D)
    return games


def is_valid_game(gt, bag):
    return all(
        [
            gt.get("red", 0) <= bag["red"],
            gt.get("green", 0) <= bag["green"],
            gt.get("blue", 0) <= bag["blue"],
        ]
    )


def solve(records, bag):
    S = 0
    for k, v in records.items():
        flag = True
        for r in v:
            if not is_valid_game(r, bag):
                flag = False
        if flag:
            S += k
    return S


def min_bag_game(game):
    R, G, B = [], [], []
    for g in game:
        R.append(g.get("red", 0))
        G.append(g.get("green", 0))
        B.append(g.get("blue", 0))

    return {"red": max(R), "green": max(G), "blue": max(B)}


def get_power(bag):
    return bag["red"] * bag["green"] * bag["blue"]


def solve2(records):
    min_bags = map(min_bag_game, records.values())
    powers = map(get_power, min_bags)

    return sum(powers)


puzzle = read_input()

ans1 = solve(puzzle, {"red": 12, "green": 13, "blue": 14})
ans2 = solve2(puzzle)
ans = (ans1, ans2)

print(ans)
