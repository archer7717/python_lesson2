# for n in range(1, 101):
#     b = bin(n)[2:]
#     b = b + str(b.count("1") %2)
#     b = b + str(b.count("1") %2)
#     r = int(b,2)
#     if r < 86:
#         print(n, r)
#

# for n in range(1, 101):
#     b = bin(n)[2:]
#     if b.count('1')%2==0:
#         b = "10" + b[2:] + '0'
#     else:
#         b = '11' + b[2:] + '1'
#     r = int(b,2)
#     if  r > 40:
#         print(n, r)

# for n in range(2, 101):
#     b = bin(n)[2:]
#     if b[0] == b[1]:
#         b = b + "0"
#     else:
#         b = b + "1"
#     if b[0] == b[1]:
#         b = b + "0"
#     else:
#         b = b + "1"
#     r = int(b, 2)
#     if r > 93:
#         print(n, r)

for n in range(1, 3000):
    b = bin(n)[2:]
   # print(b)
    if n%2==0:
        b = b + (b.count("0") * "0")
    else:
        b = (b.count('1') *'1') + b
    r = int(b,2)
    if r > 2000:
        print(n, r)