#!/usr/bin/python
import csv, sys
#[Browser,Browser_Version,Operating_System,Sessions]

browser_version_stats={}
#cr = csv.reader(open("test_data.csv","rb"))
cr = csv.reader(open(sys.argv[1],"rb"))
for row in cr:
	try:
	 	#print row 
		browser_version_os=row[0]+' '+row[1].split('.')[0]+' '+row[2]
		Sessions=int(row[3].replace(',', '')) 
		#print Sessions
		if browser_version_os in browser_version_stats:
			browser_version_stats[browser_version_os]=browser_version_stats[browser_version]+Sessions
		else:
			browser_version_stats[browser_version_os]=Sessions
		#print browser_version_os, ' ', browser_version_stats[browser_version_os] 
	except Exception:
		#/dev/null
		pass

for key in browser_version_stats:
	print browser_version_stats[key] ,'\t', key 



