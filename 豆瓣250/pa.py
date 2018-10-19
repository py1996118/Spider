from urllib.request import urlopen

import re

top = 1
top_url=[]
url = 'https://movie.douban.com/top250?start='

for num in range(4):
    top_url.append(url+str(num*25))

for i in top_url:
    html = urlopen(i).read().decode('utf-8')
    pattern = re.compile(r'<span class="title">(.*)</span>')
    data_str = re.findall(pattern,html)
    for i in data_str:
        if i.find('/') == -1:
            print('top'+str(top)+' '+i)
            top += 1
