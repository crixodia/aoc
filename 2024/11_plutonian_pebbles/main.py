def read_input(input_file="input.txt"):
    return open(input_file, "r").readline().replace("\n", "").split()


def blink(current):
    if current == "0":
        return 0, ["1"]
    elif len(current) % 2 == 0:
        mid = len(current) // 2

        left = str(int(current[:mid]))
        right = str(int(current[mid:]))

        return 1, [left, right]

    return 0, [str(int(current) * 2024)]


def solve(puzzle, iters=6):

    stones = len(puzzle)
    last_stones = len(puzzle)

    with open("output.txt", "w") as f:
        for value in puzzle:
            f.write(value + "\n")

    current_line = 0
    level = 0

    with open("output.txt", 'r') as f:
        for line in f:

            size, new_val = blink(line.replace("\n", ""))

            stones += size

            with open("output.txt", "a") as g:
                for val in new_val:
                    g.write(f"{val}\n")

            current_line += 1
            if current_line == last_stones:
                level += 1
                last_stones = stones
                current_line = 0
                print(level)

            if level >= iters:
                break

    return stones


puzzle = read_input()
ans1 = solve(puzzle, 75)
print(ans1)
