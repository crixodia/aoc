from collections import Counter


def read_input(input_file: str = "input.txt") -> list:
    rows = open(input_file, "r").readlines()
    return list(map(lambda x: list(x.replace("\n", "")), rows))


def transpose(A: list) -> list:
    m, n = len(A), len(A[0])
    T = [[""]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            T[j][i] = A[i][j]

    return T


def most_least_common(L: list):
    C = Counter(L)
    mc, lc, mcv, lcv = "", "", -1, len(L)
    for k, v in C.items():
        if v > mcv:
            mcv = v
            mc = k

        if v < lcv:
            lcv = v
            lc = k
    return [mc, lc]


def solve(puzzle: list) -> str:
    t_messages = transpose(puzzle)

    mlc = list(map(most_least_common, t_messages))
    t_mlc = transpose(mlc)

    mc_message = "".join(t_mlc[0])
    lc_message = "".join(t_mlc[1])

    return mc_message, lc_message


puzzle = read_input()
ans = solve(puzzle)
print(ans)
