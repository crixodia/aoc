from pprint import pprint

mapping = {
    "|": {"n": ("|", "F", "7", "S"), "s": ("|", "J", "L", "S")},
    "-": {"e": ("-", "7", "J", "S"), "w": ("-", "F", "L", "S")},
    "L": {"n": ("|", "F", "7", "S"), "e": ("J", "-", "7", "S")},
    "J": {"n": ("7", "|", "F", "S"), "w": ("L", "-", "F", "S")},
    "7": {"s": ("L", "|", "J", "S"), "w": ("-", "L", "F", "S")},
    "F": {"s": ("J", "|", "L", "S"), "e": ("-", "7", "J", "S")},
    "S": {
        "n": ("|", "F", "7"),
        "s": ("|", "J", "L"),
        "e": ("-", "7", "J"),
        "w": ("-", "F", "L"),
    },
}


def read_input(file="input.txt"):
    maze = []
    with open(file, "r") as f:
        for line in f:
            maze.append(list(line.strip()))

    return maze


def search_S(maze):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == "S":
                return i, j


def get_next_pipe(maze, pos, visited):
    i, j = pos
    rows, cols = len(maze), len(maze[0])
    n, s, e, w = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    next_pos = ()
    for p in [n, s, e, w]:
        ii, jj = p
        if not (0 <= ii < rows and 0 <= jj < cols):
            continue

        current_pipe = maze[i][j]

        next_pipes = ()
        if p == n:
            next_pipes = mapping[current_pipe].get("n")
        elif p == s:
            next_pipes = mapping[current_pipe].get("s")
        elif p == e:
            next_pipes = mapping[current_pipe].get("e")
        elif p == w:
            next_pipes = mapping[current_pipe].get("w")

        if not next_pipes:
            continue

        next_pos = (ii, jj)

        if (
            maze[ii][jj] in next_pipes
            and next_pos not in visited
            or (maze[ii][jj] == "S" and len(visited) > 2)
        ):
            return next_pos


def solve(maze):
    init_pos = search_S(maze)
    path = [init_pos]
    while path[-1] != path[0] or not path or len(path) == 1:
        path.append(get_next_pipe(maze, path[-1], path))
    return (len(path) - 1) // 2, path


def save_maze(maze, path):
    pipe_path_map = {
        "|": "║",
        "L": "╚",
        "F": "╔",
        "-": "═",
        "J": "╝",
        "7": "╗",
        "S": "╬",
    }

    pipe_map = {
        "|": "│",
        "L": "└",
        "F": "┌",
        "-": "─",
        "J": "┘",
        "7": "┐",
        ".": " ",
    }
    with open("maze.txt", "w", encoding="utf-8") as output:
        for i in range(len(maze)):
            line = ""
            for j in range(len(maze[0])):
                if (i, j) in path:
                    line = line + pipe_path_map[maze[i][j]]
                else:
                    line = line + pipe_map[maze[i][j]]

            print(line.encode("utf-8").decode("utf-8"), file=output)


def point_in_poly(point, poly):
    x, y = point
    intersections = 0
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        if ((y1 <= y < y2) or (y2 <= y < y1)) and (
            x < (x2 - x1) * (y - y1) / (y2 - y1) + x1
        ):
            intersections += 1

    return intersections % 2 == 1


# Ray Casting 🤯
def solve2(maze, path):
    rows, cols = len(maze), len(maze[0])
    wrapped = []
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in path:
                wrapped.append(point_in_poly((i, j), path))
    return sum(wrapped)


puzzle = read_input()

ans1, path = solve(puzzle)
save_maze(puzzle, path)
ans2 = solve2(puzzle, path)
ans = (ans1, ans2)

print(ans)
