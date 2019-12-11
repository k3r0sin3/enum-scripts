#!/usr/bin/python

# Python 2.7

import sys
import os
import subprocess

if len(sys.argv) != 3:
    print "Usage: gobuster.py <http:// target url> <save as name>"
    sys.exit(0)

url = str(sys.argv[1])
name = str(sys.argv[2])
folders = ["/usr/share/seclists/Discovery/Web_Content"]

found = []
print "INFO: Starting dirb scan for " + url
for folder in folders:
    for filename in os.listdir(folder):

	outfile = " -o " + "/root/recon_scan/results/" + name + "_gobuster_" + filename
	GOSCAN = "gobuster -u %s -w %s/%s -e" % (url, folder, filename)
        try:
	    results = subprocess.check_output(GOSCAN, shell=True)
	    resultarr = results.split("\n")
	    for line in resultarr:
	        if "+" in line:
		    if line not in found:
		        found.append(line)
	except:
	    pass

try:
    if found[0] != "":
        print "[*] Gobuster found the following items..."
        for item in found:
            print "   " + item
except:
    print "INFO: No items found during gobuster scan of " + url	
