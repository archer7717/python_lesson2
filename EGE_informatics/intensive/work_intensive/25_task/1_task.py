from fnmatch import *


for x in range(0, 10**10, 9874):
    if fnmatch(str(x),'89*6?7?9?'):
        print(x, x//9874)