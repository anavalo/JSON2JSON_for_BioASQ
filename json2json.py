import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import json
from pathlib import Path
from bs4 import BeautifulSoup as bs

#function for retrieving abstracts from pubmed
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

with open(Path('data', 'trainining7b.json')) as jsonf:
    seven_b_data = json.load(jsonf)['questions']

paragraphs = []

# find the "factoid" indexes of training7b.json
idx = []
for i, j in enumerate(seven_b_data):
    if j['type'] == 'factoid':
        idx.append(i)

idx_counter = 0

for index in idx:
    idx_counter+=1
    print(str(idx_counter) + ' of ' + str(len(idx)) + ' factoids, ' + str((idx_counter)/len(idx)*100) + ' %')
    counter = 0
    for url in seven_b_data[index]['documents']:
        dict = {'context': get_abstract(url),
                'qas': [{'question': seven_b_data[index]['body'],
                         'id': (seven_b_data[index]['id']+'_'+str("%03d" % counter))}]}
        paragraphs.append(dict)
        print(counter)
        counter += 1


training7b = {'version': 'BioASQ7b', 'data': [{'title':'BioASQ7b'}]}
training7b['data'][0]['paragraphs'] = paragraphs

with open(Path('data', 'BioASQ-test-7b'), 'w') as f:
    json.dump(training7b, f, indent=2)











