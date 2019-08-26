import re
import time

import requests

headers = """
        Host: aweme-eagle.snssdk.com
        Connection: keep-alive
        Cookie: install_id=83244009652; ttreq=1$f5afcb6e0558b700b76713eef3ff1f12297a8633; odin_tt=0eaa6d25b736034f2d2ed46bd303a1d42338b6e44b8450b861452ecece761845890e46ec4b6ecacfed80221b537ba2ddbbf17e78718c5e4a5aead7563f4f8bc1; qh[360]=1
        Accept-Encoding: gzip
        X-SS-REQ-TICKET: 1566302027594
        sdk-version: 1
        User-Agent: com.ss.android.ugc.aweme/750 (Linux; U; Android 5.1.1; zh_CN; SM-G955N; Build/NRD90M; Cronet/58.0.2991.0)
        X-Gorgon: 0300b71d40019f96d3525a176a47ce4e9ae7862a8cfaa82ac760
        X-Khronos: 1566302027

        """
headers = eval('{' + re.sub(r'(.*?):(.*?)\n', r'"\1":"\2",\n', headers).replace(' ', '') + "}")
# cookies = {
#     "Cookie": "Cookie: install_id=83241779591; ttreq=1$28590947d442ff17a83fc95a50dfc20c2ce41cb3; odin_tt=8912897371a6071f522aecab061ffa487fd9f90f0c9a39abbc420d7ead80fa4c17b01953745674664e79b57bc9566f1e4414f3f56426815141142fca2f4e1170; qh[360]=1"
# }


class GetUrl:
    def __init__(self, url):
        self.url = url

    def geturl(self):
        print(111111111111)
        res = requests.get(url=self.url,headers=headers).json()
        print(res)
        self.getDetails(res)

    def getDetails(self, res):
        url_list = res["aweme_list"]

        for i in url_list:
            url1=i["video"]["play_addr"]["url_list"][0]
            name = i["desc"]
            print(url1,name)
            res = requests.get(url=url1).content
            self.saveVideo(res,name)
    def saveVideo(self,data,name):
        with open("%s.mp4"%name,"wb") as a:
            a.write(data)

if __name__ == '__main__':
    while True:
        t = time.time()
        t1=str(t).replace(".","")[:13]
        url = "https://aweme-eagle.snssdk.com/aweme/v1/feed/?type=0&max_cursor=0&min_cursor=0&count=6&volume=0.7333333333333333&pull_type=1&need_relieve_aweme=0&filter_warn=0&req_from&is_cold_start=0&longitude=0&latitude=0&address_book_access=1&gps_access=1&os_api=22&device_type=SM-G955N&ssmix=a&manifest_version_code=750&dpi=240&js_sdk_version=1.19.2.0&uuid=354730010168304&app_name=aweme&version_name=7.5.0&ts=1566302029&app_type=normal&ac=wifi&update_version_code=7502&channel=tengxun_new&_rticket=1566302027595&device_platform=android&iid=83244009652&version_code=750&openudid=a81e8450eb131744&device_id=66591881130&resolution=1280*720&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007"

        GetUrl(url).geturl()
