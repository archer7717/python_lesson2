a = [int(x) for x in open('17_13_1.txt')]

sms = []
for a, b, c in zip(a, a[1:], a[2:]):
    if (a % 40 == 15) + (b % 40 == 15) + (c % 40 == 15) == 2:
        if (a % 7 == 0) + (b % 7 == 0) + (c % 7 == 0) <= 2:
            if a % 40 != 15:
                sms.append(a)
            elif b % 40 != 15:
                sms.append(b)
            else:
                sms.append(c)

print(len(sms), sum(sms))