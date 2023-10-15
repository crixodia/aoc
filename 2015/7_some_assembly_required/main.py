def read_input(file):
    rows = []
    with open(file, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            row = line.split(" -> ")
            row = row[::-1]
            rows.append(row)
    return rows


# NOTE: This is important to understand how unsigned integer works
def unsigned(number):
    return number % (1 << 16)


def eval(a, op="", b=0):
    ans = None

    if not op:
        ans = unsigned(a)
    elif op == "NOT":
        ans = unsigned(~a)
    elif op == "AND":
        ans = unsigned(a & b)
    elif op == "OR":
        ans = unsigned(a | b)
    elif op == "LSHIFT":
        ans = unsigned(a << b)
    elif op == "RSHIFT":
        ans = unsigned(a >> b)
    else:
        raise ("Check the operation!")

    return ans


def replace_signal(rows, signal, value):
    for i, row in enumerate(rows):
        sig, ins = row
        if signal == sig:
            rows[i] = [sig, f"{value}"]


def solve(rows):
    signals = {}
    i = 0
    while rows:
        sig, ins = rows[i]
        ins = ins.split(" ")
        n = len(ins)

        if n == 1:
            a = ins[0]

            a = int(a) if a.isdecimal() else signals.get(a, None)

            if a != None:
                signals[sig] = eval(a)
                rows.pop(i)
                i = -1

        elif n == 2:
            op, a = ins

            a = int(a) if a.isdecimal() else signals.get(a, None)

            if a != None:
                signals[sig] = eval(a, op)
                rows.pop(i)
                i = -1
        else:
            a, op, b = ins

            a = int(a) if a.isdecimal() else signals.get(a, None)
            b = int(b) if b.isdecimal() else signals.get(b, None)

            if a != None and b != None:
                signals[sig] = eval(a, op, b)
                rows.pop(i)
                i = -1
        i += 1
    return signals


input = read_input("input.txt")
ans1 = solve(input)["a"]

input = read_input("input.txt")
replace_signal(input, "b", ans1)
ans2 = solve(input)["a"]

ans = (ans1, ans2)
print(ans)
