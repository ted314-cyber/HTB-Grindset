```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://re.htb:80 2>&1 | tee "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nikto.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nikto.txt):

```
/bin/sh: 1: nikto: Permission denied

```
