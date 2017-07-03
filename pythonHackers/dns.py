import dns
import dns.resolver

ansMX = dns.resolver.query("google.com", "A")
ansMX = dns.resolver.query("google.com", "MX")
ansNS = dns.resolver.query("google.com", "NS")
ansA = dns.resolver.query("google.com", "A")
ansAAAA = dns.resolver.query("google.com", "AAAA")
ansSOA = dns.resolver.query("google.com", "SOA")
ansTXT = dns.resolver.query("google.com", "TXT")

for ans in ansMX:
    print (ans)

for ans in ansNS:
	print (ans)

for ans in ansA:
	print (ans)

for ans in ansAAAA:
	print (ans)

for ans in ansSOA:
	print (ans)

for ans in ansTXT:
	print (ans)