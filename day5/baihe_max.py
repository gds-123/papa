import threading

from lxml import etree

import requests,MySQLdb

conn = MySQLdb.connect(
        host="localhost",
        user="root",
        password="123456",
        db="no_3",
        charset="utf8",
        port=3306,
    )
cursor = conn.cursor()

cookies = {
        # "Cookie":"PHPSESSID=2fa53c7f99e248e402c3e41fe99e0468; SESSION_HASH=2357eb92dde523e96eb04577d879cf32f7d30621; accessID=20190809111852690209; ip_loc=11; user_access=1; jy_refer=sp0.baidu.com; pop_sj=0; _gscu_1380850711=65320733k4mb1716; _gscbrs_1380850711=1; main_search:219218582=%7C%7C%7C00; pop_avatar=1; stadate1=218218582; myloc=11%7C1113; myage=26; PROFILE=219218582%3A%25E6%2596%25B9%25E8%258A%25B3%25E8%258A%25B3%3Am%3Aimages1.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10%3A-5; mysex=m; myuid=218218582; myincome=10; RAW_HASH=ceJQOshtatwogI7Jx8MOud0b8%2AxhvEj5ZsA4T%2AhmEjYd2kCvAs9y39l86vKNnF9yeCpfTr4IdBNyStz%2ALMhzbouc1qAnAWhYHorUP48rxwO0r6Y.; COMMON_HASH=9a0242071ccda931d5d7365650212148; pop_time=1565338691508"
        "Cookie":"guider_quick_search=on; accessID=20190809111852690209; _gscu_1380850711=65320733k4mb1716; save_jy_login_name=13941646842; upt=DGc2FcCdlrnY%2AfbFr6AET40c6u15Xr3ZSVy2TXqR3PYOch8ZoJyhylJ8MrimVUlgs47vFO2SmZtX8Pex-sqg; user_access=1; SESSION_HASH=33dddcc65dbcda2d72853a85507b7b598b67bbf1; sl_jumper=%26cou%3D17%26omsg%3D0%26dia%3D0%26lst%3D2019-08-10; last_login_time=1565418661; user_attr=000000; PHPSESSID=e9980e0517710b26b1cf9c286f8a7387; pop_avatar=1; stadate1=218218582; myloc=11%7C1113; myage=26; PROFILE=219218582%3A%25E6%2596%25B9%25E8%258A%25B3%25E8%258A%25B3%3Am%3Aimages1.jyimg.com%2Fw4%2Fglobal%2Fi%3A0%3A%3A1%3Azwzp_m.jpg%3A1%3A1%3A50%3A10%3A3; mysex=m; myuid=218218582; myincome=10; main_search:219218582=%7C%7C%7C00; RAW_HASH=Uwq17D%2Ay4u6B0-KvidS7I-RSc2s91%2AC9oCKxL%2AiPsmWWIIUzsrIwsqOfdaEzgLpr8k0WrxCECcd8ZxQ8kEzF85CVSXi5va7WvqTLBof2MlqVfVI.; COMMON_HASH=9a0242071ccda931d5d7365650212148; is_searchv2=1"
    }

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36",
    "Referer":"http://search.jiayuan.com/v2/"
}


class GetIDList:
    def __init__(self, address, url):
        self.address = address
        self.url = url
    def getidlist(self):
        num= 0
        sql3 = "select * from count"
        cursor.execute(sql3)
        a = cursor.fetchone()
        print(self.address.index(a[0]), "]]]]]]]")

        if a:
            self.address = self.address[self.address.index(a[0]):]
            num = int(a[1]) - 1
        for i in self.address:
            print("城市%s" % i)

            page=10

            while num<page:
                print(i,num,page)
                data = {
                    'sex': ' f',
                    'stc':'1: ' + str(i) + ', 2: 19.50, 3: 155.180, 23: 1',
                    'sn': ' default',
                    'sv': '1',
                    'p': str(num),
                    'f': ' select',
                    'listStyle': ' bigPhoto',
                    'pri_uid': ' 219218582',
                    'jsversion': ' v5',
                }
                res = requests.post(url= self.url,data=data,headers=headers,cookies=cookies).json()
                page=res["pageTotal"]
                for x in res["express_search"]:
                    url = "http://www.jiayuan.com/" + str(x["realUid"])
                    GetDetails(url, x["realUid"]).getdatails()
                conn.commit()
                for j in res["userInfo"]:
                    url = "http://www.jiayuan.com/" + str(j["uid"])
                    GetDetails(url, j["realUid"]).getdatails()
                del1 = "delete from count"
                cursor.execute(del1)

                sele = "insert into count values (%s,%s)"
                cursor.execute(sele, (i, num))
                conn.commit()
                num += 1
            num = 0


