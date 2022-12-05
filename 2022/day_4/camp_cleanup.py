def iscontained(A1, A2):
    # Is A2 contained in A1
    return A2[0] >= A1[0] and A2[1] <= A1[1]


def isoverlapped(A1, A2):
    return A1[1] >= A2[0] and A1[0] <= A2[1]


fully_contains = 0
overlapped = 0
with open("input.txt") as f:

    for line in f:
        L = line.strip()
        A1, A2 = line.split(",")

        A1 = list(map(int, A1.split("-")))
        A2 = list(map(int, A2.split("-")))

        if iscontained(A1, A2) or iscontained(A2, A1):
            fully_contains += 1

        if isoverlapped(A1, A2):
            overlapped += 1

# Part One
print(f"There are {fully_contains} pairs that fully contain the other")

# Part Two
print(f"There are {overlapped} pairs that are overlapped")
