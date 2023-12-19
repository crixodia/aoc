from collections import Counter
from functools import cmp_to_key


def read_input(file="input.txt"):
    hands_bids = dict()
    with open(file, "r") as f:
        for line in f:
            h, b = line.replace("\n", "").split()
            hands_bids[h] = int(b)

    return hands_bids


LABELS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def get_type(hand, J=False):
    C = Counter(hand)

    if J:
        max_label, max_val = "J", 0
        for key, val in C.items():
            if key == "J":
                continue

            if max_val == 0:
                max_val = val
                max_label = key

            if val > max_val:
                max_val = val
                max_label = key

        C = Counter(hand.replace("J", max_label))

    n = len(C)
    vals = list(C.values())

    if n == 1:
        return 7

    if n == 2:
        if 4 in vals:
            return 6

        if 3 in vals:
            return 5

    if n == 3:
        if 3 in vals:
            return 4

        if vals.count(2) == 2:
            return 3

    if vals.count(2) == 1:
        return 2

    if n == 5:
        return 1


def get_higher_hand(h1, h2, J=False):
    labels = ["J"] + LABELS if J else LABELS
    for i in range(len(h1)):
        if h1[i] == h2[i]:
            continue

        return labels.index(h1[i]) - labels.index(h2[i])
    return 0


def compare(h1, h2):
    th1, th2 = get_type(h1), get_type(h2)

    if th1 == th2:
        return get_higher_hand(h1, h2)

    return th1 - th2


def compare_j_rule(h1, h2):
    th1, th2 = get_type(h1, True), get_type(h2, True)

    if th1 == th2:
        return get_higher_hand(h1, h2, J=True)

    return th1 - th2


def solve(puzzle):
    s_hands = sorted(puzzle, key=cmp_to_key(compare))
    js_hands = sorted(puzzle, key=cmp_to_key(compare_j_rule))

    total, total2 = 0, 0
    for i in range(len(puzzle)):
        total += puzzle[s_hands[i]] * (i + 1)
        total2 += puzzle[js_hands[i]] * (i + 1)

    return total, total2


puzzle = read_input()
ans = solve(puzzle)
print(ans)
