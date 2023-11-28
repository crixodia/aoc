# 1 2 3 4 5 6 7 8 9 10
# 1 1 1 1 1 1 1 1 1  1
#   2   2   2   2    2
#     3     3     3
#       4       4
#         5          5
#           6
#             7
#               8
#                 9
#                   10


def find_house(amount, presents_per_elf=10, max_trips=None):
    target_house = -1

    max_house = -(-amount // presents_per_elf)
    arr = [0] * (max_house + 1)

    if max_trips is None:
        max_trips = max_house

    for house in range(1, max_house):
        arr[house] = 0

    for elf in range(1, max_house + 1):
        trips = 0
        for house in range(elf, max_house + 1, elf):
            if trips >= max_trips:
                break
            arr[house] += presents_per_elf * elf
            trips += 1

    for house in range(1, max_house):
        if arr[house] >= amount:
            target_house = house
            break

    return target_house


INPUT = 36000000
ans1 = find_house(INPUT)
ans2 = find_house(INPUT, 11, 50)

ans = (ans1, ans2)
print(ans)
