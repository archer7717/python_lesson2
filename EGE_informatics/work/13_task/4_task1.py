from ipaddress import *
# print('.'.join(f'{x:>08b}' for x in [148,195,140,28]))
# print(' ')
#print('.'.join(f'{x:>08b}' for x in [255,255,252,0]))

for mask in range(33):
    net = ip_network(f'148.195.140.28/{mask}', 0)
    print(net, net.netmask)

print('.'.join(f'{x:>08b}' for x in [255,255,252,0]))