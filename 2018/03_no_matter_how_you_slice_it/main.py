import re


def read_input(input_path: str) -> list:
    claims = open(input_path, "r").readlines()
    return list(
        map(
            lambda x: tuple(
                map(
                    lambda y: int(y.strip()),
                    re.split(r"@|:|,|x", x.replace("#", ""))
                )
            ), claims)
    )


def get_max_size(claims: list) -> tuple:

    max_x, max_y = -1, -1
    for _, x, y, w, h in claims:
        max_x = max(x+w, max_x)
        max_y = max(y+h, max_y)

    return max_x, max_y


def solve(claims: list) -> int:
    count_overlap = 0
    n = max(get_max_size(claims))

    fabric = [[0] * n for _ in range(n)]
    claim_ids = {c[0]: False for c in claims}

    for id, x, y, w, h in claims:
        for i in range(x, x + w):
            for j in range(y, y + h):

                if fabric[i][j] == 0:
                    fabric[i][j] = id

                elif fabric[i][j] != -1:

                    claim_ids[id] = True
                    claim_ids[fabric[i][j]] = True

                    fabric[i][j] = -1
                    count_overlap += 1
                else:
                    claim_ids[id] = True
                    claim_ids[fabric[i][j]] = True

    ID = next(filter(lambda x: x[1] == False, claim_ids.items()))[0]
    return count_overlap, ID


puzzle_input = read_input("input.txt")
ans = solve(puzzle_input)

print(ans)
