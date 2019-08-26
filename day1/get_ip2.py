import json

import requests
from lxml import etree
from urllib import request as ru
num=0


header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
}
while 1:
    try:
        num+=1
        # try:

        url="https://www.xicidaili.com/wt/"+str(num)+"/"
        result= requests.get(url=url,timeout=5,headers=header).text
        ele=etree.HTML(result)
        getip=ele.xpath("//tr/td[position()<4]/text() |//tr/td[last()-4]/text()")

        get_list = []
        for i in range(3,len(getip),3):
            get_list.append(
                {getip[i-3:i][2]:getip[i-3:i][0]+":"+getip[i-3:i][1]}
            )
        for j in get_list:

            url = "http://www.httpbin.org/ip"
            try:
                result=requests.get(url,proxies=j,timeout=5).text
                print(result)
                if json.loads(result)["origin"] != "117.136.0.223, 117.136.0.223":
                    with open("ip.txt", "a", encoding="utf-8") as a:
                        a.write(str(j)+"\n")
            except:
                continue
    except:
        continue

    #
# get_list=[]
    #     for i in range(len(getip)):
    #         get_list.append(
    #             {gettypes[i]:getip[i]+":"+getport[i]}
    #         )
    #     print(get_list)
    #     for j in get_list:
#     #         url = "http://www.httpbin.org/ip"
#     #         # head = ru.ProxyHandler(j)
#     #         # opener = ru.build_opener(head)
#     #         # result = opener.open(url,timeout=5).read().decode("utf-8")
#     #         result=requests.get(url,proxies=j).text
#     #
#     #
#     #         print(result)
#     #         if json.loads(result)["origin"] != "114.236.138.124, 114.236.138.124":
#     #             with open("ip.txt", "a", encoding="utf-8") as a:
#     #                 a.write(str(j)+"\n")
    # except:
    #     continue

