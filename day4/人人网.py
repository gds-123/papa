from lxml import etree
import requests,MySQLdb,re
from day4.chaojiying import getCode as gc


cookies = {
    "Cookie":"anonymid=jz1dd12u-qw5wzx; depovince=ZGQT; _r01_=1; jebe_key=6dd99a47-2327-41ab-880a-dfb6469f41e4%7C35a88b2d5c4e98988d3a46d65774edb4%7C1565189479279%7C1%7C1565189479287; jebe_key=6dd99a47-2327-41ab-880a-dfb6469f41e4%7C35a88b2d5c4e98988d3a46d65774edb4%7C1565189479279%7C1%7C1565189479289; JSESSIONID=abct7UBxTO4lw4pBCCWXw; ick_login=689da5fb-2a91-4c81-9100-7ce955150cbe; t=748285180b14da3d64600095a1e656ee6; societyguester=748285180b14da3d64600095a1e656ee6; id=971820486; xnsid=8f8deb32; jebecookies=fce99eca-d395-4a2b-9a85-1dcdac443801|||||; ver=7.0; loginfrom=null; l4pager=0; wp_fold=0"

}



conn =MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            db="no_3",
            charset="utf8",
        )
cursor=conn.cursor()
class GetList:
    def __init__(self,url):
        self.url=url
        self.xpath = "//div[@class='clearfix']//li/a/@href"
    def getlist(self):
        print(self.url,"]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        res = requests.get(url=self.url,cookies=cookies).text

        ele = etree.HTML(res)
        url_list= ele.xpath(self.xpath)

        # id = self.url
        # re1=re.compile("[0-9]{9}")
        # id = re1.findall(id)[0]
        # print(url_list)

        if url_list == [] :
            print("验证码验证码验证码验证码验证码验证码验证码")
            # img = ele.xpath("//div[@class='optional']/img/@src")[0]
            # img=requests.get(img,cookies=cookies).content
            img = requests.get(url='http://icode.renren.com/getcode.do?t=ninki&rnd=1565251619821',
                               cookies=cookies).content
            with open("../day4/a.jpg","wb") as w:
                w.write(img)
            num=gc()["pic_str"]
            data={
                # "id":str(id),
                'icode': str(num),
                'submit': '继续浏览',
                'requestToken': '1011228066',
                '_rtk': '8071bfc',
            }
            url2 = "http://www.renren.com/validateuser.do"
            requests.post(url=url2,data=data,cookies=cookies)

        for i in url_list:

            try:
                print(8888)
                sql3 = "select result from result where url=%s"
                cursor.execute(sql3,(i,))
                result = cursor.fetchone()[0]
                print(result)
                if result=="1":
                    print(11111111)
                    continue


            except:
                print(2222222222222222)
                sql = "insert into result values (%s,%s)"
                cursor.execute(sql, (i, str(0)))
                conn.commit()
            print("可以")
            GetDetails(i).getdetails()
            print("diguidiguidiididiididididiid")
            GetList(i).getlist()
class GetDetails:
    def __init__(self,url):
        self.url = url
        self.name = "//h1[@class='avatar_title no_auth']/text()"
        self.intro = "//div[@class='cover-bg']/p[@class='authentication']/text()"
        self.school = "//div[@class='tl-information']/ul//li[@class='school']/span/text()"
        self.sex = "//div[@class='tl-information']/ul//li[@class='birthday']/span[1]/text()"
        self.brithday = "//div[@class='tl-information']/ul//li[@class='birthday']/span[2]/text()"
        self.hometown = "//div[@class='tl-information']/ul//li[@class='hometown']/text()"
        self.address = "//div[@class='tl-information']/ul//li[@class='address']/text()"

    def getdetails(self):
        print(45444)
        try:
            res = requests.get(url=self.url,cookies=cookies).text
        except:
            return

        ele = etree.HTML(res)
        try:
            name = ele.xpath(self.name)[0].split()[0]
        except:
            name = ""
        try:
            intro = ele.xpath(self.intro)[0]
        except:
            intro = ""
        try:
            address = ele.xpath(self.address)[0]
        except:
            address = ""
        try:
            hometown = ele.xpath(self.hometown)[0]
        except:
            hometown = ""
        try:
            brithday = ele.xpath(self.brithday)[1:][0]
        except:
            brithday = ""
        try:
            sex = ele.xpath(self.sex)[0]
        except:
            sex = ""
        try:
            school = ele.xpath(self.school)[0]
        except:
            school = ""
        print(name,intro,address,hometown,brithday,sex,school,self.url)
        SaveText(name,intro,address,hometown,brithday,sex,school,self.url).save()





class SaveText:
    def __init__(self,name,intro,address,hometown,brithday,sex,school,url):
        self.name = name
        self.intro = intro
        self.address = address
        self.hometown = hometown
        self.brithday = brithday
        self.sex = sex
        self.school = school
        self.url = url
    def save(self):
        print("存入")
        try:
            sql8 = "insert into renren values (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql8, (
            self.school,self.sex,self.brithday, self.hometown,self.address,self.intro,self.name, self.url))
            conn.commit()
            sql1 = "update result set result ='1' where url=%s"
            cursor.execute(sql1, (self.url,))
            conn.commit()
        except:
            return



if __name__ == '__main__':
    url = "http://www.renren.com/330773777/profile"
    GetList(url).getlist()
    while 1:

        try:
            print("p[p[p[")
            sql = "select result,url from result where result ='0'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result, "]]]]]]]]]]]]]]]")
            if result:

                for i in result:
                    print("这是以 一一一一iy ",i[1])
                    if i[0] == "0" and i[1]!="#":
                        print("llllll")
                        GetList(i[1]).getlist()
                    else:
                        print("kkkkkkk")
                        GetList(url).getlist()
        except:
            pass

