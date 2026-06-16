from itertools import *



for a1 in '2468':
    for a2 in '0123456789':
        for a3 in '0123456789':
            for a4 in '13579':
                for a5 in '02468':
                    x = int(f'{a1}9{a2}23{a3}23{a4}{a5}')
                    if x % 1984 == 0:
                        print(x, x // 1984)