class GetDetails:
    def __init__(self,url,id):
        self.url=url
        self.id=id


    def getdatails(self):
        print(self.url, "!!!!!")
        res = requests.get(self.url, headers=headers, cookies=cookies).text
        ele = etree.HTML(res)
        # print(res)
        try:
            name = ele.xpath("//div[@class='member_info_r yh']/h4/text()")[0]
        except:
            name = ""
        try:
            age = ele.xpath("//div[@class='member_info_r yh']/h6/text()")[0].split("，")[0]
        except:
            age = ""
        try:
            stature = ele.xpath("//div[@class='fl pr']//em/text()")[1]
        except:
            stature = ""
        try:
            education = ele.xpath("//div[@class='fl pr']//em/text()")[0]
        except:
            education = ""
        try:
            weight = ele.xpath("//div[@class='fl pr']//em/text()")[5]
        except:
            weight = ""
        try:
            constellation = ele.xpath("//div[@class='fl pr']//em/text()")[-6]
        except:
            constellation = ""
        try:
            nation = ele.xpath("//div[@class='fl pr']//em/text()")[7]
        except:
            nation = ""
        try:
            zodiac = ele.xpath("//div[@class='fl pr']//em/text()")[8]
        except:
            zodiac = ""
        try:
            self_introduction = ele.xpath("//div[@class='js_text']//text()")[0].strip()
        except:
            self_introduction = ""
        try:
            religion = ele.xpath("//div[@class='ifno_r_con']//em/text()")[5]
        except:
            religion = ""
        try:
            work_and_rest = ele.xpath("//div[@class='ifno_r_con']//em/text()")[6]
        except:
            work_and_rest = ""
        try:
            money = ele.xpath("//div[@class='fl f_gray_999']/em/text()")[3]
        except:
            money = ''
        try:
            y_age = ele.xpath("//div[@class='ifno_r_con']/text()")[0]
        except:
            y_age = ""
        try:
            y_salary = ele.xpath("//div[@class='ifno_r_con']/text()")[-1]
        except:
            y_salary = ""
        try:
            y_address = ele.xpath("//div[@class='ifno_r_con_1']/text()")[0]
        except:
            y_address = ""
        try:
            y_stuture = ele.xpath("//div[@class='ifno_r_con']/text()")[1]
        except:
            y_stuture = ""
        try:
            y_education = ele.xpath("//div[@class='ifno_r_con']/text()")[3]
        except:
            y_education = ""
        try:
            y_marital_status = ele.xpath("//div[@class='ifno_r_con']/text()")[-3]
        except:
            y_marital_status = ""

        SaveText().save(y_age, y_address, y_education, y_marital_status, y_salary, y_stuture, name, age, money, stature,
                        work_and_rest, weight, zodiac, self_introduction, constellation, religion, nation, education,
                        self.id)
        return


class SaveText:
    def save(self,y_age, y_address, y_education, y_marital_status, y_salary, y_stuture, name, age, money, stature,
              work_and_rest, weight, zodiac, self_introduction, constellation, religion, nation, education,id):
        print(self_introduction)
        sql="select * from baihe where id=%s"
        print(sql)
        result=cursor.execute(sql,(id,))
        print(result)
        if not result:
            try:
                sql1 = "insert into baihe (y_age,y_address,y_education,y_marital_status,y_salary,y_stuture,name,age,money,stature,work_and_rest,weight,zodiac,self_introduction,constellation,religion,nation,education,id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                print(sql1)
                cursor.execute(sql1, (
                    y_age, y_address, y_education, y_marital_status, y_salary, y_stuture, name, age, money, stature,
                    work_and_rest, weight, zodiac, self_introduction, constellation, religion, nation, education, id))

            except:
                return




class GetAddress:
    def __init__(self,url):
        self.url=url
    def getaddress(self):

        res = requests.get(self.url,headers=headers).content.decode("utf-8")
        ele=etree.HTML(res)
        address = ele.xpath("//select[@name='dq-Province']//option/@value")
        return address


if __name__ == '__main__':
    ar_url = "http://search.jiayuan.com/v2/"

    result = GetAddress(ar_url).getaddress()
    print(result)
    url = "http://search.jiayuan.com/v2/search_v2.php"
    GetIDList(result, url).getidlist()
