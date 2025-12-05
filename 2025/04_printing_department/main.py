from copy import deepcopy
import os
import glob
from PIL import Image
import re


def read_input(filename: str = "input.txt"):
    return [list(x.replace("\n", "")) for x in open(filename, "r").readlines()]


def get_adj_idx(i, j, n, m):
    return filter(
        lambda x: -1 < x[0] < n and -1 < x[1] < m,
        [
            (i-1, j-1),
            (i-1, j),
            (i-1, j+1),
            (i, j-1),
            (i, j+1),
            (i+1, j-1),
            (i+1, j),
            (i+1, j+1),
        ])


def solve(puzzle):
    output_state = deepcopy(puzzle)
    forklift_access = 0

    n = len(puzzle)
    m = len(puzzle[0])

    for i in range(n):
        for j in range(m):
            if puzzle[i][j] != "@":
                continue

            current_forklift = 0
            for x, y in get_adj_idx(i, j, n, m):
                try:
                    if puzzle[x][y] == "@":
                        current_forklift += 1
                except:
                    pass

            if current_forklift < 4:
                forklift_access += 1
                output_state[i][j] = "."

    # for line in output_state:
    #   print("".join(line))
    return forklift_access, output_state


def gen_frame(state, filename, cell_size=20, black_color=(0, 0, 0), white_color=(255, 255, 255)):
    frames_folder = "frames"
    os.makedirs(frames_folder, exist_ok=True)

    rows = len(state)
    cols = len(state[0]) if rows > 0 else 0

    img_width = cols * cell_size
    img_height = rows * cell_size

    img = Image.new('RGB', (img_width, img_height), color=white_color)
    pixels = img.load()

    for r in range(rows):
        for c in range(cols):
            color = black_color if state[r][c] == "@" else white_color
            for i in range(cell_size):
                for j in range(cell_size):
                    x = c * cell_size + j
                    y = r * cell_size + i
                    pixels[x, y] = color

    save_path = os.path.join(frames_folder, filename)
    img.save(save_path)


def natural_sort_key(s):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split('([0-9]+)', s)
    ]


def create_animation(output_filename="printing_department.gif", duration=100):
    frames_folder = "frames"
    image_paths = sorted(
        glob.glob(os.path.join(frames_folder, "*.png")),
        key=natural_sort_key
    )
    images = [Image.open(file) for file in image_paths]

    images[0].save(
        output_filename,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )


def solve2(puzzle):
    forklift_access = None
    output_state = deepcopy(puzzle)
    total_forklift_access = 0

    frame = 0
    gen_frame(output_state, f"{frame}.png")
    while forklift_access != 0:
        forklift_access, output_state = solve(output_state)
        total_forklift_access += forklift_access
        frame += 1
        gen_frame(output_state, f"{frame}.png")

    create_animation()

    return total_forklift_access


puzzle = read_input()
ans = (solve(puzzle)[0], solve2(puzzle))
print(ans)
