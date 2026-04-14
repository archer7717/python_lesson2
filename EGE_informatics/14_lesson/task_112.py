
for x in '0123456789abcdefgh':
    a = int(f'9009{x}', 18)  + int(f'2257{x}', 18)
    if a % 15 == 0:
        print(x, a// 15)
