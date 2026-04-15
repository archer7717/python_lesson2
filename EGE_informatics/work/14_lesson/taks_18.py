from string import *

for x in printable[1:22]:
    for y in printable[:13]:
        a = int(f'{x}23{x}5',22) - int(f'67{y}9{y}', 13)
        if a % 57 == 0:
            print(int(x,22) + int(y, 13) , a//57)
