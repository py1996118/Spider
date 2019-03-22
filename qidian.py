import requests
from lxml import etree
import os


class Spider(object):
    # def start_request(self):
    #     res = requests.get('https://www.qidian.com/all')
    #     xml = etree.HTML(res.text)
    #     bigtit_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/text()')
    #     bigsrc_list = xml.xpath('//div[@class="book-mid-info"]/h4/a/@href')
    #     for bigtit, bigsrc in zip(bigtit_list,bigsrc_list):
    #         if os.path.exists(bigtit) == False:
    #             os.mkdir(bigtit)
    #         self.next_file(bigtit,"https:"+bigsrc)
    #         print(bigtit,bigsrc)
    #         """进行一次就好"""
    #         break

    def next_file(self,bigtit, bigsrc):
        res = requests.get(bigsrc)
        xml = etree.HTML(res.text)
        zj_list = xml.xpath('//ul[@class="cf"]/li/a/text()')
        zjsrc_list = xml.xpath('//div[@class="volume"]/ul/li/a/@href')
        for zj, zjsrc in zip(zj_list, zjsrc_list):
            # if os.path.exists(bigtit+'/'+zj) == False:
            #     os.mkdir(bigtit+'/'+zj)
            self.get_text(zj, "https:"+zjsrc)

    def get_text(self, zj, zjsrc):
        res = requests.get(zjsrc)
        xml = etree.HTML(res.text)
        get_info = xml.xpath('//div[@class="read-content j_readContent"]/p/text()')
        for i in get_info:
            self.writer(zj, i)

    def writer(self, zj, text):
        with open('凡人修仙之仙界篇/'+zj+'.txt', 'a', encoding='utf-8',) as f:
            f.write(text+'\n')







spider = Spider()
# spider.start_request()
url = 'https://book.qidian.com/info/1010734492'
name = '凡人修仙之仙界篇'
spider.next_file(name,url)

# url= 'https://read.qidian.com/chapter/ORlSeSgZ6E_MQzCecGvf7A2/CkfURYYQdxNp4rPq4Fd4KQ2'
#
# spider.get_text(url)