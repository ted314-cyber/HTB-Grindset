```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/xml/tcp_445_smb_nmap.xml" re.htb
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.80 scan initiated Fri Dec 20 12:38:56 2024 as: nmap -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/xml/tcp_445_smb_nmap.xml re.htb
Nmap scan report for re.htb (10.10.10.144)
Host is up, received user-set (0.012s latency).
Scanned at 2024-12-20 12:38:56 AEDT for 47s

PORT    STATE SERVICE       REASON          VERSION
445/tcp open  microsoft-ds? syn-ack ttl 127
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-print-text: false
| smb-protocols: 
|   dialects: 
|     2.02
|     2.10
|     3.00
|     3.02
|_    3.11
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-capabilities: 
|   2.02: 
|     Distributed File System
|   2.10: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.00: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.02: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.11: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-12-20T01:39:15
|_  start_date: N/A

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Dec 20 12:39:43 2024 -- 1 IP address (1 host up) scanned in 47.26 seconds

```
