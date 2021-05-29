from scapy.all import *
from scapy.layers.inet import IP, ICMP

pack = IP(dst="100.65.181.155") / ICMP()
resp = sr1(pack, timeout=2)

if resp is None:
    print("No response")
elif IP in resp:
    if resp.getlayer(IP).ttl <= 64:
        theos = "Linux/Google's Customised Linux(Android)/FreeBSD"
    elif resp.getlayer(IP).ttl <= 128:
        theos = "Windows XP / Window10 / Windows 7 / Vista"
    elif resp.getlayer(IP).ttl <= 225:
        theos = "Cisco Router"
    print(f"os:{theos}")
