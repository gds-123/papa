import json
import threading
from urllib import parse

import requests
from lxml import etree
import MySQLdb
headers={
    "referer": "https://so.dajie.com/job/search?keyword=JAVA&from=fulltimejob",
}



parmas={
    'keyword': 'python',
    'from': 'job',
    'clicktype': '-blank'

}

cookies = 0

url = "https://so.dajie.com/job/search?keyword=JAVA&from=fulltimejob"

def getlist():

    while 1:
        try:

            with requests.session() as c:
                c.get(url="https://so.dajie.com/job/search", params=parmas, )
                # print("!!!!!!!!!!!",c.cookies)
                cookies = c.cookies
                print(cookies)
                if cookies:
                    res = requests.get(url=url,headers=headers,cookies=cookies).text
                    print(res)
        except:
            print(1121212)
            continue

getlist()
# class GetList:
#     def __init__(self,url,citys,works):
#         self.url=url
#         self.citys=citys
#         self.works=works
#         self.db = MySQLdb.connect(host="localhost", user="root", password="123456", db="no_3", charset="utf8",
#                                   port=3306, )
#         self.cursor = self.db.cursor()
#     def getlist(self):
#         cookies=0
#         while 1:
#             try:
#
#                 with requests.session() as c:
#                     c.get(url="https://so.dajie.com/job/search", params=parmas,)
#                     # print("!!!!!!!!!!!",c.cookies)
#                     cookies = c.cookies
#                     print(cookies)
#
#
#                  res = requests.get(url=url,headers=headers,cookies=cookies).text
#
#             except:
#                 print(1121212)
#                 continue
#         for i in reversed(self.citys):
#             num = 5
#             for j in reversed(self.works):
#                 print(j,i)
#                 page = 10
#
#                 j = parse.quote(j)
#                 while num<=page:
#                     print(num,page)
#                     url = self.url.format(j,i,num)
#                     # url = self.url.format(j,citys,num)
#                     try:
#                         print(cookies)
#                         res = requests.get(url=url,headers=headers,cookies=cookies).text
#                     except:
#
#                         print(111111111123423423423)
#                         # with requests.session() as c:
#                         #     c.get(url="https://so.dajie.com/job/search?keyword=JAVA&from=fulltimejob",params=parmas,headers=headers1)
#                         #     # print("!!!!!!!!!!!",c.cookies)
#                         #     cookies = c.cookies
#
#                         continue
#                     # print(res)
#
#                     res=json.loads(res)
#                     page = int(res["data"]["totalPage"])
#                     # print(res["data"]["list"])
#                     for x in res["data"]["list"]:
#                         GetDetails("http:"+str(x["jobHref"]),self.db,self.cursor).getdetails()
#                     self.db.commit()
#                     num += 1
#                 num = 0
#                 print("SB Pycharm 存入成功")
#
#
# class GetDetails:
#     def __init__(self,url,db,cursor):
#         self.url = url
#         self.db = db
#         self.cursor = cursor
#
#     def getdetails(self):
#         try:
#             res = requests.get(self.url,headers=headers,cookies=cookies).text
#         except:
#             print(22222222222)
#             return
#
#         # res = requests.get(self.url,headers=headers,cookies=cookies).text
#         ele = etree.HTML(res)
#         try:
#             titel = ele.xpath("//span[@class='job-name']/text()")[0].strip()
#         except:
#             titel=""
#         try:
#             salary = ele.xpath("//span[@class='job-money']/em/text()")[0].strip()
#         except:
#             salary=""
#         try:
#             lightspot1 = ele.xpath("//div[@class='job-msg-bottom']/ul//li/text()")
#             lightspot=""
#             for i in lightspot1:
#                 lightspot+=i
#         except:
#             lightspot=""
#         try:
#             workplace =ele.xpath("//div[@class='ads-msg']//span[1]/text()")[0]
#         except:
#             workplace=""
#         try:
#             working_area = ele.xpath("//li[@class='ads']//span/text()")[0]
#         except:
#             working_area=""
#         try:
#             working_time = ele.xpath("//li[@class='exp']//span/text()")[0]
#         except:
#             working_time=""
#         try:
#             education = ele.xpath("//li[@class='edu']//span/text()")[0]
#         except:
#             education=""
#         try:
#             peoples = ele.xpath("//li[@class='recruiting']//span/text()")[0].split()
#             peoples = peoples[0] + peoples[1]
#         except:
#             peoples=""
#         try:
#             describe1 = ele.xpath("//div[@class='position-data ']//pre/text()")[0].strip()
#             # print(type(describe2))
#             # describe1 = ""
#             # for i in describe2:
#             #     describe1 += i
#         except:
#             describe1=""
#
#         SaveDB(self.db,self.cursor).savedb(peoples,working_area,working_time,workplace,education,titel,salary,describe1,lightspot,self.url,)
#




class SaveDB:
    def __init__(self,db,cursor):
        self.db=db
        self.cursor=cursor

    def savedb(self,peoples,working_area,working_time,workplace,education,titel,salary,describe1,lightspot,url):
        self.db.ping(True)
        print(url)
        try:
            sql = "insert into dajie(url,peoples,working_area,working_time,workplace,education,titel,salary,describe1,lightspot)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(sql,(url,peoples,working_area,working_time,workplace,education,titel,salary,describe1,lightspot))

        # self.cursor.execute(sql,("1","1","1","1","1","1","1","1","1","1"))
        except:
            print("存入失败")
            return








# if __name__ == '__main__':
#
#     def run(citys,works,url,i):
#
#         GetList(url,citys,works[i:]).getlist()
#
#     citys = [110000, 310000, 120000, 500000, 340000, 350000, 620000, 440000, 450000, 520000, 460000, 130000,
#                   410000, 230000, 420000,
#                   430000, 220000, 320000, 360000, 210000, 150000, 640000, 630000, 370000, 140000, 610000, 510000,
#                   540000, 650000, 530000,
#                   330000, 800000, 810000, ]
#     works = ["python", "java", "web", "大数据", "人工智能", "ui", "销售代表","电气工程师","大堂经理","建筑设计师","猎头顾问","网络客服","人力资源专员/助理"]
#     url = "https://so.dajie.com/job/ajax/search/filter?keyword={}&order=0&city={}&recruitType=&salary=&experience=&page={}&positionFunction=&_CSRFToken=&ajax=1"
#     for i in range(13):
#         threading.Thread(target=run,args=(citys,works,url,i)).start()
#
