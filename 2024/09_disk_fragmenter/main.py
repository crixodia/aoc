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

    indices = list(range(len(files)))

    drive = []
    for i, f in enumerate(files):

        drive.extend([indices[i]]*f)

        count = 0
        for k in range(len(files)-1, i, -1):
            if indices[k] == -1:
                continue

            if files[k] <= space[i] - count:
                drive.extend([indices[k]]*files[k])
                indices[k] = -1
                count += files[k]

        drive.extend([-1]*(space[i]-count))

    return sum([x * i if x >= 0 else 0 for i, x in enumerate(drive)])


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
