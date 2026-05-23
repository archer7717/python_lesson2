command = {
    (' ',0): (' ', -1, 1),
    (' ', 1): (' ',2,1),
    ('0', 1):('1',-1,1),
    ('1', 1):('0',-1,1)
}

def mt(s):
    s = list(' ' + s + ' ')
    q = 0
    i = len(s) - 1
    while True:
        cmd = command[(s[i], q)]
        s[i] = cmd[0]
        if cmd[1] == 2:
            break
        i += cmd[1]
        q = cmd[2]
    return ''.join(s)
print(int(mt('101110111'),2))