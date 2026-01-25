# counter = 0
# for n in range(100):
#     b = (bin(n)[2:])
#     for j in b:
#         if j == 1:
#             counter += 1
#     if counter % 2 == 0:
#         b = b +'0'
#     else:
#         b = b +'1'
#
#     for j in b:
#         if j == 1:
#             counter += 1
#     if counter % 2 == 0:
#         b = b +'0'
#     else:
#         b = b +'1'
#
#     r = int(b,2)
#     if r > 130:
#         print(n, r)

#
# counter = 0
# for n in range(100):
#     b = bin(n)[2:]
#     for i in b:
#         counter += int(i)
#     b = b + str(counter % 2)
#     counter = 0
#     for i in b:
#         counter += int(i)
#     b = b + str((counter % 2) * 2)
#     r = int(b, 2)
#     if r < 86:
#         print(n, r)
# count = 0
# for n in range(100):
#     b = bin(n)[2:]
#     for i in b:
#         count+= int(1)
#
#     if count%2==0:
#         b = b + "0"
#         b = b.replace(b[0], "10")
#         b = b.replace(b[0], "10")
#     else:
#         b = b + "1"
#         b = b.replace(b[0], "11")
#         b = b.replace(b[0], "11")
#     r = int(b,2)
#
#     print(r,n)




# for n in range(100):
#     b = bin(n)[2:]
#     if b[:1] == b[:0]:
#         b = b + '1'
#     if b[:1] == b[:0]:
#         b = b + '1'
#
#     r = int(b, 2)
#     if r > 93:
#         print(r, n)
#
# count = 0
# for n in range(1, 100):
#     b = bin(n)[2:]
#     b = b+ b[-1]
#     q = b.count('1')
#     if q %2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#
#     if q %2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#     r = int(b, 2)
#     if r > 97:
#         print(r, n)

# for n in range(100):
#     b = bin(n)[2:]
#     b = b + b[-1]
#     if bin(n).count('1')%2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#     if b.count('1')%2 == 0:
#         b = b + '0'
#     else:
#         b = b + '1'
#     r = int(b, 2)
#     if r > 90:
#         print(r, n)
# count = 0
# counter = 0
# for n in range(100):
#     b = bin(n)[2:]
#     for i in b:
#         count = count + int(i)
#     b = b + str(count%2)
#     count = 0
#     for i in b:
#         count = count + int(i)
#     b = b + str(count%2)
#     print(int(b,2))
#     if  210 <= int(b, 2) <= 260:
#         counter+=1
# print(counter)
# a = []
# for n in range(1, 100):
#     b = bin(n)[2:]
#     if n%2!=0:
#         b = "1" + b + "11"
#     else:
#         b = "11" + b + '00'
#     r = int(b, 2)
#     if r < 127:
#         a.append(r)
#         print(n, r)
# print(max(a))

# for n in range(1, 100):
#     b = bin(n)[2:]
#     if sum(map(int, b)) % 2 == 0:
#         b = b + "0"
#         del b[0]
#         del b[0]
#         b = "10" + b
#     else:
#         b = b + "1"
#         b = b.replace(b[0], '11')
#     r = int(b, 2)
#     if r > 16:
#         print(r, n)

# for n in range(1,100):
#     b = bin(n)[2:]
#     if sum(map(int, b)) % 2 ==0:
#         b = "10" + b[2:] + '0'
#     else:
#         b = '11' + b[2:] + '1'
#     r = int(b,2)
#     if r > 16:
#         print(r, n)





# Перевод из лююбой системы счисления в 10ричную
def cc(x):
    s = ''






























