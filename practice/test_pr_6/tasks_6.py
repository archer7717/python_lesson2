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

#3
N = int(input())
A = [0]*N
n = 0
curren_max = 0
max = 0
for k in A:
    b  = int(input())
    A[n] = b
    if A[n] ==1:
        curren_max +=1
        if curren_max > max:
            max = curren_max
    else:
        curren_max = 0
    n+=1
print(max)
