```bash
ffuf -u http://re.htb:80/ -t 10 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.re.htb" -mc all -fs 311 -r -noninteractive -s | tee "/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_re.htb_vhosts_subdomains-top1million-110000.txt"
```

[/home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_re.htb_vhosts_subdomains-top1million-110000.txt](file:///home/cbjs/htb/re/RE-payload/auto/re.htb/scans/tcp80/tcp_80_http_re.htb_vhosts_subdomains-top1million-110000.txt):

```
Fuzz Faster U Fool - v1.1.0

HTTP OPTIONS:
  -H               Header `"Name: Value"`, separated by colon. Multiple -H flags are accepted.
  -X               HTTP method to use (default: GET)
  -b               Cookie data `"NAME1=VALUE1; NAME2=VALUE2"` for copy as curl functionality.
  -d               POST data
  -ignore-body     Do not fetch the response content. (default: false)
  -r               Follow redirects (default: false)
  -recursion       Scan recursively. Only FUZZ keyword is supported, and URL (-u) has to end in it. (default: false)
  -recursion-depth Maximum recursion depth. (default: 0)
  -replay-proxy    Replay matched requests using this proxy.
  -timeout         HTTP request timeout in seconds. (default: 10)
  -u               Target URL
  -x               HTTP Proxy URL

GENERAL OPTIONS:
  -V               Show version information. (default: false)
  -ac              Automatically calibrate filtering options (default: false)
  -acc             Custom auto-calibration string. Can be used multiple times. Implies -ac
  -c               Colorize output. (default: false)
  -maxtime         Maximum running time in seconds for entire process. (default: 0)
  -maxtime-job     Maximum running time in seconds per job. (default: 0)
  -p               Seconds of `delay` between requests, or a range of random delay. For example "0.1" or "0.1-2.0"
  -s               Do not print additional information (silent mode) (default: false)
  -sa              Stop on all error cases. Implies -sf and -se. (default: false)
  -se              Stop on spurious errors (default: false)
  -sf              Stop when > 95% of responses return 403 Forbidden (default: false)
  -t               Number of concurrent threads. (default: 40)
  -v               Verbose output, printing full URL and redirect location (if any) with the results. (default: false)

MATCHER OPTIONS:
  -mc              Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403)
  -ml              Match amount of lines in response
  -mr              Match regexp
  -ms              Match HTTP response size
  -mw              Match amount of words in response

FILTER OPTIONS:
  -fc              Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fl              Filter by amount of lines in response. Comma separated list of line counts and ranges
  -fr              Filter regexp
  -fs              Filter HTTP response size. Comma separated list of sizes and ranges
  -fw              Filter by amount of words in response. Comma separated list of word counts and ranges

INPUT OPTIONS:
  -D               DirSearch wordlist compatibility mode. Used in conjunction with -e flag. (default: false)
  -e               Comma separated list of extensions. Extends FUZZ keyword.
  -ic              Ignore wordlist comments (default: false)
  -input-cmd       Command producing the input. --input-num is required when using this input method. Overrides -w.
  -input-num       Number of inputs to test. Used in conjunction with --input-cmd. (default: 100)
  -mode            Multi-wordlist operation mode. Available modes: clusterbomb, pitchfork (default: clusterbomb)
  -request         File containing the raw http request
  -request-proto   Protocol to use along with raw request (default: https)
  -w               Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'

OUTPUT OPTIONS:
  -debug-log       Write all of the internal logging to the specified file.
  -o               Write output to file
  -od              Directory path to store matched results to.
  -of              Output file format. Available formats: json, ejson, html, md, csv, ecsv (or, 'all' for all formats) (default: json)

EXAMPLE USAGE:
  Fuzz file paths from wordlist.txt, match all responses but filter out those with content-size 42.
  Colored, verbose output.
    ffuf -w wordlist.txt -u https://example.org/FUZZ -mc all -fs 42 -c -v

  Fuzz Host-header, match HTTP 200 responses.
    ffuf -w hosts.txt -u https://example.org/ -H "Host: FUZZ" -mc 200

  Fuzz POST JSON data. Match all responses not containing text "error".
    ffuf -w entries.txt -u https://example.org/ -X POST -H "Content-Type: application/json" \
      -d '{"name": "FUZZ", "anotherkey": "anothervalue"}' -fr "error"

  Fuzz multiple locations. Match only responses reflecting the value of "VAL" keyword. Colored.
    ffuf -w params.txt:PARAM -w values.txt:VAL -u https://example.org/?PARAM=VAL -mr "VAL" -c

  More information and examples: https://github.com/ffuf/ffuf


```
