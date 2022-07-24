def read_input(file: str = 'input.txt') -> list[list['str']]:
    rows = []
    with open(file, 'r') as f:
        for line in f:
            rows.append(line.replace('\n', ''))
    return rows


def solve(s: str) -> int:
    vc = 0
    vowel_flag = False

    vowels = ('a', 'e', 'i', 'o', 'u')
    two_condition = ('ab', 'cd', 'pq', 'xy')

    last_two = ['', '']
    for c in s:
        last_two.append(c)
        last_two.pop(0)

        if ''.join(last_two) in two_condition:
            return 0

        if ''.join(last_two) == c*2:
            vowel_flag = True

        if c in vowels:
            vc += 1

    return int(vc >= 3 and vowel_flag)


"""

test = [
    'ugknbfddgicrmopn',  # True
    'aaa',  # True
    'jchzalrnumimnmhp',  # False
    'haegwjzuvuyypxyu',  # False
    'dvszwmarrgswjxmb'  # False
]

for t in test:
    print(t, solve(t))

"""
s = 0
for r in read_input():
    s += solve(r)

print(s)
