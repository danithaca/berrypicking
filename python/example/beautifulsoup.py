import urllib.request
from bs4 import BeautifulSoup
import re
import json

page = urllib.request.urlopen('http://www-01.sil.org/linguistics/GlossaryOfLinguisticTerms/contents.htm').read()
soup = BeautifulSoup(page, 'html.parser')
prefix = 'http://www-01.sil.org/linguistics/GlossaryOfLinguisticTerms/'
text_pattern = r'What (?:is|are) (?:a |an |the )?(.+)\?(.*)'
data = []

for link in soup.find_all('a'):
    text = link.get_text()
    href = link.get('href')
    if text.startswith('What') and href.startswith('What'):
        match = re.match(text_pattern, text)
        #print(text)
        extracted = (match.group(1) + match.group(2)).title()
        # print(extracted.title())
        full_url = prefix + href
        data.append({
            'term': extracted,
            'url': full_url
        })
        node = BeautifulSoup(urllib.request.urlopen(full_url).read(), 'html5lib')
        print(''.join([str(x) for x in node.body.contents]))
        break

with open('crawled.json', 'w') as f:
    json.dump(data, f)

