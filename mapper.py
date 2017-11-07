from ipwhois import IPWhois
from pprint import pprint
import ipaddr

targetIp = raw_input("Enter Target IP Address: ")
obj = IPWhois(targetIp)
results = obj.lookup_rdap(depth=1)
pprint(results)

