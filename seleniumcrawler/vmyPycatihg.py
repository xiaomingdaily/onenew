#coding:utf-8
import requests,re,datetime
import json,sys
url = "https://apis.ihg.com.cn/guest-api/v1/ihg/cn/zh/searchLight"

# 20190809 - 提供V0.01版本，满足基本需求.

reload(sys)
sys.setdefaultencoding("UTF-8")
# 更新下面地点
#location = "杭州"
#cities = ["杭州"]
cities =["北京","上海","香港","深圳","成都","杭州","广州","南京","青岛","天津","苏州"]
#cities =["北京","上海","香港","深圳","成都","杭州","广州","南京","首尔","新加坡","特拉维夫","巴黎","伦敦","纽约州纽约","悉尼","莫斯科","加州旧金山","西雅图","加州洛杉矶","佛罗里达州奥兰多","东京","曼谷","三亚","苏州","大阪","巴厘岛","青岛","普吉岛","天津","冲绳"]
#在下面更新时间.
traveldate = "2019-08-12" # 只看一天价格
def calcpoints(location,traveldate):
    # print(location)
    city = location
    payload = {"version":"1.3","checkDailyPointsCost":"true","corporateId":"","stay":{"travelAgencyId":"99618455","rateCode":"","children":0,"adults":1,"rooms":1},"radius":30,"radiusUnit":"MI","bulkAvailability":False}
    payload["location"] = {"location":location}
    start = datetime.datetime.strptime(traveldate, '%Y-%m-%d')
    end = (start+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    payload["stay"]["dateRange"] = {"start":str(traveldate),"end":str(end)}
    headers={}
    headers['Content-Type']='application/json; charset=UTF-8'
    headers['X-IHG-API-KEY']='pQM1YazQwnWi5AWXmoRoA5FSfW0S9x8A'
    headers['X-IHG-MWS-API-Token']='58ce5a89-485a-40c8-abf4-cb70dba4229b'
    headers['Origin']='https://www.ihg.com.cn'
    headers['User-Agent']='Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    headers['Referer']='https://www.ihg.com.cn/hotels/cn/zh/find-hotels/hotel/list?fromRedirect=true&qAms=null&qSrt=sDD&qDest=hangzhou&setPMCookies=true&srb_u=1'

    resp = requests.post(url,data=json.dumps(payload),headers=headers)
    # print(resp.content)
    hotels = json.loads(resp.content)
    for item in hotels['hotels']:
        rewardNightAvailableStatus = str(item['rewardNightAvailableStatus'])
        if rewardNightAvailableStatus == "False":
            continue
        dailyPointsCost = str(item['dailyPointsCost'])
        rateRange  =  str(item['rateRange']['low'])
        value = str(item['rateRange']['low']*10000/int(item['dailyPointsCost']))
        try:
            print(city + "," + rewardNightAvailableStatus+","+item['hotelCode']+"," + dailyPointsCost + ","+ rateRange +"," + value + ","+item['name'].replace(","," "))
        except:
            print(city + "," + rewardNightAvailableStatus+","+ item['hotelCode']+","+ dailyPointsCost + "," + rateRange + "," + value)


print(u"城市,可兑换状态,酒店代号，需要积分，价格，每万积分价值")			
for city in cities:
    try:
        calcpoints(city,traveldate)
    except:
        print(city + " Error")