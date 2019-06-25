import requests
import json
from pathlib import Path
import beautifulsoup4




with open(Path('data', 'trainining7b.json')) as jsonf:
    data = json.load(jsonf)['questions']



paragraphs = []
dictionary = {'context':'', 'qas': [{'question':'', 'id': ''}]}

for i in data:
    if i['type'] == 'factoid':
        dictionary['context'] = i['body']

    paragraphs.append(dictionary)

def get_abstract(url):
    data = requests.get(url)
    soup = beautifulsoup4(data.text, parser)
    for p in soup.find_all('p'):
        print(p)

get_abstract('https://www.ncbi.nlm.nih.gov/pubmed/12239580')