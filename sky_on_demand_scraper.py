from urllib.request import urlopen
from urllib.error import HTTPError
import time
import string
import csv
from bs4 import BeautifulSoup

def is404(text):
    if "div.alert404" in text:
        return True
    else:
        return False

def stripTitles(text):
    titles = []
    tmp = ""
    for item in text.split("\n"):
        if "locandina_hover" in item:
            tmp = item.split('"')[5]
        if "film-locandinaspan-small" in item:
            tmp2 = item.split('"')[2]
            if tmp2[1:4].isalpha():
                nation = tmp2[1:4]
            else:
                nation = ""
            if tmp2[-11:-7].isdigit():
                year = tmp2[-11:-7]
            else:
                year = ""
            titles.append([tmp, year, nation])
    return titles

base = 'http://skygo.sky.it/ondemand/categorie/cinema/a-z/240_%s_%s.inc'
options = ['09'] + list(string.ascii_uppercase)
# options = ['A']
urls = []

titles = []

for opt in options:
    i = 1
    while(True):
        url = base % (opt, i)
        try:
            page = urlopen(url)
        except HTTPError as e:
            if e.code == 404:
                # print("404 found")
                break
        time.sleep(1)
        content = str(BeautifulSoup(page, 'html.parser'))
        print(url)
        titles += stripTitles(content.strip("\n"))
        i += 1
            
# print(titles) 

out = csv.writer(open("sky_on_demand.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
for row in titles:
    out.writerow(row)
