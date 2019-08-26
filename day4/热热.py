import requests
from lxml import etree
import MySQLdb

from day4.chaojiying import getCap

url = 'http://www.renren.com/880151247/profile'


cookies = {
    'Cookie': 'anonymid=jz0zmuk7-ub8kah; depovince=BJ; _r01_=1; l4pager=0; JSESSIONID=abcZK9d9bxDQGeJrj-VXw; ick_login=bad8f5c3-d998-415c-ae44-c1ab213d8dff; t=047c8b544724e8a4bb95b6c67b44c86d0; societyguester=047c8b544724e8a4bb95b6c67b44c86d0; id=969805440; xnsid=9003112d; ver=7.0; loginfrom=null; wp_fold=0; jebecookies=84d367ca-e1ed-4dc3-b5be-be9792346362|||||; jebe_key=51b033f6-fe0d-4a2c-a627-f51cb8752297%7Cc9648fadd971497f6415b29ba7925b4e%7C1565166373802%7C1%7C1565252868552; jebe_key=51b033f6-fe0d-4a2c-a627-f51cb8752297%7Cc9648fadd971497f6415b29ba7925b4e%7C1565253278038%7C1'

}
conn = MySQLdb.connect(host='localhost', user='root', password='123456', port=3306, db='crawler', charset='utf8')
cursor = conn.cursor()

def getURLS(url):
    sql2 = 'SELECT status FROM renren_url WHERE urls=%s'
    cursor.execute(sql2,(url,))
    status = cursor.fetchone()[0]
    print(status)
    if status=="1":
        return
    res = requests.get(url=url,cookies=cookies).text
    ele = etree.HTML(res)
    name = ele.xpath("//title/text()")
    sql1 = 'UPDATE renren_url set status="1" where urls=%s'
    cursor.execute(sql1,(url,))
    conn.commit()
    print(name)
    if name == ['人人网 - 验证码']:
        img = requests.get(url='http://icode.renren.com/getcode.do?t=ninki&rnd=1565251619821',cookies=cookies).content
        with open('a.jpg','wb') as w:
            w.write(img)
        code = getCap('a.jpg')['pic_str']
        print(code)
        validata_url = 'http://www.renren.com/validateuser.do'
        validata_data = {
            'id': '244461309',
            'icode': code,
            'submit': '继续浏览',
            'requestToken': '-1920086405',
            '_rtk': '594eccd5'
        }
        r =  requests.post(url=validata_url,data=validata_data,cookies=cookies).text
        # print(r)
    # print(res)
    print(requests.get(url='http://www.renren.com/880151247/profile',cookies=cookies).text)
    urls = ele.xpath('//ul//li/a/@namecard')
    urls = ['http://www.renren.com/'+i+'/profile' for i in urls]
    for i in urls:
        try:
            sql = 'INSERT INTO renren_url VALUES (%s,%s)'
            cursor.execute(sql, (i, str(0)))
            conn.commit()
        except:
            pass
        getURLS(i)

# def pjyzm():


if __name__ == '__main__':
    getURLS('http://www.renren.com/220937288/profile')