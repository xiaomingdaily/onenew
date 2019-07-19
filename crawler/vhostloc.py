#coding=utf-8
## 说明：
## 【20190719】爬取hostloc论坛数据看别人在讨论什么新鲜事。
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
def main():
    # headless
    options=webdriver.ChromeOptions()
    # 提高效率
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()

    driver.get("https://www.hostloc.com/forum-45-1.html")
    for i in range(5):
        time.sleep(1)
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        driver.find_element_by_xpath('//*[@id="autopbn"]').click()

    titles = driver.find_elements_by_xpath("//*[contains(@id,'normalthread_')]/tr/th/a[3]")
    for i in range(len(titles)):
        print(titles[i].text + "- " + titles[i].get_attribute("href") )
    # time.sleep(10)
    driver.quit()

start = time.time()
main()
end = time.time()
print(end-start)
