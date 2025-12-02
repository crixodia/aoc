def read_input(filename: str = "input.txt"):
    ranges = open(filename, "r").readline().replace("\n", "").split(",")
    ranges = [r.split("-") for r in ranges]
    return [(int(rid[0]), int(rid[1])) for rid in ranges]


def is_invalid_id(number: int) -> bool:
    str_number = str(number)
    n = len(str_number)

    if n % 2 != 0:
        return False

    a, b = str_number[:n//2], str_number[n//2:]
    return a == b


def is_invalid_all(number: int) -> bool:
    str_number = str(number)
    n = len(str_number)

    multiples = [i for i in range(1, n) if n % i == 0]
    for m in multiples:
        chunks = set(str_number[i:i+m] for i in range(0, n, m))
        if len(chunks) == 1:
            return True

    return False


def solve(puzzle):
    sum_invalid = 0
    sum_invalid2 = 0
    for l, r in puzzle:
        sum_invalid += sum(filter(is_invalid_id, range(l, r+1)))
        sum_invalid2 += sum(filter(is_invalid_all, range(l, r+1)))
    return sum_invalid, sum_invalid2


puzzle = read_input()
ans = (solve(puzzle))
print(ans)
