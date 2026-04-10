from itertools import permutations

count =0
for x in permutations('ЭКЗАМЕН', r=7):
    s = "".join(x)
    s.replace('А','Э').replace('Е', 'Э')
    s.replace('З','К').replace('М','К').replace('Н','К')
    if s[0]=='А' and s[-1]=='К':
        print(s)
    else:
        count+=1
       # print(s)
print(count)
