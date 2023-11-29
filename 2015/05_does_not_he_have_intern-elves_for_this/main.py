def read_input(file="input.txt"):
    rows = []
    with open(file, "r") as f:
        for line in f:
            rows.append(line.replace("\n", ""))
    return rows


def solve(s):
    vc = 0
    vowel_flag = False

    vowels = ("a", "e", "i", "o", "u")
    two_condition = ("ab", "cd", "pq", "xy")

    last_two = ["", ""]
    for c in s:
        last_two.append(c)
        last_two.pop(0)

        if "".join(last_two) in two_condition:
            return 0

        if "".join(last_two) == c * 2:
            vowel_flag = True

        if c in vowels:
            vc += 1

    return int(vc >= 3 and vowel_flag)


def solve2(s):
    c1 = False
    c2 = False
    for i in range(len(s)):
        if i + 2 >= len(s):
            continue

        if s[i] == s[i + 2]:
            c2 = True

        for j in range(i + 2, len(s)):
            if s[i : i + 2] == s[j : j + 2]:
                c1 = True
    return c1 and c2


def second_condition(s):
    for i in range(len(s)):
        if i + 2 >= len(s):
            continue
        if s[i] == s[i + 2]:
            print(s[i : i + 3])


s1 = 0
s2 = 0
for r in read_input():
    s1 += solve(r)
    s2 += solve2(r)

print((s1, s2))
