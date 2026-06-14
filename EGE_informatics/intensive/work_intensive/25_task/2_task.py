from fnmatch import *


for x in range(0, 10**8, 271):
    if fnmatch(str(x), '12??15*6'):
        print(x, x//271)