import requests

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",

        'Referer': 'https://weibo.com/caizicaixukun?topnav=1&wvr=6&topsug=1&is_hot=1',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    }

cookies = {
    "Cookie": "SUB=_2AkMqDFdFf8NxqwJRmfsRymPmZI5wzArEieKcUKaeJRMxHRl-yT9jqm8ktRB6AYx5qpMQ3DlPQvgEfiJHO0mrdb1Vt2GP; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFxremPPI3mn9aThzGev10C; _s_tentry=passport.weibo.com; Apache=9908056079678.482.1565579381987; SINAGLOBAL=9908056079678.482.1565579381987; ULV=1565579382051:1:1:1:9908056079678.482.1565579381987:; YF-V5-G0=451b3eb7a5a4008f8b81de1fcc8cf90e; YF-Page-G0=5161d669e1ac749e79d0f9c1904bc7bf|1565579556|1565579374"
}

class GetDetails:
    def __init__(self,url):
        self.url=url
    def getdetails(self):
        res = requests.get(self.url,headers=headers,cookies=cookies).text
        print(res)


if __name__ == '__main__':
    url="https://weibo.com/caizicaixukun?topnav=1&wvr=6&topsug=1&is_hot=1"


    GetDetails(url).getdetails()