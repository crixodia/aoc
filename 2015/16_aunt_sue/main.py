from pprint import pprint

MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def read_input(file: str = "input.txt") -> dict:
    sues = []

    with open(file, "r") as f:
        for line in f:
            l = line.replace(":", ",")
            l = l.replace("\n", "")
            l = l.replace(" ", "")
            l = l.split(",")

            id = int(l[0].replace("Sue", ""))
            sues.append({"id": id})

            for i in range(1, len(l), 2):
                sues[-1][l[i]] = int(l[i + 1])
    return sues


def solve(aunts: list[dict]) -> int:
    for aunt in aunts:
        match = True

        for key, val in aunt.items():
            if key == "id":
                continue

            if val != MFCSAM.get(key):
                match = False
                break

        if match:
            return aunt["id"]

    return -1


def solve2(aunts: list[dict]) -> int:
    for aunt in aunts:
        match = True
        for key, val in aunt.items():
            if key == "id":
                continue

            if key in ["cats", "trees"]:
                if val <= MFCSAM.get(key):
                    match = False
                    break
                continue

            if key in ["pomeranians", "goldfish"]:
                if val >= MFCSAM.get(key):
                    match = False
                    break
                continue

            if val != MFCSAM.get(key):
                match = False
                break

        if match:
            return aunt["id"]

    return -1


aunts = read_input()

ans1 = solve(aunts)
ans2 = solve2(aunts)
ans = (ans1, ans2)

print(ans)
