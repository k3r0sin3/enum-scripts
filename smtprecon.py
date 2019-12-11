#!/usr/bin/python
import socket
import sys
import subprocess

if len(sys.argv) != 2:
    print "Usage: smtprecon.py <ip address>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
	
SMTPSCAN = "nmap -vv -sV -Pn -p 25,465,587 --script=smtp-commands,smtp-enum-users,smtp-open-relay,smtp-open-relay,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -oN '/root/scripts/recon_enum/results/exam/%s_smtp.nmap' %s" % (ip_address, ip_address)

results = subprocess.check_output(SMTPSCAN, shell=True)
outfile = "/root/recon_scan/results/" + ip_address + "_smtprecon.txt"
f = open(outfile, "w")
f.write(results)
f.close


###NEED TO CREATE USERNAME WORDLIST IF WANT TO USE CODE BELOW###
#print "INFO: Trying SMTP Enum on " + sys.argv[1]
#names = open('/usr/share/wfuzz/wordlist/fuzzdb/wordlists-user-passwd/names/namelist.txt', 'r')
#for name in names:
#    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    connect=s.connect((sys.argv[1],25))
#    banner=s.recv(1024)
#    s.send('HELO test@test.org \r\n')
#   result= s.recv(1024)
#   s.send('VRFY ' + name.strip() + '\r\n')
#   result=s.recv(1024)
#    if ("not implemented" in result) or ("disallowed" in result):
#	sys.exit("INFO: VRFY Command not implemented on " + sys.argv[1]) 
#    if (("250" in result) or ("252" in result) and ("Cannot VRFY" not in result)):
#	print "[*] SMTP VRFY Account found on " + sys.argv[1] + ": " + name.strip()	
#    s.close()
