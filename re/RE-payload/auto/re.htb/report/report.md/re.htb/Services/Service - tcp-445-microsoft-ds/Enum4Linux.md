```bash
enum4linux -a -M -l -d re.htb 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/enum4linux.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/enum4linux.txt):

```
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Fri Dec 20 12:38:56 2024

[34m =========================================( [0m[32mTarget Information[0m[34m )=========================================

[0mTarget ........... re.htb
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


[34m ===============================( [0m[32mEnumerating Workgroup/Domain on re.htb[0m[34m )===============================

[0m[33m
[E] [0m[31mCan't find workgroup/domain

[0m

[34m ===================================( [0m[32mNbtstat Information for re.htb[0m[34m )===================================

[0mLooking up status of 10.10.10.144
No reply from 10.10.10.144

[34m ======================================( [0m[32mSession Check on re.htb[0m[34m )======================================

[0m[33m
[E] [0m[31mServer doesn't allow session using username '', password ''.  Aborting remainder of tests.

[0m

```