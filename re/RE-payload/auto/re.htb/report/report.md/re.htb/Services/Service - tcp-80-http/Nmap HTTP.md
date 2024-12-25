```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/xml/tcp_80_http_nmap.xml" re.htb
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nmap.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.80 scan initiated Fri Dec 20 12:38:56 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_nmap.txt -oX /home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/xml/tcp_80_http_nmap.xml re.htb
Nmap scan report for re.htb (10.10.10.144)
Host is up, received user-set (0.012s latency).
Scanned at 2024-12-20 12:38:56 AEDT for 53s

PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 10.0
|_http-chrono: Request times for /; avg: 152.45ms; min: 151.58ms; max: 153.82ms
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=re.htb
|     
|     Path: http://re.htb:80/
|     Line number: 8
|     Comment: 
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|         
|_            </ol> -->
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-date: Fri, 20 Dec 2024 01:39:04 GMT; +1s from local time.
|_http-devframework: ASP.NET detected. Found related header.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-errors: Couldn't find any error pages.
|_http-feed: Couldn't find any feeds.
|_http-fetch: Please enter the complete path of the directory to save data in.
| http-headers: 
|   Content-Length: 930
|   Content-Type: text/html
|   Last-Modified: Mon, 25 Mar 2019 21:42:03 GMT
|   Accept-Ranges: bytes
|   ETag: "5e9ebb9553e3d41:0"
|   Server: Microsoft-IIS/10.0
|   X-Powered-By: ASP.NET
|   Date: Fri, 20 Dec 2024 01:39:05 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-malware-host: Host appears to be clean
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-mobileversion-checker: No mobile version detected.
| http-php-version: Logo query returned unknown hash 95f20fd0932c9a17f47f0e436585d65c
|_Credits query returned unknown hash 95f20fd0932c9a17f47f0e436585d65c
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-security-headers: 
|_http-server-header: Microsoft-IIS/10.0
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-title: Ghidra Dropbox Coming Soon!
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34
| http-vhosts: 
|_127 names had status 200
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Dec 20 12:39:49 2024 -- 1 IP address (1 host up) scanned in 53.45 seconds

```
