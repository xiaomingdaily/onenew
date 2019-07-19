#coding=utf-8
## 说明：
## 【20190719】爬去juejin看别人在讨论什么新鲜事情。
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

    driver.get("https://juejin.im/timeline")
    for i in range(5):
        time.sleep(0.6)
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)

    titles = driver.find_elements_by_xpath('//*[@id="juejin"]/div[2]/main/div/div/div[1]/ul/li/div/div/a/div/div/div[2]/a')
    for i in range(len(titles)):
        print(titles[i].text + "- " + titles[i].get_attribute("href") )
    # time.sleep(10)
    driver.quit()

start = time.time()
main()
end = time.time()
print(end-start)
