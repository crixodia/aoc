from functools import lru_cache


def read_input(input_file="input.txt"):
    return tuple(open(input_file, "r").readline().replace("\n", "").split())


def blink(stone):
    if stone == "0":
        return tuple(["1"])

    elif len(stone) % 2 == 0:
        mid = len(stone) // 2

        left = str(int(stone[:mid]))
        right = str(int(stone[mid:]))

        return (left, right)

    return tuple([str(int(stone) * 2024)])


# Use LRU cache to optimize stone counting
@lru_cache(None)
def count_stones(stones, depth):
    if depth == 0:
        return len(stones)  # A single stone remains

    n_stones = 0
    for s in stones:
        new_stones = blink(s)
        n_stones += count_stones(new_stones, depth - 1)

    return n_stones


puzzle = read_input()
ans = (count_stones(puzzle, 25), count_stones(puzzle, 75))
print(ans)
