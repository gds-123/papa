import json
from urllib import request as ru, parse, request
from lxml import etree
import MySQLdb
import requests

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user="root",
    password="123456",
    db="no_3",
    charset="utf8"
)
cursor = conn.cursor()


#获取列表

class GetList:
    def __init__(self,url,num,head):
        self.url=url
        self.num=num
        self.head=head
    def getulrs(self):
        req = ru.Request(self.url,headers=self.head)
        res = ru.urlopen(req).read().decode("utf-8")
        print(res)
        result = json.loads(res)
        url_list=[]
        for j in result["data"]["results"]:
            # url_list.append(j["positionURL"])

            head = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                              "55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36",
                "referer":j["positionURL"]
            }
            print(j["positionURL"])
            GetDetails(j["positionURL"], head).getdatails()

#获取详情页
class GetDetails:
    def __init__(self,url,head):
        self.url=url
        self.head=head

    def getdatails(self):
        result = requests.get(self.url,headers=self.head).text
        # result = ru.urlopen(self.url).read().decode("utf-8")
        ele = etree.HTML(result)
        try:
            titel = ele.xpath("//h3//text()")[0]

            salary = ele.xpath("//div[@class='summary-plane__left']/span/text()")[0]
            lightspot1 = ele.xpath("//div[@class='highlights__content']/span/text()")
            lightspot = ""
            for j in lightspot1:
                lightspot += j
            workplace = ele.xpath("//div[@class='job-address__content']/span/text()")[0]
            working_area = ele.xpath("//ul/li/a/text()")[0]
            working_time = ele.xpath("//ul/li/text()")[0]
            education = ele.xpath("//ul/li/text()")[1]
            peoples = ele.xpath("//ul/li/text()")[2]
            describe = ele.xpath("//div[@class='describtion__detail-content']//text()")
            describe1 = ""
            for i in describe:
                describe1 += i.strip()

            print(titel, salary, lightspot, workplace, working_area, working_time, education, peoples, describe1)
            SaveText(titel, salary, lightspot, workplace, working_area, working_time, education, peoples, describe1).save()

        except:
            pass


#写入
class SaveText:
    def __init__(self,titel, salary, lightspot, workplace, working_area, working_time, education, peoples, describe1):
        self.titel=titel
        self.salary=salary
        self.lightspot=lightspot
        self.workplace=workplace
        self.working_area=working_area
        self.working_time=working_time
        self.education=education
        self.peoples=peoples
        self.describe1=describe1
    def save(self):
        with open("newjobs.txt", "a", encoding="utf-8") as w:
            w.write(
                "工作：" + self.titel + "\n" + "工资：" + self.salary + "\n" + "职位亮点：" + self.lightspot + "\n" + "工作地点：" + self.workplace + "\n" + "公司区域：" + self.working_area + "\n" + "经验要求：" + self.working_time
                + "\n" + "学历：" + self.education + "\n" + "招聘人数：" + self.peoples + "\n" + "职位描述：" + self.describe1 + "\n"
            )





if __name__ == '__main__':
    adress = ["530", "538", "765", "763"]
    position1 = ["爬虫", "web", "AI", "JAVA", "大数据"]
    head={

    }
    for i in adress:

        for j in position1:
            print(j,"!!!!")
            num = 0
            j = parse.quote(j)
            while 1:
                num += 90
                print(j)

                # try:
                url = "https://fe-api.zhaopin.com/c/i/sou?start=" + str(num) + "&pageSize=90&cityId=" + str(
                    i) + "&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=" + str(
                    j) + "&kt=3&=0&_v=0.34331922&x-zp-page-request-id=b3049e4c15644d22bf1afb5183ddb043-1564998589572-795041&x-zp-client-id=f997901b-58ce-48e6-9fb5-bd0e0f856692"

                head = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                                  "55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36"

                }

                req=ru.Request(url,headers=head)
                res = ru.urlopen(req).read().decode("utf-8")
                result = json.loads(res)
                try:
                    count_all = result["data"]["count"]
                    print(count_all,num)
                except:
                    break

                getlist = GetList(url, num,head).getulrs()

                # except:
                #     print("cuole")
                #     break
