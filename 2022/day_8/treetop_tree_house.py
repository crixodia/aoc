import numpy as np
M = []

with open("input.txt") as f:
    for line in f:
        L = list(line.replace("\n", ""))
        M.append([int(c) for c in L])


def get_scenic_score(A, reversed=False):
    if reversed:
        A = A[::-1]

    A = list(A)
    if True in A:
        return A.index(True) + 1

    return len(A)


def count_visible(M):
    M = np.array(M)
    n_row = len(M)
    n_col = len(M[0])
    C = 0
    scenic_score = -1
    for i in range(1, n_row - 1):
        for j in range(1, n_col - 1):
            # Is not visible
            L = M[i, :j] >= M[i, j]
            R = M[i, j+1:] >= M[i, j]
            T = M[:i, j] >= M[i, j]
            B = M[i+1:, j] >= M[i, j]

            # If there is a visible side, count it
            if not (True in L and True in R and True in T and True in B):
                C += 1

            score = get_scenic_score(L, True)
            score *= get_scenic_score(T, True)
            score *= get_scenic_score(R)
            score *= get_scenic_score(B)

            scenic_score = max(scenic_score, score)

    return C + n_row * 2 + (n_col-2)*2, scenic_score


# Part One
print(f"{count_visible(M)[0]} trees are visible from outside the grid")

# Part Two
print(f"{count_visible(M)[1]} is the highest scenic score")
