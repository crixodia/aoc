

def read_input(input_file="input.txt"):
    positions, velocities = [], []
    with open(input_file, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            line = line.replace("p=", "")
            line = line.replace("v=", "")

            p, v = line.split()
            px, py = p.split(",")
            vx, vy = v.split(",")

            positions.append([int(px), int(py)])
            velocities.append([int(vx), int(vy)])

    return positions, velocities


def solve(puzzle, rows=7, cols=11, seconds=100):
    P, V = puzzle
    mid_col, mid_row = cols//2, rows//2

    for t in range(0, seconds + 1):
        bathroom = [[' ']*cols for _ in range(rows)]
        if t == 0:
            continue
        for r, p in enumerate(P):
            x, y = p
            vx, vy = V[r]

            x += vx
            y += vy

            x = x % cols
            y = y % rows

            P[r] = [x, y]
            bathroom[y][x] = "#"

    q1, q2, q3, q4 = 0, 0, 0, 0
    for r, p in enumerate(P):
        x, y = p
        if x < mid_col and y < mid_row:
            q1 += 1
        elif x > mid_col and y < mid_row:
            q2 += 1
        elif x < mid_col and y > mid_row:
            q3 += 1
        elif x > mid_col and y > mid_row:
            q4 += 1

    return q1 * q2 * q3 * q4, bathroom


ans = (solve(read_input(), rows=103, cols=101), solve2(read_input()))
print(ans)
