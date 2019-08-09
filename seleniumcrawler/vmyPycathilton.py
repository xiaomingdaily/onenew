#coding:utf-8
import requests,re,datetime
# 一定要设置Content-Type值为application/json
#cities = ["wuxi","beijing","shanghai","hangzhou","suzhou","lijiang","guangzhou","xiamen","sanya"]
cities = ["Beijing","Shanghai","Chongqing","Sanya","Dalian","Guangzhou","Xiamen","Hefei","Xian","Shengyang","Hangzhou","Qingdao","Nanjing","putian","shijiazhuang","zhongshan","jiaxing","zhengzhou","shenzhen","wuhan","tianjin","taizhou","haikou","linzhi"]
#cities = ["guangzhou"]
fromdate = (datetime.datetime.now()+datetime.timedelta(days=30)).strftime("%Y-%m-%d")
todate = (datetime.datetime.now()+datetime.timedelta(days=31)).strftime("%Y-%m-%d")
#fromdate = "2019-05-01"
#todate = "2019-05-01"
traveldate = "2019-12-07"
fromdate = datetime.datetime.strptime(traveldate, '%Y-%m-%d')
todate = (fromdate+datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def calcpoints(param1,fromdate,todate):
    headers={}
    headers['Content-Type']='text/html'
    headers['User-Agent']='Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    url = ("https://www3.hilton.com//en_US/hi/search/findhotels/results.htm?arrivalDate=%s&departureDate=%s&hhonorsRate=true&numberOfAdults[0]=1&numberOfAdults[1]=1&numberOfAdults[2]=1&numberOfAdults[3]=1&numberOfAdults[4]=1&numberOfAdults[5]=1&numberOfAdults[6]=1&numberOfAdults[7]=1&numberOfAdults[8]=1&numberOfChildren[0]=0&numberOfChildren[1]=0&numberOfChildren[2]=0&numberOfChildren[3]=0&numberOfChildren[4]=0&numberOfChildren[5]=0&numberOfChildren[6]=0&numberOfChildren[7]=0&numberOfChildren[8]=0&numberOfRooms=1&sourcePage=OHW&view=List&query=%s"%(fromdate,todate,param1))
    # print(url)
    resp= requests.get(url,headers=headers)
    # print(resp.content)
    #blocks = re.findall("<div class=\"result_content\">(.*?).jpg\">",resp.content)

    blocks = re.findall("<div class=\"result\">(.*?)Standard Room Reward </span> </div> </div>",resp.content)

    for line in blocks:
        # print(line)
        price = re.findall("<span class=\"rate\">¥ (.*?)</span>",line)
        location = re.findall(" <h2>(.*?)</h2>",line)
        point = re.findall("<span class=\"points\">(.*?)</span>",line)
        sb = param1+","
        if len(location)>0:
            sb = sb + location[0].replace(",","").replace("&#x27;"," ")+","
        else:
            sb = "nolocation,"
        if len(price)>0:
            num1 = int(price[0].replace(",",""))
            sb = sb + price[0].replace(",","")+","
        else:
            sb = sb + "noprice,"
            continue
        if len(point)>0:
            num2 = int(point[0].replace(",",""))
            sb = sb + point[0].replace(",","")+","
        else:
            sb = sb + "nopoint"
            continue
        sb = sb + str(num1*10000/num2)
        print(sb)
print(u"酒店,价格，所需积分，每万积分价值")
for city in cities:
    try:
        calcpoints(city,fromdate,todate)
    except:
        print("Error while city="+city)
