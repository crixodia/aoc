def read_input(input_path: str) -> list[int]:
    lines = open(input_path, "r").read().split("\n")
    lines = [int(x.strip()) for x in lines]
    return lines


def solve(input: list) -> int:
    frec = 0
    mem = []

    for val in input:
        frec += val
        mem.append(frec)

    return frec, mem


def solve2(input: list) -> int:
    frec = 0
    mem = dict()

    while True:
        for val in input:
            frec += val
            if frec not in mem:
                mem[frec] = 1
            else:
                return frec


input = read_input('input.txt')
ans1, _ = solve(input)
ans2 = solve2(input)

ans = (ans1, ans2)
print(ans)
