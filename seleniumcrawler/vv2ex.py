#coding=utf-8
## 说明：
## 【20190719】每日监控与爬取vv2ex中的灌水信息。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
def main(keywords,url):
    # headless
    options=webdriver.ChromeOptions()
    # 提高效率
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()

    driver.get(url)
    for i in range(1):
        time.sleep(0.6)
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)

    titles = driver.find_elements_by_xpath('//*[@id="Main"]/div[2]/div/table/tbody/tr/td[3]/span[1]/a')
    for i in range(len(titles)):
        print("["+keywords+"]"+titles[i].text + "- " + titles[i].get_attribute("href") )
    # time.sleep(10)
    driver.quit()

start = time.time()
main("技术","https://www.v2ex.com/?tab=tech")
main("创意","https://www.v2ex.com/?tab=creative")
main("苹果","https://www.v2ex.com/?tab=apple")
main("工作","https://www.v2ex.com/?tab=jobs")
main("交易","https://www.v2ex.com/?tab=deals")
end = time.time()
print(end-start)
