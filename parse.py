import requests
from bs4 import BeautifulSoup
url="http://quotes.toscrape.com/"
response=requests.get(url)
soap=BeautifulSoup(response.text,'lxml')
print(soap)