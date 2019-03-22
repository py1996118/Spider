import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    ranks = soup.select('span.pc_temp_num')
    tittles = soup.select('div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank,tittle,ti in zip(ranks,tittles,times):
        data = {
            'rank': rank.get_text().strip(),
            'singer': tittle.get_text().split('-')[0],
            'song': tittle.get_text().split('-')[1],
            'time': ti.get_text().strip()
        }
        print(data)

if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
    time.sleep(1)
