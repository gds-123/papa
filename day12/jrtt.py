import json

import requests
from lxml import etree

headers= {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "referer": "https://www.toutiao.com/"
}
cookies={
    "cookie": "tt_webid=6726853066030876167; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=9h5fai2hi1566217538719; tt_webid=6726853066030876167; csrftoken=0824112df55ce21866cd987deba3d443"
}



class GetUrl:
    def __init__(self,page):
        self.page = page
        self.url="https://www.toutiao.com/api/pc/feed/?min_behot_time="+str(self.page)+"&category=__all__&utm_source=toutiao&widen=1&tadrequire=true"

    def getUrl(self):
        print(self.page)
        res = requests.get(url=self.url,headers=headers,cookies=cookies).text
        data = json.loads(res)
        print(data)
        page = data["next"]["max_behot_time"]

        all= data["data"]
        for i in all:
            try:
                abstract = i["abstract"]
                title = i["title"]
                print(abstract,title)
                print("***********************************************************************************************************************************************")
            except:
                continue

        GetUrl(page).getUrl()


if __name__ == '__main__':
    GetUrl(0).getUrl()