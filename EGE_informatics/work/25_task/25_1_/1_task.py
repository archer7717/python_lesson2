# a?b aab acd adb avb

#a*b ab aab asdb avvvb

from fnmatch import *


for x in range(0,10**8,171):
    if fnmatch(str(x),'1*23??56'):
        print(x, x // 171)
