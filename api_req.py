import requests
baseurl='https://api.upcitemdb.com/prod/trial/lookup'
param={'upc':'885909950805'}
response=requests.get(baseurl,params=param)
print (response.url)