import requests
import re
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def re_scraper(url):
    res = requests.get(url,headers=headers)
    ids =re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    for id,content in zip(ids,contents):
        info = {
            'id':id.strip(),
            'content':content.strip(),
        }
        return info

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,13)]
    start_1 = time.time()
    for url in urls:
        re_scraper(url)
    end_1 = time.time()
    print('one',end_1-start_1)
    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(re_scraper,urls)
    end_2 = time.time()
    print('two', end_2 - start_2)
    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(re_scraper,urls)
    end_3 = time.time()
    print('four', end_3 - start_3)