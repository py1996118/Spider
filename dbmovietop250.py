import requests
import re
from lxml import etree
import csv
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

fp = open('G:\CSV\movie.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('name','director','actor','style','country','release_time','time','score'))

def get_movie(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    movie_hrefs = selector.xpath('//div[@class="hd"]/a/@href')
    for movie_href in movie_hrefs :
        get_movie_info(movie_href)


def get_movie_info(url):
    html = requests.get(url,headers=headers)
    selector = etree.HTML(html.text)
    try:
        name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]
        director = selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors = selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        actor = actors.xpath('string(.)')
        style = re.findall('<span property="v:genre">(.*?)</span>',html.text,re.S)
        country = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>',html.text,re.S)[0]
        release_time = re.findall('上映日期:</span>.*?>(.*?)</span>',html.text,re.S)[0]
        time = re.findall('片长:</span>.*?>(.*?)</span>',html.text,re.S)[0]
        score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0]
        print(name,country,release_time,time,score)
        writer.writerow((name,director,actor,style,country,release_time,time,score))
    except IndexError:
        pass

if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls :
        get_movie(url)
        time.sleep(1)
fp.close()
