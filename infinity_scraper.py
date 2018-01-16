from urllib.request import urlopen
from urllib.error import HTTPError
import time
import string
import csv
import json
from bs4 import BeautifulSoup

url = "https://www.infinitytv.it/AVS/besc?action=GetMenuItems&channel=PCTV&service=INFINITY&userClusterName=SUBSCRIBER"
raw = json.loads(urlopen(url).read())
options = []

for item in raw["resultObj"]["categoryList"][0]["categoryList"][1]["categoryList"]:
    options.append(item["categoryName"])

titles = []
base = 'https://www.infinitytv.it/AVS/besc?action=GetContentList&channel=PCTV&service=INFINITY&categoryId=1001380&contentType=CATEGORY_LEAF&callerPage=LEAFPAGE&categoryName=%s&callerPageName=CINEMA&orderBy=contentYear&sortDirection=desc&showSeries=Y&offset=%s'

for opt in options:
    i = 1
    while(True):
        url = base % (opt, i)

        try:
            page = urlopen(url)
        except HTTPError as e:
            if e.code:
                break


        time.sleep(1)
        raw = json.loads(urlopen(url).read())
        print(opt + " - " + str(i))

        if( raw["totalResult"] == 0 ):
            print("404 found")
            break;
        else:
            obj =  raw["resultObj"]["contentList"] 
            print("Total results: ", raw["totalResult"])
            for item in obj:
                titles.append([ item["contentTitle"], item["averageRating"], opt ])
            i += 1

out = csv.writer(open("infinity.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
for row in titles:
    out.writerow(row)
