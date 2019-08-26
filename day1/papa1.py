import json
from urllib import request as ru, parse
from lxml import etree
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user="root",
    password="123456",
    db="no_3",
    charset="utf8"
)
cursor = conn.cursor()


def url_all(adress, count1):
    position1 = ["爬虫", "web", "AI", "JAVA", "大数据"]
    sql = "select position from papa"
    cursor.execute(sql)
    try:
        a = cursor.fetchone()[0]
    except:
        a=0
    print(a)
    if len(position1)>=a>=0:
        position1 = position1[int(a):]
        print(position1)
    else:
        a=0
        position1 = position1[int(a):]
    count = 0
    num=0
    sql = "select adress,position from papa"
    sql=cursor.execute(sql)
    print(sql)
    if not sql:
        print(sql,"~~~~~~~~~~~~~~~~~")
        sql = "insert into papa(adress,position)values(%d,%d)" % (count1, count)
        cursor.execute(sql)
        conn.commit()
    else:
        print(sql, "~~~~!!!!!!!!!!!!!!!!!!!!!!~",count,count1)
        sql = "update papa set adress=%d,position=%d"%(count1, count)

        cursor.execute(sql)
        conn.commit()

    for i in position1:
        print(i)
        print("hahahahah",count1,count)
        sql = "update papa set adress=%d,position=%d" % (count1, count)
        cursor.execute(sql)
        conn.commit()
        i = parse.quote(i)
        a=1
        num = 0
        while a:
            num+=90
            print(num,adress,i,"~~~~")
            url = "https://fe-api.zhaopin.com/c/i/sou?start=" + str(num) + "&pageSize=90&cityId=" + str(
                adress) + "&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=" + str(
                i) + "&kt=3&=0&_v=0.34331922&x-zp-page-request-id=b3049e4c15644d22bf1afb5183ddb043-1564998589572-795041&x-zp-client-id=f997901b-58ce-48e6-9fb5-bd0e0f856692"
            # try:
            result = ru.urlopen(url).read().decode("utf-8")
            print(result)

            result = json.loads(result)
            count_all = result["data"]["count"]
            print(count_all,num)
            if num>int(count_all):
                break
            for j in result["data"]["results"]:
                url = j["positionURL"]
                details(url)
            count += 1

            # except:
            #     print("错了")
            #     pass





def details(url):
    result = ru.urlopen(url).read().decode("utf-8")
    ele = etree.HTML(result)
    try:
        titel = ele.xpath("//h3//text()")[0]

        print(titel)
        salary = ele.xpath("//div[@class='summary-plane__left']/span/text()")[0]
        lightspot1 = ele.xpath("//div[@class='highlights__content']/span/text()")
        lightspot=""
        for j in lightspot1:
            lightspot+=j
        workplace = ele.xpath("//div[@class='job-address__content']/span/text()")[0]
        working_area = ele.xpath("//ul/li/a/text()")[0]
        working_time = ele.xpath("//ul/li/text()")[0]
        education = ele.xpath("//ul/li/text()")[1]
        peoples = ele.xpath("//ul/li/text()")[2]
        describe = ele.xpath("//div[@class='describtion__detail-content']/text()")
        print(describe)

        describe1=""
        for i in describe:
            describe1+=i.strip()

        save_text(titel, salary, lightspot, workplace, working_area, working_time, education, peoples, describe1)
    except:
        pass


def save_text(titel,salary,lightspot,workplace,working_area,working_time,education,peoples,describe1):
    with open("jobs.txt","a",encoding="utf-8") as w:
        w.write(
            "工作："+titel+"\n"+"工资："+salary+"\n"+"职位亮点："+lightspot+"\n"+"工作地点："+workplace+"\n"+"公司区域："+working_area+"\n"+"经验要求："+working_time
            +"\n"+"学历："+education+"\n"+"招聘人数："+peoples+"\n"+"职位描述："+describe1+"\n"
        )


if __name__ == "__main__":
    adress = ["530", "538", "765", "763"]
    count1 = 0
    sql= "select adress from papa"
    s = cursor.execute(sql)
    try:
        a = cursor.fetchone()[0]
    except:
        a=0
    print(a)
    if a>=0:

        count1=int(a)
        print(count1)
        adress=adress[int(a):]
        for i in adress:
            url_all(i, count1)
            count1 += 1
    else:
        print(11111)
        for i in adress:

            url_all(i, count1)
            count1 += 1
