def read_input(input_file="input.txt"):
    return [[int(y) for y in list(x.replace("\n", ""))] for x in open(input_file, "r").readlines()]


def get_trailheads(topographic_map) -> set:

    rows, cols = len(topographic_map), len(topographic_map[0])

    trailheads = set()

    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:
                trailheads.add((i, j))

    return trailheads


def get_score(dir, topographic_map, visited=[], trails_number=False) -> int:

    i, j = dir

    if topographic_map[i][j] == 9 and (i, j) not in visited and not trails_number:
        visited.append((i, j))
        return 1
    elif topographic_map[i][j] == 9 and trails_number:
        return 1

    rows, cols = len(topographic_map), len(topographic_map[0])

    available_dirs = [
        (i-1, j),  # Up
        (i+1, j),  # Down
        (i, j-1),  # Left
        (i, j+1),  # Right
    ]

    score = 0
    for ad in available_dirs:
        x, y = ad
        if not (0 <= x < rows and 0 <= y < cols):
            continue

        if topographic_map[x][y] == topographic_map[i][j] + 1:
            score += get_score(ad, topographic_map, visited, trails_number)

    return score


def solve(puzzle, trails_number=False):
    trailheads = get_trailheads(puzzle)
    scores_sum = 0

    for th in trailheads:
        scores_sum += get_score(th, puzzle, [], trails_number)

    return scores_sum


puzzle = read_input()
ans = (solve(puzzle), solve(puzzle, True))
print(ans)
