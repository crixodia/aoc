from time import time


def read_input(input_file="input.txt"):
    return open(input_file, "r").readline().replace("\n", "").split()


def blink(stone):
    if stone == "0":
        return ["1"]

    elif len(stone) % 2 == 0:
        mid = len(stone) // 2

        left = str(int(stone[:mid]))
        right = str(int(stone[mid:]))

        return [left, right]

    return [str(int(stone) * 2024)]


# Memory stores the number of stones with the stone label and its depth
def conunt_stones(stones, depth, memory={(1, "0"): 1}):
    if depth == 0:
        return len(stones)

    n_stones = 0
    for s in stones:
        if (depth, s) in memory:
            n_stones += memory[(depth, s)]
            continue

        new_stones = blink(s)

        memory[(depth, s)] = conunt_stones(
            new_stones,
            depth - 1,
            memory
        )
        n_stones += memory[(depth, s)]

    return n_stones


puzzle = read_input()
ans = (conunt_stones(puzzle, 25), conunt_stones(puzzle, 75))
print(ans)
