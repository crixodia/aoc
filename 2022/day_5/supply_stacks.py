
from copy import deepcopy
crates = []
moves = []  # Quantity, From, To


def transpose(matrix):
    row, col = len(matrix), len(matrix[0])
    t = [[0]*row for i in range(col)]
    for i in range(col):
        for j in range(row):
            t[i][j] = matrix[j][i]
    return t


with open("input.txt") as f:
    for line in f:
        L = line.replace("\n", "")
        if not L.startswith("move") and L != "":
            L = L.replace("    ", "[_]")
            L = L.replace(" ", "")
            L = L.split("]")
            L = [s.replace("[", "") for s in L[:-1]]
            if L != []:
                crates.append(L)

        elif L.startswith("move"):
            L = L.split(" ")
            T = []
            for el in L:
                if el not in ["move", "from", "to"]:
                    T.append(int(el))
            moves.append(T)

crates = transpose(crates)

for i, crate in enumerate(crates):
    crate = [c for c in crate if c != "_"]
    crates[i] = crate[::-1]

crates2 = deepcopy(crates)

for move in moves:
    Q, F, T = move
    aux_row = []
    
    for i in range(Q):
        crates[T-1].append(crates[F-1].pop())
        aux_row.append(crates2[F-1].pop())

    crates2[T-1] = crates2[T-1] + aux_row[::-1]

# Part One
ctos="".join([c.pop() for c in crates])
print(f"Crates on top of stack: {ctos}")

# Part Two
ctos="".join([c.pop() for c in crates2])
print(f"Crates on top of stack (moving chunks): {ctos}")
