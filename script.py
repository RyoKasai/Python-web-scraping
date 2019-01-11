import requests
from bs4 import BeautifulSoup
import json

r = requests.get('https://www.gooya.co.jp/news')
# HTMLを解析
soup = BeautifulSoup(r.content, "html.parser")

# 結果格納用
result = {'date': '', 'label': '', 'url': '', 'description': ''}
f = open('output.json', 'w')

for i in soup.select('#content > section.content__section.section__news > '\
                     'div.contents-list__wrap > div > div.c-half--gray.tile-height > div > div > section > dl'):
    date = i.select_one('dt').text.replace('.', '-')
    label = ''.join(i.get('class'))
    url = i.a.get('href')
    description = i.select_one('dd').text
    result.update(date=date, label=label, url=url, description=description)
    json.dump(result, f, ensure_ascii=False, indent='\t')
