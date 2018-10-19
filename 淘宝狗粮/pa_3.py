import re
from urllib.parse import quote
from urllib.request import urlopen

keyword = "狗粮"
url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8'.format(quote(keyword))

html = urlopen(url).read().decode('utf-8')

regex = re.compile(r'<li data-sku=".*" class="gl-item">[\s\S]*?</li>')

title_regex = re.compile(r'<div class="p-img">[\s\S]*?<a target="_blank" title="(.*?)" href=".*"')

#title_regex = re.compile(r'<a target="_blank" title="(.*)" href=".*"')
img_regex = re.compile(r'<img width=".*" height=".*"[\s\S]*?source-data-lazy-img="(.*)"')
money_regex = re.compile(r'<em>(￥)</em><i>(.*?)</i>')

patt = re.findall(regex,html)
count = 1
for i in patt:
    print(count)
    print("title:" + re.findall(title_regex,i)[0])
   # print("http:" + re.findall(img_regex,i)[0])
   # print(" ".join(re.findall(money_regex,i)[0]))
    count += 1