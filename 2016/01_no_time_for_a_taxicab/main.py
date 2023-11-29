def read_input(file="input.txt") -> list[tuple]:
    with open(file, "r") as f:
        values = f.readline().strip().split(", ")
    return [(x[0], int(x[1:])) for x in values]


def add_coord(a: tuple, b: tuple) -> tuple:
    return (a[0] + b[0], a[1] + b[1])


def scale_coord(a: int, b: tuple) -> tuple:
    return (a * b[0], a * b[1])


def abs_coord(a: tuple) -> tuple:
    return (abs(a[0]), abs(a[1]))


def next_ref(ref: tuple, dir: str) -> tuple:
    REF = {
        (1, 0): {"R": (0, -1), "L": (0, 1)},
        (0, 1): {"R": (1, 0), "L": (-1, 0)},
        (-1, 0): {"R": (0, 1), "L": (0, -1)},
        (0, -1): {"R": (-1, 0), "L": (1, 0)},
    }
    return REF[ref][dir]


def visited_pos_between(pos: tuple, dir: tuple, steps: int) -> list[tuple]:
    visited = []

    for i in range(steps):
        to_add = scale_coord(i, dir)
        visited.append(add_coord(pos, to_add))

    return visited


def solve(ins: list[tuple]) -> int:
    pos = (0, 0)
    ref = (0, 1)

    last_pos = None
    twice_pos = None
    all_positions = []

    for dir, steps in ins:
        last_pos = pos

        ref = next_ref(ref, dir)
        to_add = scale_coord(steps, ref)
        pos = add_coord(pos, to_add)

        new_visited = visited_pos_between(last_pos, ref, steps)

        for nv in new_visited:
            if nv in all_positions and not twice_pos:
                twice_pos = nv
                break

        if not twice_pos:
            all_positions += new_visited

    return sum(abs_coord(pos)), sum(abs_coord(twice_pos))


puzzle = read_input()
ans = solve(puzzle)
print(ans)
