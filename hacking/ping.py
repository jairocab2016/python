#!/usr/bin/env python
from subprocess import Popen, PIPE


for ip in range(1, 500):
    ipAddress = '192.168.212.%s' % str(ip)

for ip in range(1, 200):
    ipAddress = '192.168.168.%s' % str(ip)
    print "Scanning %s " % (ipAddress)
    subprocess = Popen(['/bin/ping', '-c 1 ',
                        ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = subprocess.communicate(input=None)
    if "bytes from " in stdout:
        print "The Ip Address %s has responded with a ECHO_REPLY!" % (stdout.split()[1])
        with open("ips.txt", "a") as myfile:
            myfile.write(stdout.split()[1] + '\n')
