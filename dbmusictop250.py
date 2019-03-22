import requests
import re
from lxml import etree
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

fp = open('G:\CSV\music.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('name','author','style','time','publisher','score'))

def get_music(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//a[@class="nbg"]/@href')
    for music_href in music_hrefs :
        get_music_info(music_href)


def get_music_info(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    # author = selector.xpath('//*[@id="info"]/span[1]/span/a/text()')
    author = re.findall('表演者:.*?>(.*?)</a>',html.text,re.S)[0]
    styles = re.findall('<span class="pl">流派:</span>&nbsp;(.*?)<br />',html.text,re.S)
    if len(styles) == 0 :
        style = ' 未知'
    else:
        style = styles[0].strip()
    time = re.findall('发行时间:</span>&nbsp;(.*?)<br />',html.text,re.S)[0].strip()
    publishers = re.findall('出版者:</span>&nbsp;(.*?)<br />',html.text,re.S)
    if len(publishers) == 0 :
        publisher = ' 未知'
    else:
        publisher = publishers[0].strip()
    score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    writer.writerow((name,author,style,time,publisher,score))
    # info = {
    #     'name': name,
    #     'author': author,
    #     'style': style,
    #     'time': time,
    #     'publisher': publisher,
    #     'score': score
    # }


if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls :
        get_music(url)
        time.sleep(2)
fp.close()
