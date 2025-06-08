#1
# x = int(input())
# y = int(input())
# r = int(input())
# if x**2+y**2 <= r*r:
#     print("Yes")
# else:
#     print("No")
#2 потом сделать
# vklad = int(input())
# p = int(input())
# y = int(input())
# year = 0
# while vklad <y:
#     year+=1
#     vklad+=vklad*p/100
#     kopeeiki = vklad * 100
#     kopeeiki = int(kopeeiki)
#     kopeeiki = kopeeiki/100
#     vklad = kopeeiki
#     #vklad = int(vklad)
#
# print(year)
from uaclient.api.u.pro.packages.summary.v1 import summary

#3
# N = int(input())
# A = [0]*N
# n = 0
# curren_max = 0
# max = 0
# for k in A:
#     b  = int(input())
#     A[n] = b
#     if A[n] ==1:
#         curren_max +=1
#         if curren_max > max:
#             max = curren_max
#     else:
#         curren_max = 0
#     n+=1
# print(max)


#
# n = int(input())
# counter_3_summ = 0
# counter_3 = 0
# remainder = 0
# average = 0
# av = 0
# max = 0
# min = 99999999
# while n!="#":
#     counter_3_summ +=n
#     counter_3+=1
#     if counter_3 ==3:
#         remainder += counter_3_summ%n
#         # print(remainder, counter_3_summ)
#         counter_3_summ=0
#         counter_3=0
#
#     av+=1
#     average +=n
#     if n > max:
#         max = n
#     if n <min:
#         min = n
#     a = input()
#     if a == '#':
#         break
#     else:
#         n = int(a)**2**0.5
#     print(a)
#
# average = round(average/av,3)
#
#
# print(average,max,min,remainder)

#4
# A =['#'] * 100000
# b = 0
# n = int(input())
# number_1 = 0
# number_2 = 1
# number_3 = 2
# counter_3 = 0
# counter_3_summ = 0
# remainder = 0
# average = 0
# av = 0
# max = 0
# min = 99999999
# while n!='#':
#     A[b] = n
#     b+=1
#     a = input()
#     if a=='#':
#         break
#     else:
#         n = int(a)
# b = 0
# while A[b]!='#':
#     if A[b] > max:
#         max = A[b]
#     if A[b] < min:
#         min = A[b]
#     average +=A[b]
#     av+=1
#     b+=1
#
# average= round(average/av,3)
# b = 0
# while A[number_1]!='#':
#     counter_3_summ = A[number_1] + A[number_2] +A[number_3]
#     remainder+=counter_3_summ%A[number_3]
#     counter_3_summ=0
#     number_1+=3
#     number_2+=3
#     number_3+=3
#
# print(average,max,min,remainder)

#5_not_done
# A = []
# n = int(input())
# b = input()
# while b!='#':
#     x, y =map(int, b.split())
#     A.append(x)
#     A.append(y)
#     b = input()
# print(A)







