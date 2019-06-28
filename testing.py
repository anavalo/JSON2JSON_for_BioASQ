import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from bs4 import BeautifulSoup as bs

def get_abstract(url):
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    data = session.get(url)
    soup = bs(data.text, 'html.parser')
    text = [p.text for p in soup.find_all('div', attrs={'class':'abstr'})]
    final = text[0].replace('Abstract', '')
    return final


print(get_abstract('https://www.ncbi.nlm.nih.gov/pubmed/19390085'))