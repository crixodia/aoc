def read_input(file):
    s = []
    with open(file) as f:
        for c in f.read():
            s.append(c)
    return s


def solve(input):
    instruction = {'(': 1, ')': -1}
    sum = 0
    pos = 0
    for i, c in enumerate(input):
        sum += instruction[c]
        if sum == -1 and pos == 0:
            pos = i + 1
    return sum, pos


print(solve(read_input('input.txt')))
