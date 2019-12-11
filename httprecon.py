#!/usr/bin/env python

# Python 2.7

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: httprecon.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Performing nmap HTTP script scan for " + ip_address + ":" + port
HTTPSCAN = "nmap -sV -Pn -vv -p %s --script=http-methods,http-enum,http-iis-webdav-vuln,http-webdav-scan,http-rfi-spider,http-robots.txt,http-shellshock,http-sql-injection,http-vuln-cve2006-3392,http-vuln-cve2009-3960,http-vuln-cve2010-0738,http-vuln-cve2010-2861,http-vuln-cve2011-3192,http-vuln-cve2011-3368,http-vuln-cve2012-1823,http-vuln-cve2013-0156,http-vuln-cve2013-7091,http-vuln-cve2014-2126,http-vuln-cve2014-2127,http-vuln-cve2014-2128,http-vuln-cve2014-2129,http-vuln-cve2014-2129,http-vuln-cve2015-1427,http-vuln-cve2015-1635,http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,http-config-backup,http-default-accounts,http-method-tamper,http-passwd -oN '/root/scripts/recon_enum/results/exam/%s_http.nmap' %s" % (port, ip_address, ip_address)

print "INFO: Performing Nikto HTTP script scan for " + ip_address + ":" + port
url = "http://" + ip_address
NIKTOSCAN = "nikto -host %s -p %s" % (url, port)

results = subprocess.check_output(HTTPSCAN, shell=True)
results2 = subprocess.check_output(NIKTOSCAN, shell=True)
outfile = "/root/recon_scan/results/" + ip_address + "_httprecon.txt"
f = open(outfile, "a+")
f.write(results)
f.write(results2)
f.close
