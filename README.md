# google-analytics-analyzer [![wercker status](https://app.wercker.com/status/3200e275c698f760a950ed35eacb9260/s/master "wercker status")](https://app.wercker.com/project/bykey/3200e275c698f760a950ed35eacb9260)
simple scripts to aggregate google analytics data



## Version 1 - aggregates data over just browser version (Safari 8, Chrome 40, IE 11 …)

The first version, aggregates data (i.e. csv file from google analytics) over just the 'browser version':

```sh
~/projects/google-analytics-analyzer $ head test_load_version.csv
# ----------------------------------------
# All Web Site Data
# *************
# 2014*******
# ----------------------------------------

Browser,Browserversie,Sessies,% nieuwe sessies,Nieuwe gebruikers,Bouncepercentage,Pagina's/sessie,Gem. sessieduur,Doelconversieratio,Behaalde doelen,Doelwaarde
Chrome,40.0.2214.111,2.546,"99,88%",2.543,"85,98%","1,15",00:00:31,"0,00%",0,"US$ 0,00"
Safari,8.0,449,"73,05%",328,"57,91%","2,16",00:01:19,"0,00%",0,"US$ 0,00"
Internet Explorer,11.0,411,"74,70%",307,"47,69%","2,35",00:01:37,"0,00%",0,"US$ 0,00"
```

Most of the logic is python, but I'm using a bash wrapper script for the sort operation ('sort -nr'):

```sh
~/projects/google-analytics-analyzer $ ./wrapper_load_version.sh test_load_version.csv | head
7374
2610 	Chrome 40
487 	Safari 8
411 	Internet Explorer 11
354 	Chrome 36
329 	Chrome 42
299 	Internet Explorer 9
284 	Safari 7
268 	Chrome 39
247 	Chrome 43
```

## Version 2 - aggregates data over both browser version and operating system (Mac, Windows, Android) 

The second version, aggregates data (i.e. csv file from google analytics) over both the 'browser version' and operating system (Mac, Windows, Android):

```sh
~/projects/google-analytics-analyzer $ head test_load_version_and_os.csv
# ----------------------------------------
# All Web Site Data
# ***************
# ***************
# ----------------------------------------

Browser,Browser Version,Operating System,Sessions
Chrome,40.0.2214.111,Macintosh,"2,533"
Safari,8.0,iOS,437
Internet Explorer,11.0,Windows,389
```

and here is some sample output:

```sh
~/projects/google-analytics-analyzer $ ./wrapper_load_version_and_os.sh test_load_version_and_os.csv | head
7374
2533 	Chrome 40 Macintosh
437 	Safari 8 iOS
389 	Internet Explorer 11 Windows
347 	Chrome 36 Windows
297 	Internet Explorer 9 Windows
225 	Safari 7 iOS
186 	Chrome 42 Windows
171 	Internet Explorer 8 Windows
118 	(not set) (not set) (not set)
```
