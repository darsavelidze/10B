from ipaddress import *

ips = ip_network('192.168.108.157/255.255.255.192', 0)

for ip in ips:
    print(bin(int(ip))[2:], ip)


print(bin(192))
print(bin(157))
print(int('011101', 2))
print(2**6)