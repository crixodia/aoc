from itertools import combinations


def read_input(file="input.txt"):
    image = []
    with open(file, "r") as f:
        for line in f:
            image.append(list(line.strip()))
    return image


def transpose(mat):
    rows, cols = len(mat), len(mat[0])
    T = [[None] * rows for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            T[j][i] = mat[i][j]
    return T


def get_galaxies(image):
    galaxies = []
    for i, row in enumerate(image):
        for j, col in enumerate(row):
            if image[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


def process_image(image):
    indices = []
    for i, row in enumerate(image):
        if row.count("#") == 0:
            indices.append(i)
    return indices


def scale_coords(component, indices, factor):
    passed_indices = 0
    for i, idx in enumerate(indices):
        if component > idx:
            passed_indices += 1
    added = 0 if factor <= 1 else passed_indices
    return component + (factor * passed_indices) - added


def solve(image, factor=0):
    iidx = process_image(image)
    jidx = process_image(transpose(image))

    galaxies = get_galaxies(image)
    pairs = combinations(galaxies, 2)
    distances = []
    for pair in pairs:
        a, b = pair

        ai, aj = a
        ai = scale_coords(ai, iidx, factor)
        aj = scale_coords(aj, jidx, factor)

        bi, bj = b
        bi = scale_coords(bi, iidx, factor)
        bj = scale_coords(bj, jidx, factor)

        dist = (abs(bi - ai), abs(bj - aj))
        distances.append(sum(dist))
    return sum(distances)


puzzle = read_input()

ans1 = solve(puzzle, 1)
ans2 = solve(puzzle, 1000000)
ans = (ans1, ans2)

print(ans)
