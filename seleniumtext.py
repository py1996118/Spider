from selenium import webdriver
import time


url = 'https://www.jianshu.com/p/ee0bb2f5965a'


def get_info(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # author = driver.find_element_by_xpath('//span[@class="name"]/a').text
    time.sleep(2)
    # print(driver.page_source)
    author = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span/a').text
    data = driver.find_element_by_xpath('//span[@class="publish-time"]').text.strip('*')
    word = driver.find_element_by_xpath('//span[@class="wordage"]').text
    view = driver.find_element_by_xpath('//span[@class="views-count"]').text
    comment = driver.find_element_by_xpath('//span[@class="comments-count"]').text
    like = driver.find_element_by_xpath('//span[@class="likes-count"]').text
    print(author, data, word, view, comment, like)
    # print(like)
    driver.quit()


get_info(url)






# driver = webdriver.Chrome()
# driver.get('https://www.douban.com/')
# driver.set_window_position(20, 40)
# driver.set_window_size(1000,600)
# driver.switch_to.frame(0)
# driver.find_element_by_class_name('account-tab-account').click()
# driver.find_element_by_id('username').clear()
# driver.find_element_by_id('username').send_keys('111111111111')
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('password').send_keys('123123123123')



# driver = webdriver.PhantomJS()
# driver.get('https://qzone.qq.com/')

# driver.switch_to.frame('login_frame')
# driver.find_element_by_id('switcher_plogin').click()
# driver.find_element_by_id('u').clear()
# driver.find_element_by_id('u').send_keys('479692863')
# driver.find_element_by_id('p').clear()
# driver.find_element_by_id('p').send_keys('')
# driver.find_element_by_class_name('btn').click()
# time.sleep(5)
# print(driver.page_source)
# driver.quit()

