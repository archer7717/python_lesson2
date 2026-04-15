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
# def cc(x):
#     s = ''
#     d = '0123456789abcdefghijklmnopqrstuvwxyz'
#     while x > 0:
#         s = d[x%12] + s
#         x = x // 12
#     return s

# def cc(x):
#     s = ''
#     while x > 0:
#         s = str(x%3) + s
#         x = x//3
#     return s
#
# for n in range(1, 100):
#     b = cc(n)
#     if n%3 == 0:
#         b = "1" + b + '02'
#     else:
#         b = b + cc((n%3) * 4)
#     r = int(b, 3)
#     #print(r, n)
#     if r < 199:
#         print(r, n)


# def cc(x):
#     s = ''
#     d = '0123456789abcdefg'
#     while x > 0:
#         s = str(d[x%12]) + s
#         x = x//12
#     return s
#
# for n in range(12, 300):
#     b = cc(n)
#     if n%12==0:
#         b = b + b[-2] + b[-1]
#     else:
#         b = b + cc((n%12) * 9)
#     r = int(b, 12)
#     if r > 300:
#         print(n, r)

#
# for n in range(1, 128):
#     b = bin(n)[2:].zfill(8)
#     b = b.replace('1', '2').replace('0', '1').replace('2', '0')
#     r = int(b, 2)
#     r = r + 1
#     if r  == 153:
#         print(n, r)

# for n in range(1, 100):
#     b = bin(n)[2:]
#     if len(b)%2==0:
#         b = b[:len(b)//2] + "1" + b[len(b)//2:]
#     else:
#         pass
#     r = int(b, 2)
#     if r <= 26:
#         print(n, r)

# for i in range(1000, 10000):
#     # a = str(i)[0] + str(i)[2]
#     #
#     # b = str(i)[1] + str(i)[3]
#     #print(i, a, b)
#     d = [int(d) for d in str(i)]
#   #  print(d)
#     a = d[0] + d[2]
#     b = d[1] + d[3]
#
#     if a < b:
#         r = int(str(a) + str(b))
#     else:
#         r = int(str(b) + str(a))
#     #print(i, r)
#     if r == 1315:
#         print(i, r)

# for n in range(1, 101):
#     b = bin(n)[2:]
#     b = b + str(b.count("1") %2)
#     b = b + str(b.count("1") %2)
#     r = int(b,2)
#     if r < 86:
#         print(n, r)

# k = 0
# for n in range(100, 1000):
#     d = str(n)
#     a = [d[0] + d[1] , d[0] + d[2], d[1] + d[0], d[1] + d[2], d[2] + d[0], d[2] + d[1]]
#     a = [int(x) for x in a if x[0]!="0"]
#     r = max(a) - min(a)
#     if r == 35:
#         k = k + 1
#         print(n, r)
# print(k)

# for n in range(100, 1000):
#     d = str(n)
#     a = [int(d[0]+ d[1]), int(d[1] + d[2])]
#     r = max(a) - min(a)
#     if r ==26:
#         print(n, r)
# summ2 = 0
# for n in range(1, 1000):
#     a = [int(d) for d in str(n)]
#     s1 = sum(d for d in a if d%2==0)
#     s2 = 0
#     for i in range(len(a)):
#         if (i+1)%2 ==0:
#             s2+=a[i]
#     r = abs(s2-s1)
#     if r == 7:
#         print(n, 7)

# for n in range(1, 10000000):
#     r = n
#     if r%3==0:
#         r = r//3
#     else:
#         r = r -1
#     if r%7 ==0:
#         r = r//7
#     else:
#         r = r - 1
#     if r%11 == 0:
#         r = r//11
#     else:
#         r = r - 1
#     if r == 6:
#         print(r, n)

# def f(n):
#     b = bin(n)[2:]
#     b = b + bin(n%3)[2:].zfill(2)
#     r = int(b,2)
#     b = b + bin(r%5)[2:].zfill(3)
#     r = int(b,2)
#     return r
# print(f(13))