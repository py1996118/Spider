from selenium import webdriver
import time
import csv
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
qq_shuo = mydb['qzone']

driver = webdriver.Chrome()


def get_info(qq):
    driver.get('https://user.qzone.qq.com/{}/311'.format(qq))
    driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('***********')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('**********')
        driver.find_element_by_class_name('btn').click()
        time.sleep(2)
    driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
    except:
        b = False
    if b == True:
        try:
            time.sleep(2)
            driver.switch_to.frame('app_canvas_frame')
            contents = driver.find_elements_by_xpath('//pre[@class="content"]')
            times = driver.find_elements_by_xpath('//a[@class="c_tx c_tx3 goDetail"]')
            for content, tim in zip(contents, times):
                data = {
                    'time': tim.text,
                    'content': content.text
                }
                qq_shuo.insert_one(data)
        except:
            pass


if __name__ == '__main__':
    qq_lists = []
    fp = open('C:/Users/ASUS-PC/Desktop/QQmail.csv',encoding='utf-8')
    reader = csv.DictReader(fp)
    for row in reader:
        qq_lists.append(row['电子邮件'].split('@')[0])
    fp.close()
    for item in qq_lists:
        get_info(item)
driver.close()