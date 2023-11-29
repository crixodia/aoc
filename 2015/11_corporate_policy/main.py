import time


def read_input(file):
    return open(file, "r").readline().replace("\n", "")


def req1(s):
    count = 1
    last = s[0]
    for i in range(1, len(s)):
        if ord(last) + 1 == ord(s[i]):
            count += 1
        elif count >= 3:
            return True
        else:
            count = 1
        last = s[i]
    return count >= 3


def req2(s):
    not_allowed = ["i", "o", "l"]
    for c in s:
        if c in not_allowed:
            return False
    return True


def req3(s):
    count = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            count += 1
            i += 1
        i += 1
    return count >= 2


def add(S, idx=None):
    if idx == None:
        idx = len(S) - 1

    if S[idx] == "z":
        S[idx] = "a"
        S = add(S, idx - 1)
    else:
        S[idx] = chr(ord(S[idx]) + 1)
    return S


def skip(s):
    indices = []
    for c in ["i", "o", "l"]:
        idx = s.find(c)
        if idx != -1:
            indices.append(idx)

    if not indices:
        return s, False

    min_idx = min(indices)
    S = list(s)
    S[min_idx] = chr(ord(S[min_idx]) + 1)
    for i in range(min_idx + 1, len(S)):
        S[i] = "a"
    return "".join(S), True


def solve(s):
    while not (req1(s) and req2(s) and req3(s)):
        s, skipped = skip(s)
        if not skipped:
            s = "".join(add(list(s)))
    return s


i = read_input("input.txt")
ans1 = solve(i)
ans2 = solve("".join(add(list(ans1))))

ans = (ans1, ans2)
print(ans)
