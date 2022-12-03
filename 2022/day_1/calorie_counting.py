max_calories = 0
all_calories = []
with open('input.txt', 'r') as f:
    current = 0
    for line in f:
        L = line.replace("/n", "").strip()
        if L != "":
            current += int(L)
        else:
            max_calories = max(max_calories, current)
            all_calories.append(current)
            current = 0

# Part one
print(f"Max calories: {max_calories}")

# Part Two
all_calories.sort(reverse=True)
print("Sum of tp three max calories:", sum(all_calories[:3]))
