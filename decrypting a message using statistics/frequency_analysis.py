# This is an implementation of frequency analysis algorithm

msg = [int(x) for x in open('message', 'r').read().split(' ')]

def password_to_key(password: str):
    return [ord(c) for c in list(password)]


def encrypt(message, password):
    key = password_to_key(password)

    return [ord(c) ^ key[i % len(key)] for i, c in enumerate(list(message))]


def decrypt(encrypted, password):
    key = password_to_key(password)

    return "".join([chr(n ^ key[i % len(key)]) for i, n in enumerate(encrypted)])

def analysis(msg, key_length):
    max_size = 0
    for c in msg:
        if c > max_size:
            max_size = c

    a_msg = []
    for y in range(0, key_length):
        a_msg.append([])
        for x in range(0, max_size + 1):
            a_msg[y].append(0)
    key = []
    for x in range(0, key_length):
        key.append(0)

    for i, c in enumerate(msg):
        j = i % key_length
        a_msg[j][c] += 1
        if a_msg[j][c] > a_msg[j][key[j]]:
            key[j] = c

    space_ascii = 32

    for i in range(0, key_length):
        key[i] = key[i] ^ space_ascii

    return key

for x in range(1, 10):
    password = ''.join([chr(x) for x in analysis(msg, x)])
    print('==', x, password)
    print(decrypt(msg, password))
