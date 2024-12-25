```bash
curl -sSik http://re.htb:80/
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_curl.html](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_curl.html):

```
HTTP/1.1 200 OK
Content-Type: text/html
Last-Modified: Mon, 25 Mar 2019 21:42:03 GMT
Accept-Ranges: bytes
ETag: "5e9ebb9553e3d41:0"
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Date: Fri, 20 Dec 2024 01:38:56 GMT
Content-Length: 930

<!DOCTYPE html>
<html>
  <head>
    <title>Ghidra Dropbox Coming Soon!</title>
  </head>
  <body>
    <p>Please check back soon for re.htb updates.</p>
	<!--future capability
	<p> To upload Ghidra project:
	<ol>
	  <li> exe should be at project root.Directory stucture should look something like:
	      <code><pre>
|   vulnerserver.gpr
|   vulnserver.exe
\---vulnerserver.rep
    |   project.prp
    |   projectState
    |
    +---idata
    |   |   ~index.bak
    |   |   ~index.dat
    |   |
    |   \---00
    |       |   00000000.prp
    |       |
    |       \---~00000000.db
    |               db.2.gbf
    |               db.3.gbf
    |
    +---user
    |       ~index.dat
    |
    \---versioned
            ~index.bak
            ~index.dat
		  </pre></code>
	  </li>
	  <li>Add entire directory into zip archive.</li>
	  <li> Upload zip here:</li>
    </ol> -->
</body>
 </html>

```
