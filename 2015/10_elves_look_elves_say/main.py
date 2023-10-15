def read_file(file):
    f = open(file, "r")
    return f.read()


def step(input):
    last = input[0]
    count = 0
    output = ""

    for c in input:
        if last == c:
            count += 1
        else:
            output = output + f"{count}{last}"
            count = 1
            last = c
    output = output + f"{count}{last}"
    return output


def solve(input, times):
    output = ""
    for i in range(times):
        output = step(input)
        input = output
    return len(output)


input = read_file("input.txt")
ans1 = solve(input, 40)
ans2 = solve(input, 50)

ans = (ans1, ans2)
print(ans)
