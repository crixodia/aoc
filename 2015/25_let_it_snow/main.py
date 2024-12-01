

def read_input(input_file="input.txt"):
    puzzle = open(input_file, "r").readline()
    puzzle = puzzle.replace(
        "To continue, please consult the code grid in the manual.  Enter the code at row ", "")

    puzzle = puzzle.replace(", column ", ",")
    puzzle = puzzle.replace(".", "")
    puzzle = puzzle.replace("\n", "")

    r, c = puzzle.split(",")
    return int(r), int(c)


def get_index(r, c):
    # 1 => +3 + (c - 2)(c - 2 + 5)/2
    # 2 => +2 + (c - 1)(c - 1 + 5)/2
    # 3 => +1 + (c + 0)(c + 0 + 5)/2
    # 4 =>  0 + (c + 1)(c + 1 + 5)/2
    # 5 => -1 + (c + 2)(c + 2 + 5)/2

    # g(r) => 4 - r
    # h(r) => r - 3
    # f(c,r) => g(r)+(c+h(r))*(c+h(r)+5)//2

    def g(r):
        return 4 - r

    def h(r):
        return r - 3

    return g(r)+(c+h(r))*(c+h(r)+5)//2


def get_code(n, seed=20151125, multiplier=252533, divider=33554393):
    # f(1) = 20151125
    # f(2) = (f(1)*M)%D
    # f(n) = (f(n-1)*M)%D
    # D => divider, M => multiplier, get_code(1) = seed
    if n <= 1:
        return seed

    return (get_code(n-1, seed, multiplier, divider) * multiplier) % divider


def get_code_iter(n, seed=20151125, multiplier=252533, divider=33554393):
    last = seed
    current = seed

    for _ in range(2, n+1):
        current = (last * multiplier) % divider
        last = current

    return last


def solve(puzzle):
    row, col = puzzle
    idx = get_index(row, col)
    return get_code_iter(idx)


puzzle = read_input()
ans = (solve(puzzle),)
print(ans)
