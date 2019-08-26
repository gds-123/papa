import json

import requests
from lxml import etree
from urllib import request as ru
num=191
while 1:
    try:
        num+=1
        try:

            url="https://www.kuaidaili.com/free/inha/"+str(num)+"/"
            result=ru.urlopen(url,timeout=5).read().decode("utf-8")
            ele=etree.HTML(result)
            getip=ele.xpath("//td[@data-title='IP']/text()")
            getport=ele.xpath("//td[@data-title='PORT']/text()")
            gettypes=ele.xpath("//td[@data-title='类型']/text()")
        except:
            break

        get_list=[]
        for i in range(len(getip)):
            get_list.append(
                {gettypes[i]:getip[i]+":"+getport[i]}
            )
        print(get_list)
        for j in get_list:
            url = "http://www.httpbin.org/ip"
            # head = ru.ProxyHandler(j)
            # opener = ru.build_opener(head)
            # result = opener.open(url,timeout=5).read().decode("utf-8")
            try:
                result=requests.get(url,proxies=j,timeout=5).text
            except:
                continue

            print(result)
            if json.loads(result)["origin"] != "218.91.92.91, 218.91.92.91":
                with open("ip.txt", "a", encoding="utf-8") as a:
                    a.write(str(j)+"\n")
    except:
        continue


