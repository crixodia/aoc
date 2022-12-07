def start_of_packet(n):
    with open("input.txt") as f:
        line = f.readline()
        for i in range(0, len(line)):
            if len(set(line[i:i+n])) == n:
                return i+n
    return 0

# Part one
print(f"{start_of_packet(4)} characters are needed")

# Part two
print(f"{start_of_packet(14)} characters are needed")
