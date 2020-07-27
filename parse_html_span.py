import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com/"
response=requests.get(url)
soap=BeautifulSoup(response.text,'lxml')
qoutes=soap.find_all('span',class_='text')
authors=soap.find_all('small',class_='author')
tags=soap.find_all('div',class_='tags')

for i in range(0,len(authors)):
    print(qoutes[i].text)
    print(authors[i].text)
    quotetags=tags[i].find_all('a',class_='tag')
    for quotetag in quotetags:
        print(quotetag.text)
