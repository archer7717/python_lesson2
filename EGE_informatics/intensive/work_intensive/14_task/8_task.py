from string import *


for x in printable[:27]:
    a = int(f'123{x}24', 27) + int(f'135{x}78', 27)
    if a %26==0:
        print(x, a // 26)