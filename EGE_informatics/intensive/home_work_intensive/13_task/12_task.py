from ipaddress import *

for mask in range(0, 33):
    ip = ip_network(f'111.233.75.16/{mask}', 0)
    print(ip, ip.num_addresses)