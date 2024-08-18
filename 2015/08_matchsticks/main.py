def read_input(file):
    rows = []
    with open(file, "r") as f:
        for line in f:
            row = line.replace("\n", "")
            rows.append(row)
    return rows


def solve(rows):
    sl_count = 0
    mem_count = 0
    for row in rows:
        sl_count += len(row)

        decoded = row.encode().decode("unicode-escape")
        mem_count += len(decoded) - 2
    return sl_count - mem_count


def solve2(rows):
    sl_count = 0
    enc_count = 0
    for row in rows:
        sl_count += len(row)

        encoded = str(row.encode())
        encoded = encoded.replace('"', '\\"')
        encoded = encoded.replace("'", '"')
        encoded = list(encoded)
        encoded.pop(0)

        enc_count += len(encoded)
    return enc_count - sl_count


input = read_input("input.txt")
ans1 = solve(input)
ans2 = solve2(input)
ans = (ans1, ans2)

print(ans)
