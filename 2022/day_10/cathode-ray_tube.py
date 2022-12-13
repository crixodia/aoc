
X = 1
instructions = []
known_cycles = [20, 60, 100, 140, 180, 220]

with open("input.txt") as f:
    instructions = [line.replace("\n", "") for line in f]

positions = []
for i, ins in enumerate(instructions):
    positions.append(X)
    if ins.startswith("add"):
        positions.append(X)
        X += int(ins.split(" ")[1])


# Part One
signals = [(i+1)*x for i, x in enumerate(positions)]
print(
    f"Signal strength {sum([c for i, c in enumerate(signals) if i+1 in known_cycles])}")

# Part Two
CRT = [positions[i:i + 40] for i in range(0, len(positions), 40)]
CRT_str = ""
for row in CRT:
    R = ["#" if i in [pos - 1, pos, pos + 1] else " " for i, pos in enumerate(row)]
    CRT_str += "".join(R) + "\n"
print(CRT_str)
