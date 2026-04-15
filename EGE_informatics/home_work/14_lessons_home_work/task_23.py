

# def to_10(a, n):
#     a = a[::-1]
#     s = 0
#     for i in range(len(a)):
#         s = s + a[i] + n**i
#     return s
#
# for x in range(1, 100):
#     for y in range(1, 100):
#         z = to_10([1,2,3,x,5], 15) + to_10([6,7,y,9], 17)
#         if z % 131==0:
#             print(x, y, z//131


# for x in '0123456789abcde':
#     for y in '0123456789abcdefg':
#         a = int(f'123{x}5', 15) + int(f'67{y}9', 17)
#         if a%131 == 0:
#             print(x, y, a//131)



for x in range(21):
    for y in range(21):
        a = 9 + 21*x + y * 21**2 + 2 *21**3 + 1 * 21**4 + 9 + 9*21 + y*21**2 + 6 * 21**3 + 3* 21**4
        if a % 18 == 0:
            print(x, y, a)