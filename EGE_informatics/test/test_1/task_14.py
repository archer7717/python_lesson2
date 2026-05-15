a = 5 * 1296**2021- 4*216**2022 + 3 * 36**2023 - 2* 6**2024 - 2025

def f(n):
    s = ''
    while n >0:
        s = str(n%36) + s
        n = n // 36
    return s

b = f(a)
k = 0
for i in b:
    if int(i)%2==0:
        k+=1
print(k)

