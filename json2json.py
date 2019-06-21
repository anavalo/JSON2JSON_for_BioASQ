import requests
import json
from pathlib import Path


with open(Path('data', 'trainining7b.json')) as jsonf:
    data = json.load(jsonf)

questions = data['questions']

factoids = []
for i in questions:
    if i['type'] == 'factoid':
        factoids.append(i)


