import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def judment_sex(class_name):
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'


def get_links(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get("href")
        get_info(href)


def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    tittles = soup.select('div.pho_info > h4')
    addresses = soup.select('span.pr5')
    prices = soup.select('div.day_l > span')
    sexs = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    for tittle,addresse,price,sex in zip(tittles,addresses,prices,sexs):

        data = {
            'tittle': tittle.get_text().strip(),
            'addresse': addresse.get_text().strip(),
            'price': price.get_text().strip(),
            'sex': judment_sex(sex.get("class"))
        }
        print(data)

if __name__ == '__main__':
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,2)]
    for url in urls:
        get_links(url)
        time.sleep(2)