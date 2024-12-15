from math import inf
import os

from PIL import Image


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_binary_matrix(matrix, output_path):
    colors = {
        0: (128, 128, 128),  # Grey
        1: (255, 165, 0)    # Orange
    }

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    img = Image.new('RGB', (cols, rows))
    pixels = img.load()

    for y in range(rows):
        for x in range(cols):
            pixels[x, y] = colors[matrix[y][x]]

    img = img.resize((1000, 1000), resample=Image.NEAREST)
    img.save(output_path)


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
    current_min = inf

    for t in range(seconds + 1):
        bathroom = [[0]*cols for _ in range(rows)]
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
            bathroom[y][x] = 1

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

        sf = q1*q2*q3*q4

        if sf < current_min:
            clear_console()
            draw_binary_matrix(bathroom, f"./output/{t}.png")
            current_min = sf
            print(t, current_min)

    return sf


ans = (solve(read_input(), rows=103, cols=101))
print("Part 1:", ans)
input("Press enter to continue...")
solve(read_input(), 103, 101, 100_000_000_000)
