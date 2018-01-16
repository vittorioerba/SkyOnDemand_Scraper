from urllib.request import urlopen
from urllib.error import HTTPError
import csv
import json
import time
import unidecode
from past.builtins import execfile

execfile('tmdb_api.py')

# sky_db = {}
out = csv.writer(open("tmdb_votes.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)

with open('sky_on_demand.csv', 'r') as f:
    reader = csv.reader(f)
    sky_db_input = list(reader)

for row in sky_db_input:
    title = unidecode.unidecode(row[0])
    year = row[1]
    if title and year:
        print(title, "...")
        url = "https://api.themoviedb.org/3/search/movie?api_key=%s&language=it-IT&query=%s&year=%s" % (api_key, title.replace(" ", "%20"), year)
        raw = json.loads(urlopen(url).read())
        print("Total results: ", raw["total_results"])
        if (raw["total_results"]) > 0:
            data  = raw["results"][0]
            # sky_db[raw["title"]] =  data
            out.writerow([data["title"], data["release_date"][0:4], data["vote_average"], data["overview"], "SkyOnDemand"])
            time.sleep(0.5)


with open('infinity.csv', 'r') as f:
    reader = csv.reader(f)
    infinity_db_input = list(reader)

for row in infinity_db_input:
    title = unidecode.unidecode(row[0])
    if title:
        print(title, "...")
        url = "https://api.themoviedb.org/3/search/movie?api_key=%s&language=it-IT&query=%s" % (api_key, title.replace(" ", "%20"))
        raw = json.loads(urlopen(url).read())
        print("Total results: ", raw["total_results"])
        if (raw["total_results"]) > 0:
            data  = raw["results"][0]
            # sky_db[raw["title"]] =  data
            out.writerow([data["title"], data["release_date"][0:4], data["vote_average"], data["overview"], "Infinity"])
            time.sleep(0.5)



