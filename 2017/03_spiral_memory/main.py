def read_input(input_file: str = "input.txt") -> int:
    return int(open(input_file, "r").readline())


def add_tuple(A, B) -> tuple:
    if len(A) != len(B):
        raise f"Dimensions are not the same {len(A)} != {len(B)}"

    C = [0] * len(A)
    for i, a in enumerate(A):
        C[i] = A[i] + B[i]

    return tuple(C)


def solve(target):
    next_pos = (0, 0)
    current_val = 1
    k = 0

    positions = {current_val: next_pos}
    while current_val < target:
        s = [(1, 0)] + [(0, 1)] * (2*k - 1) + \
            [(-1, 0)] * (2*k - 1) + [(0, -1)] * (2*k-2) + [(1, 0)]*(2*k-1)

        print(s)
        while s:
            current_val = current_val + 1
            next_pos = add_tuple(next_pos, s.pop(0))
            positions[current_val] = next_pos

        k = k + 1

    print(positions)


print(read_input())
solve(25)
