from concurrent.futures import ProcessPoolExecutor
from copy import deepcopy


def read_input(input_file="input.txt"):
    lines = open(input_file, "r").readlines()
    return [list(x.replace("\n", "")) for x in lines]


DIRECTIONS = ("^", "v", "<", ">")
TURN_90 = {"^": ">", "v": "<", "<": "^", ">": "v"}
TO_ADD = {
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1)
}


def add_tuple(A, B):
    if len(A) != len(B):
        raise "Value error"

    return tuple([A[i] + B[i] for i in range(len(A))])


def get_guard_position(guard_map):
    for i in range(len(guard_map)):
        for j in range(len(guard_map[i])):
            if guard_map[i][j] in DIRECTIONS:
                return (i, j), guard_map[i][j]
    return -1, -1


def get_obstacles(guard_map):
    obstacles = []
    for i in range(len(guard_map)):
        for j in range(len(guard_map[i])):
            if guard_map[i][j] == "#":
                obstacles.append((i, j))
    return obstacles


def is_outside(pos, dir, rows, cols):
    x, y = pos
    return any([
        (dir == "^" and x == 0),
        (dir == "v" and x == rows - 1),
        (dir == "<" and y == 0),
        (dir == ">" and y == cols - 1)
    ])


def add_pos(pos, dir):
    return add_tuple(pos, TO_ADD[dir])


def solve(guard_map, animate=False):
    rows, cols = len(guard_map), len(guard_map[0])

    obstacles = get_obstacles(guard_map)
    visited_obstacles = []
    pos, dir = get_guard_position(guard_map)

    positions = [pos]
    is_loop = False
    frame = 0

    while not is_outside(pos, dir, rows, cols):
        next_pos = add_pos(pos, dir)

        x, y = pos
        guard_map[x][y] = " "

        if next_pos in obstacles:

            if (next_pos, dir) in visited_obstacles:
                is_loop = True
                break

            visited_obstacles.append((next_pos, dir))

            dir = TURN_90[dir]
            next_pos = pos
            continue

        pos = next_pos

        if pos not in positions:
            positions.append(pos)

        # Animation
        if animate:
            x, y = pos
            guard_map[x][y] = dir
            M = ""
            for r in guard_map:
                M = M + "".join(r) + "\n"

            with open(f"./output/{frame}.txt", "w") as f:
                f.write(M)

            frame += 1
        # End Animation

    return len(positions), positions, is_loop


# Define process_path as a top-level function

def process_path(args):
    guard_map, coords = args
    i, j = coords
    new_guard_map = deepcopy(guard_map)
    if new_guard_map[i][j] in DIRECTIONS:
        return 0
    new_guard_map[i][j] = "#"
    _, _, is_loop = solve(new_guard_map)
    return 1 if is_loop else 0


def solve2(guard_map, available_path):
    # Pass both guard_map and coordinates to process_path
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(
            process_path, [(guard_map, coords) for coords in available_path]))

    return sum(results)


if __name__ == '__main__':
    puzzle = read_input()
    puzzle2 = read_input()

    ans1, positions, _ = solve(puzzle, True)
    ans2 = solve2(puzzle2, positions)
    ans = (ans1, ans2)
    print(ans)
