#coding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys
import time
# 【20190719】日常爬取sec-wiki上数据情报，以便分析关注
reload(sys)
sys.setdefaultencoding('utf-8')
def main():
    ##headless
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()

    driver.get("https://www.sec-wiki.com/event")
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    titles = driver.find_elements_by_class_name("links")
    for i in range(len(titles)):
        print(titles[i].text+"-"+titles[i].get_attribute("href"))

    driver.get("https://www.sec-wiki.com/news")
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    titles = driver.find_elements_by_class_name("links")
    for i in range(len(titles)):
    	print(titles[i].text+"-"+titles[i].get_attribute("href"))
    driver.quit()
main()
