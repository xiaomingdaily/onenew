#coding=utf-8
## 说明：
## 【20190719】日常查询每日官网公告
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time,sys,requests,json
import time,re

# TODO:
# 1. 20190519 - 联动串并市值指标？（数据串并）
# 2. 20190519 - 只看关注列表中公司？（加白名单）
reload(sys)
sys.setdefaultencoding('utf-8')
def passkeywords(line):
   if "银行" in line or "问询函" in line or  "转债" in line or  "年度报告" in line or  "权益变动" in line or "可转换" in line :
       return(True)
   else:
       return(False)
def main():
    ##headless
    options=webdriver.ChromeOptions()
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()

    driver.get("http://www.sse.com.cn/disclosure/listedinfo/announcement/")
    time.sleep(3)
    js="var q=document.documentElement.scrollTop=1000000"
    driver.execute_script(js)
    time.sleep(3)
    titles = driver.find_elements_by_xpath('//*[@id="panel-1"]/div[1]/dl/dd[*]/em/a')
    for i in range(len(titles)):
        if passkeywords(titles[i].text) == True:
            print(titles[i].text + " - " + titles[i].get_attribute("href"))
    print("----------------------------------------------------------")
    #time.sleep(3)
    url = "http://www.szse.cn/disclosure/listed/bulletinDetail/index.html?"
    r=requests.get("http://www.szse.cn/api/disc/announcement/detailinfo?random=0.4121872967066069&pageSize=10000&pageNum=1&plateCode=szse")
    time.sleep(3)
    r.json()
    items = json.loads(r.text)['data']
    for item in items:
        company = item['secCode']
        announList = item['announList']
        for announ in announList:
            if passkeywords(announ['title']):
                print(company+"： " +announ['title'] + " - " + url+announ['id'])
    driver.quit()

start = time.time()
main()
end = time.time()
print(end-start)
