
#Вернутся попозже



x = int(input())
t_seq = [0, 0, 1]
idx = 2
while t_seq[-1] <= x:
    t_seq.append(sum(t_seq[-3:]))
    idx += 1
print(idx)
