command = {
    (' ', 0):(' ', 1, 1),
    (' ', 1): (' ', 2, 1),
    ('1', 1): ('0', 1, 1),
    ('0', 1): ('1', 1, 1)
}

def mt(s):
    s = list(' ' + s + ' ')
    i = 0
    q = 0
    while True:
        cmd = command[(s[i], q)]
        s[i] = cmd[0]
        if cmd[1] == 2:
            break
        q = cmd[2]
        i += cmd[1]
    return ''.join(s)

print(mt(bin(400)[2:]))