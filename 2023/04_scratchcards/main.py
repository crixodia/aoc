from pprint import pprint


def read_input(file="input.txt"):
    cards = dict()
    with open(file, "r") as f:
        for line in f:
            line = line.replace("\n", "")

            a, numbers = line.split("|")
            name, winning = a.split(":")

            win = []
            winning = winning.strip().split(" ")
            for w in winning:
                if w.isdigit():
                    win.append(int(w))

            nums = []
            numbers = numbers.strip().split(" ")
            for n in numbers:
                if n.isdigit():
                    nums.append(int(n))

            name = int(name.replace("Card ", "").strip())
            cards[name] = {"winning": win, "numbers": nums, "stock": 1}

    return cards


def solve(puzzle):
    worth_points = 0
    for card, vals in puzzle.items():
        winning = vals.get("winning")
        numbers = vals.get("numbers")

        winning_numbers = 0
        for w in winning:
            winning_numbers += numbers.count(w)

        if winning_numbers > 1:
            worth_points += 1 * int(2 ** (winning_numbers - 1))
        else:
            worth_points += winning_numbers

    return worth_points


def solve(puzzle):
    worth_points = 0
    for card, vals in puzzle.items():
        winning = vals.get("winning")
        numbers = vals.get("numbers")

        winning_numbers = 0
        for w in winning:
            winning_numbers += numbers.count(w)

        if winning_numbers > 1:
            worth_points += 1 * int(2 ** (winning_numbers - 1))
        else:
            worth_points += winning_numbers

        puzzle[card]["winning_numbers"] = winning_numbers

    return worth_points


def __solve2__(card, puzzle):
    if card >= len(puzzle):
        return

    winning_numbers = puzzle[card]["winning_numbers"]

    for i in range(card + 1, card + winning_numbers + 1):
        puzzle[i]["stock"] += puzzle[card]["stock"]

    __solve2__(card + 1, puzzle)


def solve2(puzzle):
    __solve2__(1, puzzle)
    total_cards = 0
    for card_value in puzzle.values():
        total_cards += card_value["stock"]
    return total_cards


puzzle = read_input()
ans1 = solve(puzzle)
ans2 = solve2(puzzle)

ans = (ans1, ans2)
print(ans)
