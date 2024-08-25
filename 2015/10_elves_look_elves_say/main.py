def read_file(file):
    f = open(file, "r")
    return f.read()


def step(input):
    last = input[0]
    count = 1
    output = []

    for i in range(1, len(input)):
        c = input[i]
        if last == c:
            count += 1
        else:
            output.append(f"{count}{last}")
            last = c
            count = 1

    output.append(f"{count}{last}")
    return ''.join(output)


def solve(input, times):
    output = input
    for _ in range(times):
        output = step(output)
    return len(output)


input = read_file("input.txt")
ans1 = solve(input, 40)
ans2 = solve(input, 50)

ans = (ans1, ans2)
print(ans)
