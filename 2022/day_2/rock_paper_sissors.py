# A|X Rock, B|Y Paper, C|Z Sissors
# Win = 6, Lose = 0, Draw = 3
# Rock = 1, Paper = 2, Sissors = 3

def play(p1, p2):
    if p1 == p2:
        return 3

    if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
        return 6

    return 0


move = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

winner = {1: 2, 2: 3, 3: 1}
loser = {k: v for v, k in winner.items()}

p1, p2 = 0, 0
T = 0
TNew = 0
with open("input.txt") as f:
    for line in f:
        L = line.replace(" ", "").strip()
        p1, p2 = move[L[0]], move[L[1]]

        T += play(p2, p1) + p2

        if L[1] == "X":
            p2 = loser[p1]
        elif L[1] == "Z":
            p2 = winner[p1]
        else:
            p2 = p1

        TNew += play(p2, p1) + p2

# Part one
print(f"Your total score is: {T}")


# Part two
# X = Lose, Y = Draw, Z = Win
print(f"Your total score is (new strategy): {TNew}")
