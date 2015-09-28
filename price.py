from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import re

# "toronto", ottawa, montreal.en, calgary, edmonton, hamilton, winnipeg, victoria, reddeer, kamloops, kelowna, nanaimo, sunshine, whistler, abbotsford, halifax, lethbridge, hat, peace, ftmcmurray, cariboo, comoxvalley, cranbrook, princegeorge, skeena, newbrunswick, newfoundland, yellowknife, barrie, belleville, brantford, chatham, cornwall, guelph, hamilton, kingston, kitchener, londonon, niagara, owensound, peterborough, sarnia, soo, sudbury, thunderbay, windsor, pei, quebec, saguenay, sherbrooke, troisrivieres, regina, saskatoon, whitehorse 

# cat *.csv >merged.csv 

cpages = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24" ]

# cities = ["hamilton", "winnipeg", "reddeer",  -> "sunshine", "whistler", "abbotsford", "halifax", "lethbridge", "hat", "peace", "ftmcmurray", "cariboo", "comoxvalley", "cranbrook", "princegeorge", "skeena", "newbrunswick", "newfoundland", "yellowknife", "barrie", "belleville", "brantford", "chatham", "cornwall", "guelph", "hamilton", "kingston", "kitchener", "londonon", "niagara", "owensound", "peterborough", "sarnia", "soo", "sudbury", "thunderbay", "windsor", "pei", "quebec", "saguenay", "sherbrooke", "troisrivieres", "regina", "saskatoon", "whitehorse"]
# cities = ["toronto", "ottawa", "montreal.en", "calgary", "edmonton", "kamloops", "kelowna", "victoria", => "nanaimo"]


cities = ["toronto", "ottawa", "montreal.en"]

i=0

while i<len(cpages): 

    city=0

    while city<len(cities):

        base_url = ("http://"+ cities[city] +".craigslist.ca/search/rea?s="+ cpages[i] +"00&min_price=10000&sort=date")   

        soup = BeautifulSoup(urlopen(base_url).read())
        posts = soup.find_all("p", "row")
        post_urls = [p.a["href"] for p in posts]

        with open( cities[city] +"RE_price" + cpages[i] + ".csv", "w") as f:
            fieldnames = ("lat-lng", "price", "number of rooms")
            output = csv.writer(f)
            output.writerow(fieldnames)
            
            for url in post_urls:
                url = url.replace("http://"+ cities[city] +".craigslist.ca", "")  # inconsistent URL
                page = urlopen("http://"+ cities[city] +".craigslist.ca{0}".format(url))
                soup = BeautifulSoup(page.read()).find("section", "body")

        #lat&Lng   
                latlng = "N/A"
                latlng = soup.find_all("div", {"id": "map"})
                
        #price
                price = "N/A"
                for hit in soup.find_all(attrs={'class' : 'price'}):
                    price = hit.contents[0].strip()
                    print price

        #rooms
                rooms = "N/A"
                for hit in soup.find_all(attrs={'class' : 'housing'}):
                    rooms = hit.contents[0].strip()
                    print rooms

        #white in csv
                output.writerow([latlng, price, rooms ])
        city+=1
    i+=1 
            
       
