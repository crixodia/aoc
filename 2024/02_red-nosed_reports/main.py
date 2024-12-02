def read_input(input_file="input.txt"):
    reports = open(input_file, "r").readlines()
    return [[int(x) for x in r.replace("\n", "").split()] for r in reports]


def is_safe(report):
    diffs = []
    is_increasing = False
    for i in range(1, len(report)):
        d = report[i-1] - report[i]

        if i == 1:
            is_increasing = d < 0
        elif is_increasing and d > 0 or not is_increasing and d < 0:
            return False

        diffs.append(0 < abs(d) < 4)

    return all(diffs)


def is_safe_with_tolerance(report):
    T = [report[0:i] + report[i+1:len(report)] for i in range(len(report))]
    T = [is_safe(tr) for tr in T]
    return any(T)


def solve(reports):
    return len(list(filter(is_safe, reports)))


def solve2(reports):
    return len(list(filter(is_safe_with_tolerance, reports)))


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
