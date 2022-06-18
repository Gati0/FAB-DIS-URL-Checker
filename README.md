# FAB-DIS-URL-Checker
URL Checker for FAB-DIS file

## Purpose of the script :
This script allows you to check the list of URLs present in a FAB-DIS referentiel.  
Fab-Dis is the name of a standardised Excel file format for the exchange of product data between FABricants and DIStributors in the French building industry (electricity, sanitation, heating and ventilation). 
Each URL is tested with simple request, if the HTTP code is not 200 then the URL is saved to a file for correction. 
Each FAB-DIS file has the same format. So this script is normally able to work with all FAB-DIS files.

## Requirements :
Developed with python version 3.9.0  
Necessary package : openpyxl, requests, click, progress.bar

## Installation of dependencies :
```
pip install openpyxl requests click progress
```

## How to use :
Get the help :
```
python fabdis_url_checker.py --help
```

Run the script :
```
python fabdis_url_checker.py -f FAB-DIS_file.xlsx -s 03_MEDIA -c G
```

-f (file) : FAB-DIS file name in xlsx format. Example : "FAB-DIS_file.xlsx".  
-s (sheet): Sheet name to check in FAB-DIS file. Example : "03_MEDIA".  
-c (column): Column ID of url list to check. Example : "G".  

Example of use: 

```
python fabdis_url_checker.py -f FAB-DIS_test.xlsx -s 03_MEDIA -c G

Loading file FAB-DIS_test.xlsx
Please wait...
FAB-DIS_test.xlsx is loaded
Number of URL to check: 5
Processing |################################| 5/5
Number of URLs in error: 1
You can see the result in the file http_check_status.txt
```

## Run with docker : 

### Clone this repo in your working dir :
```
cd workdir
git clone https://github.com/Gati0/FAB-DIS-URL-Checker.git
cd FAB-DIS-URL-Checker
# Paste your FAB-DIS file here
```

### Create docker image from Dockerfile :
```
sudo docker build -t fab-dis_checker .
```

### Start the script inside the container :
##### You have to mount a volume.

```
sudo docker run --name FAB-DIS_Checker -v workdir/FAB-DIS-URL-Checker:/home/FAB-DIS:rw -d fab-dis_checker -f /home/FAB-DIS/FAB-DIS_file.xlsx -s 03_MEDIA -c G
```

--name : The container will have the name : FAB-DIS_Checker.  
-v : Mount you local volume on the container : local volume workdir/FAB-DIS-URL-Checker to /home/FAB-DIS on container (wr for read and write).  
-d : for detach.  
-f, -s, -c are the argument for the python script.  

The logs of script can be seen with the command :
```
docker logs -f containerid
```

The result file will be in your workdir.