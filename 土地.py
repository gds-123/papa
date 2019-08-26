import requests
from lxml import etree

headers={
    "User-Agent": "Spider",
    "Referer": "http://www.landchina.com/default.aspx?tabid=226&ComName=default",
    "Sec-Fetch-Mode": "no-cors",
    "Host": "www.landchina.com",
    "Connection": "keep-alive",
}
cookies={
    "Cookie": "ASP.NET_SessionId=r3oncczscf33newteckdbq0k; Hm_lvt_83853859c7247c5b03b527894622d3fa=1566312385,1566314849,1566314853,1566315488; Hm_lpvt_83853859c7247c5b03b527894622d3fa=1566316642; security_session_verify=fc74fefba922420e4b316a9d6c00ea7a"
}
def a(x):
    res = requests.get(x).text
    ele = etree.HTML(res)
    url = ele.xpath("//a[@target='_blank']/@href")
    for i in url[3:]:
        new_url = "http://www.landchina.com" + i
        print(new_url)
        res1=requests.get(url=new_url,headers=headers,cookies=cookies).text
        print(res1)
if __name__ == '__main__':
    url = "https://www.landchina.com/default.aspx?tabid=261&ComName=default"
    a(url)
