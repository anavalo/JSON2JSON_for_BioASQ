import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup as bs
import time

#function for retrieving abstracts from pubmed
def get_abstract(url):
    data = requests.get(url)
    soup = bs(data.text, 'html.parser')
    text = [p.text for p in soup.find_all('p')]
    return text[9]

with open(Path('data', 'trainining7b.json')) as jsonf:
    seven_b_data = json.load(jsonf)['questions']

paragraphs = []

#find the "factoid" indexes of training7b.json
idx = []
for i, j in enumerate(seven_b_data):
    if j['type'] == 'factoid':
        idx.append(i)

for index in idx:
    counter = 0
    for url in seven_b_data[index]['documents']:
        dict = {'context': get_abstract(url),
                'qas': [{'question': seven_b_data[index]['body'],
                         'id': (seven_b_data[index]['id']+'_'+str("%03d" % counter))}]}
        paragraphs.append(dict)
        counter += 1
        time.sleep(0.30)

training7b










