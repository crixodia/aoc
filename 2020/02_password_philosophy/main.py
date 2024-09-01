from collections import Counter


class Policy:
    def __init__(self, inf: int, sup: int, c: str) -> None:
        self.inf = inf
        self.sup = sup
        self.c = c

    def __repr__(self) -> str:
        return f"{self.inf}-{self.sup} {self.c}"

    def validate_password(self, password: str) -> bool:
        char_count = Counter(password)
        occurencies = char_count[self.c]

        return self.inf <= occurencies <= self.sup

    def otcas_validation(self, password: str) -> bool:
        first_validation = password[self.inf - 1] == self.c
        second_validation = password[self.sup - 1] == self.c
        return first_validation + second_validation == 1


def read_input(input_path: str) -> list:
    lines = open(input_path, "r").read().split("\n")

    policies, passwords = [], []
    for line in lines:
        policy, pwd = line.split(":")
        inf_sup, c = policy.split(" ")
        inf, sup = inf_sup.split("-")

        policies.append(
            Policy(
                inf=int(inf),
                sup=int(sup),
                c=c
            )
        )

        passwords.append(pwd.strip())

    return policies, passwords


def solve(policies: list, passwords: list, otcas: bool = False) -> int:
    valid_passwords = 0
    for i, pwd in enumerate(passwords):

        if otcas:
            is_valid = policies[i].otcas_validation(pwd)
        else:
            is_valid = policies[i].validate_password(pwd)

        valid_passwords += is_valid

    return valid_passwords


puzzle_input = read_input("input.txt")

ans1 = solve(*puzzle_input)
ans2 = solve(*puzzle_input, True)

ans = (ans1, ans2)
print(ans)
