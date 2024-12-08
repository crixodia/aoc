from math import floor


def read_input(input_file="input.txt"):
    lines = open(input_file, "r").readlines()

    rules = dict()
    pages = []

    for l in lines:
        if l == "\n":
            continue

        if "|" in l:
            b, a = l.split("|")
            b, a = int(b), int(a)

            if b not in rules:
                rules[b] = []

            rules[b].append(a)
        else:
            pages.append([int(x) for x in l.split(",")])

    return rules, pages


def custom_lt(x, y, rules):
    order = rules.get(x, None)

    if not order:
        return False

    if y in order:
        return True

    return False


def merge(left, right, rules):
    result = []

    i = j = 0

    while i < len(left) and j < len(right):
        if custom_lt(left[i], right[j], rules):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr, rules):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], rules)
    right = merge_sort(arr[mid:], rules)

    return merge(left, right, rules)


def solve(puzzle):
    rules, pages = puzzle
    valid_mid_sum = 0
    corrected_mid_sum = 0
    for page in pages:
        mid_idx = (len(page)-1)//2
        custom_sorted = merge_sort(page, rules)
        if custom_sorted == page:
            valid_mid_sum += page[mid_idx]
        else:
            corrected_mid_sum += custom_sorted[mid_idx]

    return valid_mid_sum, corrected_mid_sum


puzzle = read_input()
ans = (solve(puzzle))
print(ans)
