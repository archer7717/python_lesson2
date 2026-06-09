
from string import *

for x in printable[:25]:
    a = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if a%24==0:
        print(x, a// 24)