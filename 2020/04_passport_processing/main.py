import re


def to_dict(L):
    M = [x.split(":") for x in L]
    D = dict()
    for k, v in M:
        D[k] = v
    return D


def read_input(input_file="input.txt"):
    passports_text = ""
    with open(input_file, "r") as f:
        for line in f.readlines():
            passports_text = passports_text + line.replace(" ", "\n")

    passports = [to_dict(x.split("\n")) for x in passports_text.split("\n\n")]
    return passports


def solve(passports):
    valid_fields = 0
    valid_values = 0
    for p in passports:
        keys = set(p.keys())

        if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}.issubset(keys):
            valid_fields += 1

            all_conditions = []
            for k, v in p.items():
                conditions = [
                    k == "byr" and 1920 <= int(v) <= 2002,
                    k == "iyr" and 2010 <= int(v) <= 2020,
                    k == "eyr" and 2020 <= int(v) <= 2030,
                    k == "hgt" and (
                        "cm" in v and 150 <= int(
                            v.replace("cm", "").replace("in", "")) <= 193
                        or "in" in v and 59 <= int(v.replace("in", "").replace("cm", "")) <= 76
                    ),
                    k == "hcl" and v.startswith(
                        "#") and re.match(r"#[0-9a-f]{6}", v),
                    k == "ecl" and v in ("amb", "blu",
                                         "brn", "gry", "grn", "hzl", "oth"),
                    k == "pid" and v.isdigit() and len(v) == 9,
                    k == "cid"
                ]
                all_conditions.append(any(conditions))

            valid_values += all(all_conditions)

    return valid_fields, valid_values


puzzle = read_input()
ans = (solve(puzzle))

print(ans)
