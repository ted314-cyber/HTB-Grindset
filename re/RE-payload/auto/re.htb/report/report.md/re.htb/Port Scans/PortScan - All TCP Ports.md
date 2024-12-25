```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_full_tcp_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_full_tcp_nmap.xml" re.htb
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_full_tcp_nmap.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_full_tcp_nmap.txt):

```
# Nmap 7.80 scan initiated Fri Dec 20 12:37:27 2024 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_full_tcp_nmap.txt -oX /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_full_tcp_nmap.xml re.htb
adjust_timeouts2: packet supposedly had rtt of -189072 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -189072 microseconds.  Ignoring time.
Nmap scan report for re.htb (10.10.10.144)
Host is up, received user-set (0.014s latency).
Scanned at 2024-12-20 12:37:28 AEDT for 171s
Not shown: 65533 filtered ports
Reason: 65533 no-responses
PORT    STATE SERVICE       REASON          VERSION
80/tcp  open  http          syn-ack ttl 127 Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Ghidra Dropbox Coming Soon!
445/tcp open  microsoft-ds? syn-ack ttl 127
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
TCP/IP fingerprint:
SCAN(V=7.80%E=4%D=12/20%OT=80%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=6764CB03%P=x86_64-pc-linux-gnu)
SEQ(SP=108%GCD=1%ISR=108%TS=U)
OPS(O1=M539NW8NNS%O2=M539NW8NNS%O3=M539NW8%O4=M539NW8NNS%O5=M539NW8NNS%O6=M539NNS)
WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70)
ECN(R=Y%DF=Y%TG=80%W=FFFF%O=M539NW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=264 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 0s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 61175/tcp): CLEAN (Timeout)
|   Check 2 (port 39973/tcp): CLEAN (Timeout)
|   Check 3 (port 18622/udp): CLEAN (Timeout)
|   Check 4 (port 29025/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-12-20T01:39:42
|_  start_date: N/A

TRACEROUTE (using port 445/tcp)
HOP RTT      ADDRESS
1   14.45 ms 10.10.14.1
2   14.89 ms re.htb (10.10.10.144)

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Dec 20 12:40:19 2024 -- 1 IP address (1 host up) scanned in 172.25 seconds

```