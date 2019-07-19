#coding=utf-8
from selenium import webdriver
import os,time,sys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
reload(sys)
sys.setdefaultencoding('utf-8')
# 【20190719】爬取readhub获取最新咨询信息，可自己加规则去掉不关注内容。
def main():
    ##headless
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()
    driver.get("https://readhub.cn/topics")

    for i in range(6):
        js="var q=document.documentElement.scrollTop=1000000"
        driver.execute_script(js)
        time.sleep(1)

    titles = driver.find_elements_by_xpath('//*[@id="itemList"]//h2')
    links = driver.find_elements_by_xpath('//*[@id="itemList"]//h2/a')
    for i in range(len(titles)):
        print(titles[i].text + " - " + links[i].get_attribute("href"))
    driver.quit()

main()
