def read_input(file="input.txt"):
    calibration_doc = []

    with open(file, "r") as f:
        for line in f:
            line = line.replace("\n", "")
            calibration_doc.append(line)

    return calibration_doc


spelled2num = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_overlappings():
    K = list(spelled2num.keys())
    overlaped = dict()
    for i in range(len(K)):
        for j in range(len(K)):
            if K[i][-1] == K[j][0]:
                overlaped[K[i][:-1] + K[j]] = spelled2num[K[i]] + spelled2num[K[j]]

    return overlaped


def get_number(s):
    n = len(s)
    first = None
    last = None
    for i in range(n):
        if s[i].isdigit() and not first:
            first = int(s[i])

        if s[n - 1 - i].isdigit() and not last:
            last = int(s[n - 1 - i])

        if first != None and last != None:
            break

    return first * 10 + last


def transform(s):
    overlappings = get_overlappings()
    for overlap in overlappings.keys():
        s = s.replace(overlap, overlappings[overlap])

    for key, val in spelled2num.items():
        s = s.replace(key, spelled2num[key])

    return s


def solve(calibration_doc):
    D = map(get_number, calibration_doc)
    return sum(D)


def solve2(calibration_doc):
    D = map(transform, calibration_doc)
    D = map(get_number, D)
    return sum(D)


puzzle = read_input()
ans1 = solve(puzzle)
ans2 = solve2(puzzle)

ans = (ans1, ans2)
print(ans)
