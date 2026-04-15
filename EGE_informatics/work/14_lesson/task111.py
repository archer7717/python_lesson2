
from string import *

for x in printable[:17]:
    for y in printable[:17]:
        a = int(f'7{x}589{y}', 17) + int(f'ee{x}{y}8ac', 17)
        if a %13 == 0:
            print(x, y, a//13)
