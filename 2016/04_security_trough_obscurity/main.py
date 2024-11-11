from collections import Counter


def read_input(input_file: str = "input.txt") -> list:
    rooms = []
    ids = []
    checksums = []
    with open(input_file, "r") as f:
        for l in f.readlines():
            l = l.replace("\n", "")
            chars = l.split("-")

            R, idchk = chars[:-1], chars[-1]
            id, chk = idchk.split("[")
            chk = chk.replace("]", "")

            rooms.append(R)
            ids.append(int(id))
            checksums.append(chk)
    return rooms, ids, checksums


def swap(K, V, i, j):
    V[i], V[j] = V[j], V[i]
    K[i], K[j] = K[j], K[i]


def get_checksum(D: dict):
    K, V = list(D.keys()), list(D.values())

    n = len(V)
    for i in range(n):
        for j in range(0, n-i-1):
            if V[j] < V[j+1]:
                swap(K, V, j, j+1)

            if K[j] > K[j+1] and V[j] == V[j+1]:
                swap(K, V, j, j+1)

    return "".join(K[:5])


def decipher(S: list, id: int) -> str:
    s = list(" ".join(S))
    s = map(lambda x: chr(97 + (ord(x) - 97 + id) % 26) if x != " " else x, s)
    return "".join(s)


def solve(rooms, ids, checksums) -> int:
    n = len(rooms)
    sum_ids = 0
    room_names = []
    for i in range(n):
        C = Counter("".join(rooms[i]))
        actual_checksum = get_checksum(C)
        sum_ids += ids[i] if "".join(actual_checksum) == checksums[i] else 0
        room_names.append(decipher(rooms[i], ids[i]))

    north_pole_idx = room_names.index("northpole object storage")
    return sum_ids, ids[north_pole_idx]


puzzle = read_input()
ans = solve(*puzzle)
print(ans)
