#!/usr/bin/env python
import subprocess
import sys
import os

if len(sys.argv) != 2:
    print "Usage: smbrecon.py <ip address>"
    sys.exit(0)

ip_address = sys.argv[1].strip()

print "INFO: Performing nmap SMB script scan for " + ip_address
SMBSCAN = "nmap -sV -Pn -vv -p 139,445 --script=smb-enum-shares.nse,smb-os-discovery,smb-vuln-conficker,smb-vuln-cve2009-3103,smb-vuln-ms06-025,smb-vuln-ms07-029,smb-vuln-ms08-067,smb-vuln-ms10-054,smb-vuln-ms10-061,smb-vuln-regsvc-dos,smb-system-info,smb-server-stats,smb-mbenum,smb-enum-users,smb-brute -oN '/root/scripts/recon_enum/results/exam/%s_smb.nmap' %s" % (ip_address, ip_address)

results = subprocess.check_output(SMBSCAN, shell=True)
outfile = "/root/recon_scan/results/" + ip_address + "_smbrecon.txt"
f = open(outfile, "a+")
f.write(results)
f.close
