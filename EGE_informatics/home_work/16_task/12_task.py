
command = {
    (' ', 0):(' ', -1, 1),
    (' ', 2):(' ', 2, 2),
    ('0', 1):('2',-1, 1),
    ('1', 1):('0', 1, 2),
    ('1', 2):('0', 1, 2),
    ('2', 1):('1',-1,1)
}

def mt(s):
    s = list(' ' + s + ' ')
    i = len(s) -1
    q = 0

    while True:
        cmd = command[(s[i], q)]
        s[i] = cmd[0]
        if cmd[1] == 2:
            break
        q = cmd[2]
        i += cmd[1]
    return ''.join(s)

print(mt("0" * 106 + '1' * 334 + '2' * 560).count('0'))