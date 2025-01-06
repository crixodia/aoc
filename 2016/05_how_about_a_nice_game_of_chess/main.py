from hashlib import md5
import os
import time


def clear_scr():
    os.system("cls" if os.name == 'nt' else "clear")


def solve(door):
    idx = 0
    password = ""
    password2 = ["-"]*8
    pp = False

    while len(password) < 8 or "-" in password2:
        current_hash = md5(bytes(f"{door}{idx}", "utf8")).hexdigest()

        if current_hash.startswith("0"*5):
            if len(password) < 8:
                password += current_hash[5]
                pp = True

            if current_hash[5].isdigit():
                pos, c = int(current_hash[5]), current_hash[6]
                if pos < 8:
                    if password2[pos] == "-":
                        password2[pos] = c
                        pp = True

        idx += 1
        if pp:
            clear_scr()
            print(
                "Hash:",
                current_hash,
                "P1:",
                "-"*(8 - len(password)) + password,
                "P2:",
                "".join(password2)
            )
            pp = False
    return password, "".join(password2)


solve("abc")
