def read_input(input_file="input.txt"):
    return [int(x) for x in list(open(input_file, "r").readline())]


def solve(puzzle):
    files, space = puzzle[::2], puzzle[1::2]
    if len(space) < len(files):
        space.append(0)

    drive = []
    for i, f in enumerate(files):
        drive.extend([i]*f)
        drive.extend([None]*space[i])

    pointer = 0
    while pointer < len(drive):
        while drive[-1] == None:
            drive.pop(-1)
            pointer -= 1

        if drive[pointer] == None:
            drive[pointer] = drive.pop(-1)

        pointer += 1

    return sum([x * i for i, x in enumerate(drive)])


def solve2(puzzle):
    files, space = puzzle[::2], puzzle[1::2]
    if len(space) < len(files):
        space.append(0)

    drive = []
    for i, f in enumerate(files):
        drive.append([i]*f)

        if space[i] != 0:
            drive.append([None]*space[i])

    i = 0
    while i < len(drive):
        if set(drive[i]) == {None}:

            j = len(drive) - 1
            while j > i:
                if set(drive[j]) == {None}:
                    j -= 1
                    continue

                if len(drive[j]) <= len(drive[i]):
                    size = len(drive[i])
                    drive[i] = drive[j].copy()
                    none_len = size - len(drive[j])
                    if none_len != 0:
                        drive.insert(i+1, [None]*none_len)

                    drive[j+1] = [None] * len(drive[i])
                    print(drive, none_len)
                    break

                j -= 1
        i += 1

    return drive


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
