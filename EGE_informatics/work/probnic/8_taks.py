from itertools import permutations

count= 0
for x in permutations('ЭКЗАМЕН', r=7):
    s = ''.join(x)
    s =    s.replace('А', 'Э').replace('Е', 'Э')
    s = s.replace( 'З', 'К').replace('М', 'К').replace('Н', 'К')
    if s[0] != 'Э' and s[-1] != 'К':
        print(s)
        count+=1
print(count)