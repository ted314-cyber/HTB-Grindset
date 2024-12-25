```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_top_100_udp_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_top_100_udp_nmap.xml" re.htb
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_top_100_udp_nmap.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.80 scan initiated Fri Dec 20 12:37:27 2024 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_top_100_udp_nmap.txt -oX /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_top_100_udp_nmap.xml re.htb
Nmap scan report for re.htb (10.10.10.144)
Host is up, received user-set (0.013s latency).
All 100 scanned ports on re.htb (10.10.10.144) are open|filtered because of 100 no-responses
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.80%E=4%D=12/20%OT=%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=6764D169%P=x86_64-pc-linux-gnu)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Network Distance: 2 hops

TRACEROUTE (using proto 1/icmp)
HOP RTT      ADDRESS
1   12.76 ms 10.10.14.1
2   12.89 ms re.htb (10.10.10.144)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Dec 20 13:07:37 2024 -- 1 IP address (1 host up) scanned in 1810.06 seconds

```
