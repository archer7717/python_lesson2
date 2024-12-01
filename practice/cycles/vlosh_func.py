x = int(input())
y = int(input())


if x > 0:
    if y > 0:
        print("Первая часть")
    else:
        print("Четвертая часть")
else:
    if y > 0:
        print("Вторая часть")
    else:
        print("Третья часть")
