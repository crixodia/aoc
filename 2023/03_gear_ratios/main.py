def read_input(file="input.txt"):
    schematic = []

    with open(file, "r") as f:
        for line in f:
            schematic.append(line.replace("\n", ""))

    return schematic


def get_number_cords(puzzle):
    coords = []
    for y, line in enumerate(puzzle):
        current_number = ""

        for x, c in enumerate(line):
            if c.isdigit():
                current_number += c

            elif current_number:
                coords.append(
                    {
                        "start": (x - len(current_number), y),
                        "end": (x - 1, y),
                        "value": int(current_number),
                    }
                )
                current_number = ""

        if current_number:
            coords.append(
                {
                    "start": (len(line) - len(current_number), y),
                    "end": (len(line), y),
                    "value": int(current_number),
                }
            )

    return coords


def convolution(coords, puzzle):
    x_0, y = coords["start"]
    x, _ = coords["end"]

    for j in range(y - 1, y + 2):
        if j < 0 or j >= len(puzzle):
            continue

        for i in range(x_0 - 1, x + 2):
            if i < 0 or i >= len(puzzle[j]):
                continue

            if puzzle[j][i] not in ("0123456789."):
                coords["gear"] = (j, i)
                return True

    return False


def solve(puzzle):
    S = 0

    coords = get_number_cords(puzzle)
    gears_candidate = dict()

    for coord in coords:
        if convolution(coord, puzzle):
            S += coord["value"]

        coord_gear = coord.get("gear")
        if coord_gear:
            if coord_gear in gears_candidate:
                gears_candidate[coord_gear].append(coord["value"])
            else:
                gears_candidate[coord_gear] = [coord["value"]]

    gears = filter(lambda x: len(x) == 2, gears_candidate.values())
    gear_ratios = map(lambda L: L[0] * L[1], gears)

    return S, sum(gear_ratios)


puzzle = read_input()
ans = solve(puzzle)
print(ans)
