from fnmatch import *


for x in range(0,10**10, 2024):
    if fnmatch(str(x), '1*2322?2'):
        print(x, x//2024)