x = 7**103 + 6*7**104 - 3*7**57 + 98

k = []

while x >0:
   # s = ''
    k = [x%7] + k
    x = x // 7
print(sum(k))
