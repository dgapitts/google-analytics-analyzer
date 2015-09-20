#!/usr/bin/python
import csv, sys
#[Browser,Browser_Version,Sessions]


print sys.argv[1]

browser_version_stats={}
#cr = csv.reader(open("test1_version.csv","rb"))
cr = csv.reader(open(sys.argv[1],"rb"))
for row in cr:
	try:
	 	#print row 
		browser_version=row[0]+' '+row[1].split('.')[0]
		Sessions=int(row[2].replace('.', '')) 
		if browser_version in browser_version_stats:
			browser_version_stats[browser_version]=browser_version_stats[browser_version]+Sessions
		else:
			browser_version_stats[browser_version]=Sessions
		#print browser_version, ' ', browser_version_stats[browser_version] 
	except Exception:
		#/dev/null
		pass

for key in browser_version_stats:
	print browser_version_stats[key] ,'\t', key 



