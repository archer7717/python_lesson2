from fnmatch import *

for x in range(0, 10**9, 451):
    if fnmatch(str(x), '10?451*3'):
        print(x, x//451)