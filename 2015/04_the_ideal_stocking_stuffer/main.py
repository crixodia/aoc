import hashlib


def to_hash(s, z):
    for i in range(0, 10000000):
        to_hash_tmp = s + str(i)
        hash = hashlib.md5(to_hash_tmp.encode("utf-8")).hexdigest()

        if hash.startswith("0" * z):
            return i


S = "ckczppom"
ans1 = to_hash(S, 5)
ans2 = to_hash(S, 6)
ans = (ans1, ans2)

print(ans)
