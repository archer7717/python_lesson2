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

# for n in range(1, 3000):
#     b = bin(n)[2:]
#    # print(b)
#     if n%2==0:
#         b = b + (b.count("0") * "0")
#     else:
#         b = (b.count('1') *'1') + b
#     r = int(b,2)
#     if r > 2000:
#         print(n, r)



# for n in range(2, 100):
#     b = bin(n)[2:]
#     if b[-1] == b[-2]:
#         b = b + '0'
#     else:
#         b = b + '1'
#
#     if b[-1] == b[-2]:
#         b = b + '0'
#     else:
#         b = b + '1'
#     r = int(b, 2)
#     if r > 93:
#         print(n, r)

# for n in range(2, 1000):
#     b = bin(n)[2:]
#     if n%3 == 0:
#         b = b + (bin(n%2)[2:])[-3:]
#     else:
#         b = b + bin((n%3)*3)[2:]
#     r = int(b,2)
#     if r > 151:
#         print((r, n))
# x = []
# for n in range(10, 2501):
#     b = bin(n)[2:]
#   #  print(b)
#     for i in b:
#         if i == '0':
#             b = b.replace(i, '')
#     r = int(b, 2)
#     #print(r)
#     if r not in x:
#         x.append(r)
# print(len(x))

# for n in range(1, 1000):
#     b = bin(n)[2:]
#    # print(b)
#     b = b.replace("0", "2").replace("1", "0").replace("2", "1")
#     b = b.replace("0", "2").replace("1", "0").replace("2", "1")
#     r = int(b, 2)
#     if r < 170:
#         print(r, n)