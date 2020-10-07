import requests
from bs4 import BeautifulSoup as bs
stories=[]
def scrapee(url):
    req = requests.get(url)
    content = req.content
    soup = bs(content,'html.parser')
    stories.extend(soup.body.select('div',attrs={'id':'ins_storylist'}))
for i in range(1,10):
    (scrapee("https://www.ndtv.com/latest/page={}".format(str(i))))
print(len(stories))