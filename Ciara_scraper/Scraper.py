import sys
import requests as rq
from bs4 import BeautifulSoup as bs
from time import sleep
from time import time
from random import randint
from warnings import warn
import json


## Creating a loop to scrape from all pages

news_title = []
news_source = []
news_link = []

#pages = [str(i) for i in range(1,371)]

reqs = 0

start_time = time()

# for url in url_list:
    
full_url = "https://web.archive.org/web/20060516073626/http://www.emporis.com/en/bu/sk/st/ma/ct/co/ci/?id=100053"

#open page
try:
    pg = rq.get(full_url).text
except urllib.error.HTTPError as e:
    print('Error: {}'.format(e))
except urllib.error.URLError as e:
    print('Error: {}'.format(e.reason))
    

# parse html using beautifulsoup and store in soup
soup = bs(pg,'html.parser')
#find all news containers
articles = soup.find_all('a')
muhlinks = [i for i in articles  if "en/wm/ci" in i["href"]] # gets city level
#for i in muhlinks
#link = i["href]"]
link = muhlinks[0]
nextlunk = "https://web.archive.org/" + link["href"]
pg = rq.get(nextlunk).text
soup = bs(pg,'html.parser')
articles = soup.find_all('a')
answer = [i for i in articles  if "ci/bu/sk" in i["href"]] 
nextlink =  answer[0]["href"] 
nextlink = nextlink[:59] + "li/" + nextlink[59:] + "&bt=2&ht=2&sro=1"
nextlink = "https://web.archive.org/" + nextlink

pg = rq.get(nextlink).text
soup = bs(pg,'html.parser')
articles = soup.find_all('a')
pagelinks = [i for i in articles  if "en/wm/bu" in i["href"]] 
nextpage = [i for i in articles  if "sro" in i["href"]][0]["href"]

breakpoint()

#
#TODO query city buildings then high rise buildings , then all buildings#

# import pandas as pd
# def get_wayback_urls(urls, from_date, to_date):
#     wayback_api_url = "http://web.archive.org/cdx/search/cdx"
#     available_urls = {}

#     for url in urls:
#         params = {
#             "url": url,
#             "from": from_date,
#             "to": to_date,
#             "output": "json",
#             "fl": "timestamp,original",
#             "filter": ["statuscode:200"],
#             # "collapse": "timestamp:4"   # 1 capture per year
#         }
#         response = requests.get(wayback_api_url, params=params)
#         data = response.json()

#         url_dict = {
#             item[0]: f"http://web.archive.org/web/{item[0]}/{item[1]}"
#             for item in data[1:]
#         }
        
#         available_urls.update(url_dict)

#     return available_urls

# def main():
#     urls = [
#         "https://www.inmuebles24.com/departamentos-en-renta.html", 
#         "https://www.inmuebles24.com/departamentos-en-baja-california-norte.html",
#         "https://www.inmuebles24.com/desarrollos-o-departamentos.html"
#     ]
#     from_date = "20100101"  # YYYYMMDD
#     to_date = "20231231"  # YYYYMMDD
#     wayback_urls = get_wayback_urls(urls, from_date, to_date)

#     print(wayback_urls)
#     print(len(wayback_urls.keys()))

# if __name__ == "__main__":
#     main()