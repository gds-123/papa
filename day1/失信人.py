import json
import requests
import MySQLdb
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    db="no_3",
    charset="utf8"
)
cursor=conn.cursor()
class Getlist:
    def __init__(self,url,head,count):
        self.url = url
        self.head = head
        self.count = count
    def getlist(self):
        try:
            res = requests.get(self.url,headers=self.head,timeout=10).text[46:-2]
        except:
            return
        print(res)
        jsonlist = json.loads(res)
        result=jsonlist["data"][0]["result"]
        for i in result:
            GetDetails(i,count).getdetails()



class GetDetails:
    def __init__(self, result,count):
        self.result = result
        self.count = count

    def getdetails(self):
        name = self.result["iname"]
        ID_card = self.result["cardNum"]
        court = self.result["courtName"]
        province = self.result["areaName"]
        gistId = self.result["gistId"]
        duty = self.result["duty"]
        performance = self.result["performance"]
        disruptTypeName = self.result["disruptTypeName"]
        publishDate = self.result["publishDate"]
        # print("当前第%d页"%self.count,name, ID_card, court, province, gistId, duty, performance, disruptTypeName, publishDate)
        # print("当前第%d页"%self.count,type(name), type(ID_card), type(court), type(province), type(gistId), type(duty), type(performance), type(disruptTypeName), type(publishDate))
        SaveText(name, ID_card, court, province, gistId, duty, performance, disruptTypeName, publishDate).savetext()


class SaveText:
    def __init__(self, name, ID_card, court, province, gistId, duty, performance, disruptTypeName, publishDate):
        self.name = name
        self.ID_card = ID_card
        self.court = court
        self.province = province
        self.gistId = gistId
        self.duty = duty
        self.performance = performance
        self.disruptTypeName = disruptTypeName
        self.publishDate = publishDate

    def savetext(self):
        # print(self.ID_card)
        select = "select ID_card from sxr1 where ID_card='%s'"%self.ID_card
        select1=cursor.execute(select)

        if select1==0:
            sql = "insert into sxr1(name,ID_card, court, province, gistId, duty, performance, disruptTypeName, publishDate)values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            self.name, self.ID_card, self.court, self.province, self.gistId, self.duty, self.performance,
            self.disruptTypeName, self.publishDate)
            cursor.execute(sql)
            conn.commit()





        # sql = "insert into sxr(name,ID_card, court, province, gistId, duty, performance, disruptTypeName, publishDate)values('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
        # self.name, self.ID_card, self.court, self.province, self.gistId, self.duty, self.performance,
        # self.disruptTypeName, self.publishDate)
        # cursor.execute(sql)
        # conn.commit()
        # cursor.close()
        # conn.close()



if __name__ == '__main__':
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
        "Referer":"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA%E6%9F%A5%E8%AF%A2&oq=%25E5%25A4%25B1%25E4%25BF%25A1%25E4%25BA%25BA&rsv_pq=daaa25400002ff10&rsv_t=d205ab%2FBD8w5elWm3RPw%2F2AcgdO2gJ20a0X8TGU4poij1bcUijN84O3P70g&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=1&rsv_sug7=100&bs=%E5%A4%B1%E4%BF%A1%E4%BA%BA"
    }
    page = 0
    num = 1565169744703
    count=0
    while 1:
        page += 10
        num += 1
        count+=1
        url="https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA%E6%9F%A5%E8%AF%A2&pn="+str(page)+"&rn=10&ie=utf-8&oe=utf-8&format=json&t=1565169751294&cb=jQuery110207570674464617735_1565169744702&_="+str(num)+""
        Getlist(url,head,count).getlist()
    # url="https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA%E6%9F%A5%E8%AF%A2&pn=70&rn=10&ie=utf-8&oe=utf-8&format=json&t=1565170264964&cb=jQuery110207570674464617735_1565169744702&_=1565169744711"
    # Getlist(url, head, count).getlist()
