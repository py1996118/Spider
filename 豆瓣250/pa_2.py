import requests

from bs4 import BeautifulSoup

#<span class="title">(.*)</span>'

url = 'https://movie.douban.com/top250?start='

urls = [ url + str(num*25) for num in range(4)]

top_num = 1

for url in urls :
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html,'html.parser')
    movies = soup.find_all('span',class_='title')
    for i in movies:
        if i.text.find('/') == -1:
            print('top'+str(top_num)+' '+i.text)
            top_num += 1
