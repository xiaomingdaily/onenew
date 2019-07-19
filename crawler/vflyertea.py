#coding=utf-8
## 说明：
## 【20190129】查询浦发飞客平台情报信息
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
def main(url,moreinfo):
    ##headless
    options=webdriver.ChromeOptions()
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--headless')
    driver=webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Chrome()

    fp = open("D:/active-scan-plus-plus/xinyongka.txt","a+")
    fp.write(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    fp.write(" -- " + moreinfo)
    fp.write("\n")

    driver.get(url)
    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    for i in range(3):
        time.sleep(0.7)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,('//*[@id="autopbn"]'))))
            driver.find_element_by_xpath('//*[@id="autopbn"]').click()
        except:
            pass

    titles = driver.find_elements_by_xpath("//tr/td/div/h2/div/span/a[2]")
    for i in range(len(titles)):
        if "删帖" not in titles[i].text and "【" not in titles[i].text and "广告" not in titles[i].text:
            print("["+moreinfo +"]"+titles[i].text+" - " + titles[i].get_attribute("href"))
            fp.write(titles[i].text)
            fp.write(" - ")
            fp.write(titles[i].get_attribute("href"))
            fp.write("\n")
    fp.close()
    driver.quit()

# main("https://www.flyertea.com/forum-priorityclub-1.html","IHG")
# main("https://www.flyertea.com/forum-marriott-1.html","万豪")
# main("https://www.flyertea.com/forum-Hilton-1.html","希尔顿")
# main("https://www.flyertea.com/forum-Donghang-1.html","东航")
# main("https://www.flyertea.com/forum-HainanAirlines-1.html","海航")
# main("https://www.flyertea.com/forum-ChinaSouthern-1.html","南航")
# main("https://www.flyertea.com/forum-Cathaypacific-1.html","国泰")
main("https://www.flyertea.com/forum-pufa-1.html","浦发")
main("https://www.flyertea.com/forum-zhaoshang-1.html","招行")
main("https://www.flyertea.com/forum-guangfa-1.html","广发")
main("https://www.flyertea.com/forum-zhongxin-1.html","中信")
main("https://www.flyertea.com/forum-zhonghang-1.html","中行")
main("https://www.flyertea.com/forum-mingsheng-1.html","民生")
main("https://www.flyertea.com/forum-xingye-1.html","兴业")
main("https://www.flyertea.com/forum-nongye-1.html","农业")
main("https://www.flyertea.com/forum-jianshe-1.html","建行")
main("https://www.flyertea.com/forum-wuka-1.html","无卡支付")
