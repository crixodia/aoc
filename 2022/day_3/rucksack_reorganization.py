
from functools import reduce

priority = []
priority2 = []
with open("input.txt") as f:
    for line in f:
        L = line.replace("\n", "").strip()
        m = len(L)//2
        A, B = set(L[:m]), set(L[m:])
        for el in A.intersection(B):
            priority.append(el)

        priority2.append(set(L))


def getRealOrd(c: str):
    F = 38 if c.isupper() else 96
    return ord(c) - F


# Part one
priority = list(map(getRealOrd, priority))
print(f"Sum of priorities: {sum(priority)}")

# Part Two
chunks = [list(map(set, priority2[i:i+3]))
          for i in range(0, len(priority2), 3)]

tags = []
for chunk in chunks:
    intersect = reduce(set.intersection, chunk)
    for el in intersect:
        tags.append(getRealOrd(el))

print(f"Sum of priorities (new approach): {sum(tags)}")
