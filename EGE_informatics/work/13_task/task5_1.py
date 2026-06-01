from ipaddress import *



# print('.'.join(f'{x:>08b}' for x in [241,185,253,57]))
# print(' ')
print('.'.join(f'{x:>08b}' for x in [241,185,252,0]))

for mask in range(33):
    net = ip_network(f'241.185.253.57/{mask}', 0)
    print(net, 32 - mask)


