```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_quick_tcp_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_quick_tcp_nmap.xml" re.htb

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_full_tcp_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_full_tcp_nmap.xml" re.htb

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/_top_100_udp_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/xml/_top_100_udp_nmap.xml" re.htb

feroxbuster -u http://re.htb:80/ -t 10 -w /root/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://re.htb:80/.well-known/security.txt

curl -sSikf http://re.htb:80/robots.txt

curl -sSik http://re.htb:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://re.htb:80 2>&1 | tee "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/xml/tcp_80_http_nmap.xml" re.htb

ffuf -u http://re.htb:80/ -t 10 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.re.htb" -mc all -fs 311 -r -noninteractive -s | tee "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_re.htb_vhosts_subdomains-top1million-110000.txt"

whatweb --color=never --no-errors -a 3 -v http://re.htb:80 2>&1

wkhtmltoimage --format png http://re.htb:80/ /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_screenshot.png

enum4linux -a -M -l -d re.htb 2>&1

nbtscan -rvh 10.10.10.144 2>&1

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/xml/tcp_445_smb_nmap.xml" re.htb

smbclient -L //re.htb -N -I re.htb 2>&1

smbmap -H re.htb -P 445 2>&1

smbmap -u null -p "" -H re.htb -P 445 2>&1

smbmap -H re.htb -P 445 -r 2>&1

smbmap -u null -p "" -H re.htb -P 445 -r 2>&1

smbmap -H re.htb -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H re.htb -P 445 -x "ipconfig /all" 2>&1


```