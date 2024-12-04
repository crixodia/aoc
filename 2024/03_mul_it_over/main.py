import re


MUL_PATTERN = r"mul\(\d+,\d+\)"
MUL_PATTERN_DO = r"do\(\)|mul\(\d+,\d+\)|don't\(\)"


def read_input(input_file='input.txt'):
    return open(input_file).read().strip()


def eval_mul(mul_str):
    exp = mul_str.replace("mul(", "")
    exp = exp.replace(")", "")
    a, b = exp.split(",")
    return int(a) * int(b)


def solve(puzzle):
    lexer = re.compile(MUL_PATTERN)
    mul_operations = lexer.findall(puzzle)
    return sum([eval_mul(x) for x in mul_operations])


def solve2(puzzle):
    lexer = re.compile(MUL_PATTERN_DO)
    operations = lexer.findall(puzzle)

    total = 0
    multiply = True
    for op in operations:
        if op == "do()":
            multiply = True
        elif op == "don't()":
            multiply = False
        elif multiply:
            total += eval_mul(op)

    return total


puzzle = read_input()
ans = (solve(puzzle), solve2(puzzle))
print(ans)
