```bash
smbmap -H re.htb -P 445 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-share-permissions.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-share-permissions.txt):

```
[\] Working on it...
[+] Guest session   	IP: re.htb:445	Name: unknown
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
                                
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	IPC$                                              	READ ONLY	Remote IPC
	malware_dropbox                                   	READ ONLY


```
```bash
smbmap -u null -p "" -H re.htb -P 445 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-share-permissions.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-share-permissions.txt):

```
[\] Working on it...
[+] Guest session   	IP: re.htb:445	Name: unknown
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
                                
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	IPC$                                              	READ ONLY	Remote IPC
	malware_dropbox                                   	READ ONLY


```
```bash
smbmap -H re.htb -P 445 -r 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-list-contents.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-list-contents.txt):

```
[\] Working on it...
[+] Guest session   	IP: re.htb:445	Name: unknown
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
                                
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	IPC$                                              	READ ONLY	Remote IPC
	.\IPC$\*
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	InitShutdown
	fr--r--r--                4 Mon Jan  1 10:04:52 1601	lsass
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	ntsvcs
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	scerpc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-338-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	epmapper
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-1c4-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	LSM_API_service
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	eventlog
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-3b0-0
	fr--r--r--                4 Mon Jan  1 10:04:52 1601	wkssvc
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	atsvc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-414-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	spoolss
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-654-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	trkwks
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	W32TIME_ALT
	fr--r--r--                4 Mon Jan  1 10:04:52 1601	srvsvc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-24c-0
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	vgauth-service
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	ROUTER
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-258-0
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PSHost.133791304247589631.2404.DefaultAppDomain.powershell
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PSHost.133791304247591937.2412.DefaultAppDomain.powershell
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	efsrpc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PSHost.133791304425745211.2792.DefaultAppDomain.powershell
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iisipmf973bf04-6f0e-4c17-bf56-62b597677f3e
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iislogpipef6c753b4-96ec-4c1f-86fd-e49cd62084a1
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	WMXUmHkAyLN5HBkhQs38OkYAAChqL8o1iseLzwDj1W3YmDHfftDFqFlrdnENz1NVbMG8sqohbkl56ZdOjYrw1FcdHvk9zCbZ2xHTB71bt3MCC6FCco7m9F
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	CPFATP_2436_v4.0.30319
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iisipm4984b742-7ee8-489b-8d79-d58efac4dba7
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iislogpipece0dacbe-826e-4b9f-9de3-123e4712c9bc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	OMX5t8rA5YhvgXT0mMfflFTXGmAbmA7IDrsOQOEpKYevFB3DXw9UjSTWTnXqP4gsf4L62X1zqCPpxvoHjrEF8D9aSz4qOzYuLLMkyuZfIgzQDGgOOzUoMK
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	CPFATP_3916_v4.0.30319
	malware_dropbox                                   	READ ONLY
	.\malware_dropbox\*
	dr--r--r--                0 Wed Jun 19 07:08:36 2019	.
	dr--r--r--                0 Wed Jun 19 07:08:36 2019	..


```
```bash
smbmap -u null -p "" -H re.htb -P 445 -r 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-list-contents.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-list-contents.txt):

```
[\] Working on it...
[+] Guest session   	IP: re.htb:445	Name: unknown
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
                                
	Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	IPC$                                              	READ ONLY	Remote IPC
	.\IPC$\*
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	InitShutdown
	fr--r--r--                4 Mon Jan  1 10:04:52 1601	lsass
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	ntsvcs
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	scerpc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-338-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	epmapper
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-1c4-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	LSM_API_service
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	eventlog
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-3b0-0
	fr--r--r--                4 Mon Jan  1 10:04:52 1601	wkssvc
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	atsvc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-414-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	spoolss
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-654-0
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	trkwks
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	W32TIME_ALT
	fr--r--r--                4 Mon Jan  1 10:04:52 1601	srvsvc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-24c-0
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	vgauth-service
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	ROUTER
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	Winsock2\CatalogChangeListener-258-0
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PSHost.133791304247589631.2404.DefaultAppDomain.powershell
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PSHost.133791304247591937.2412.DefaultAppDomain.powershell
	fr--r--r--                3 Mon Jan  1 10:04:52 1601	efsrpc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PSHost.133791304425745211.2792.DefaultAppDomain.powershell
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iisipmf973bf04-6f0e-4c17-bf56-62b597677f3e
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iislogpipef6c753b4-96ec-4c1f-86fd-e49cd62084a1
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	WMXUmHkAyLN5HBkhQs38OkYAAChqL8o1iseLzwDj1W3YmDHfftDFqFlrdnENz1NVbMG8sqohbkl56ZdOjYrw1FcdHvk9zCbZ2xHTB71bt3MCC6FCco7m9F
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	CPFATP_2436_v4.0.30319
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iisipm4984b742-7ee8-489b-8d79-d58efac4dba7
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	iislogpipece0dacbe-826e-4b9f-9de3-123e4712c9bc
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	OMX5t8rA5YhvgXT0mMfflFTXGmAbmA7IDrsOQOEpKYevFB3DXw9UjSTWTnXqP4gsf4L62X1zqCPpxvoHjrEF8D9aSz4qOzYuLLMkyuZfIgzQDGgOOzUoMK
	fr--r--r--                1 Mon Jan  1 10:04:52 1601	CPFATP_3916_v4.0.30319
	malware_dropbox                                   	READ ONLY
	.\malware_dropbox\*
	dr--r--r--                0 Wed Jun 19 07:08:36 2019	.
	dr--r--r--                0 Wed Jun 19 07:08:36 2019	..


```
```bash
smbmap -H re.htb -P 445 -x "ipconfig /all" 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-execute-command.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-execute-command.txt):

```
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...

```
```bash
smbmap -u null -p "" -H re.htb -P 445 -x "ipconfig /all" 2>&1
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-execute-command.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp445/smbmap-execute-command.txt):

```
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...
[\] Working on it...
[|] Working on it...
[/] Working on it...
[-] Working on it...

```
