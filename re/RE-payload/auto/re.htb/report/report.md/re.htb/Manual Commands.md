```bash
[*] http on tcp/80

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://re.htb:80 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_auth_hydra.txt" http-get://re.htb/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_auth_medusa.txt" -M http -h re.htb -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_form_hydra.txt" http-post-form://re.htb/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_form_medusa.txt" -M web-form -h re.htb -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://re.htb:80/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_wpscan.txt"

[*] microsoft-ds on tcp/445

	[-] Bruteforce SMB

		crackmapexec smb re.htb --port=445 -u "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -p "/usr/share/seclists/Passwords/darkweb2017-top100.txt"

	[-] Lookup SIDs

		impacket-lookupsid '[username]:[password]@re.htb'

	[-] Nmap scans for SMB vulnerabilities that could potentially cause a DoS if scanned (according to Nmap). Be careful:

		nmap -vv --reason -Pn -T4 -sV -p 445 --script="smb-vuln-* and dos" --script-args="unsafe=1" -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/tcp_445_smb_vulnerabilities.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/xml/tcp_445_smb_vulnerabilities.xml" re.htb


```