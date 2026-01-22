b = input()

if len(b) == 6:
    print((b[0] + b[1:][::-1]).lstrip("0"))
else:
    print(b[::-1].lstrip("0"))



