from pprint import pprint


def read_input(input_file="input.txt"):
    lines = open(input_file, "r").readlines()
    return [list(x.replace("\n", "")) for x in lines]


def get_diag_indices(i, j, size, only_diag=False):
    d1 = [(i, j)]
    d2 = [(i, j)]
    d3 = [(i, j)]
    d4 = [(i, j)]
    up = [(i, j)]
    do = [(i, j)]
    le = [(i, j)]
    ri = [(i, j)]

    for x in range(1, size):
        d1.append((i-x, j-x))
        d2.append((i+x, j-x))
        d3.append((i-x, j+x))
        d4.append((i+x, j+x))
        up.append((i, j-x))
        do.append((i, j+x))
        le.append((i-x, j))
        ri.append((i+x, j))

    if only_diag:
        return (d1, d2, d3, d4)

    return (d1, d2, d3, d4, up, do, le, ri)


def solve(puzzle, criteria="XMAS"):
    rows, cols = len(puzzle), len(puzzle[0])
    find = 0
    for i in range(rows):
        for j in range(cols):
            available = get_diag_indices(i, j, len(criteria))
            for word_idx in available:
                word = ""
                for p, q in word_idx:
                    if p < 0 or q < 0:
                        continue
                    try:
                        word = word + puzzle[p][q]
                    except:
                        continue

                if word == criteria:
                    find += 1
    return find


def solve2(puzzle):
    rows, cols = len(puzzle), len(puzzle[0])
    find = 0
    for i in range(rows):
        for j in range(cols):
            if puzzle[i][j] != "A":
                continue

            d1 = [(i-1, j-1), (i, j), (i+1, j+1)]
            d2 = [(i-1, j+1), (i, j), (i+1, j-1)]

            word1 = []
            word2 = []

            for k in range(3):
                if d1[k][0] < 0 or d1[k][1] < 0:
                    continue

                if d2[k][0] < 0 or d2[k][1] < 0:
                    continue
                try:
                    word1.append(puzzle[d1[k][0]][d1[k][1]])
                    word2.append(puzzle[d2[k][0]][d2[k][1]])
                except:
                    continue

            if sorted(word1) == sorted("MAS") == sorted(word2):
                find += 1

    return find


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
