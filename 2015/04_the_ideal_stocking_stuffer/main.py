import hashlib

to_hash = 'ckczppom'
z = 6  # 5

for i in range(0, 10000000):
    to_hash_tmp = to_hash + str(i)
    hash = hashlib.md5(to_hash_tmp.encode('utf-8')).hexdigest()

    if hash.startswith('0' * z):
        print(i)
        break
