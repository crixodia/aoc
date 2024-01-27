def read_input(file="input.txt"):
    return list(open(file, "r").readline().replace("\n", ""))

def solve(puzzle):
    puzzle.append(puzzle[0])
    n = len(puzzle)
    matches = []
    for i in range(n - 1):
        if puzzle[i] == puzzle[i+1]:
            matches.append(int(puzzle[i]))
    
    return sum(matches)

def solve2(puzzle):
    n = len(puzzle)
    matches = []
    for i in range(n):
        next_idx = (i + n // 2) % n
        if puzzle[i] == puzzle[next_idx]:        
            matches.append(int(puzzle[i]))

    return sum(matches)

ans1 = solve(read_input())
ans2 = solve2(read_input())
ans = (ans1, ans2)

print(ans)
