command = {
    (' ', 0): (' ', 1, 1),
    (' ', 2): (' ', 2, 2),


#FIXME

}

def mt(s):
    s = list(' ' + s + ' ')
    q = 0
    i = 0
    while True:
        cmd = command[(s[i], q)]
        s[i] = cmd[0]
        if cmd[1] == 2:
            break
        q = cmd[2]
        i += cmd[1]
    return ''.join(s)

print(mt('10010111'))