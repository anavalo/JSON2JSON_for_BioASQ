import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import json
from pathlib import Path
from bs4 import BeautifulSoup as bs
import argparse



def get_abstract(url):
    try:
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        data = session.get(url)
        soup = bs(data.text, 'html.parser')
        text = [p.text for p in soup.find_all('div', attrs={'class': 'abstr'})]
        final = text[0].replace('Abstract', '')
        return final
    except IndexError:
        print(url)



documents = [
            "http://www.ncbi.nlm.nih.gov/pubmed/19477402",
            "http://www.ncbi.nlm.nih.gov/pubmed/19740409",
            "http://www.ncbi.nlm.nih.gov/pubmed/23376948",
            "http://www.ncbi.nlm.nih.gov/pubmed/22128204",
            "http://www.ncbi.nlm.nih.gov/pubmed/19784900",
            "http://www.ncbi.nlm.nih.gov/pubmed/20688032",
            "http://www.ncbi.nlm.nih.gov/pubmed/18204915",
            "http://www.ncbi.nlm.nih.gov/pubmed/22135401",
            "http://www.ncbi.nlm.nih.gov/pubmed/12224720",
            "http://www.ncbi.nlm.nih.gov/pubmed/19808288",
            "http://www.ncbi.nlm.nih.gov/pubmed/22498326",
            "http://www.ncbi.nlm.nih.gov/pubmed/22348519",
            "http://www.ncbi.nlm.nih.gov/pubmed/21234292",
            "http://www.ncbi.nlm.nih.gov/pubmed/15861263",
            "http://www.ncbi.nlm.nih.gov/pubmed/21498307",
            "http://www.ncbi.nlm.nih.gov/pubmed/20339815",
            "http://www.ncbi.nlm.nih.gov/pubmed/19474054",
            "http://www.ncbi.nlm.nih.gov/pubmed/22687593",
            "http://www.ncbi.nlm.nih.gov/pubmed/20079992",
            "http://www.ncbi.nlm.nih.gov/pubmed/20667520",
            "http://www.ncbi.nlm.nih.gov/pubmed/20102955",
            "http://www.ncbi.nlm.nih.gov/pubmed/18208827",
            "http://www.ncbi.nlm.nih.gov/pubmed/18562248",
            "http://www.ncbi.nlm.nih.gov/pubmed/22935464"
         ]

for i in documents:
    print(get_abstract(i))