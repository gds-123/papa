# -*- coding: utf-8 -*-
import json

import scrapy


class Chninfo1Spider(scrapy.Spider):
    name = 'CHNinfo1'
    # allowed_domains = ['CHNinfo1.com']
    # start_urls = ['http://CHNinfo1.com/']
    def start_requests(self):
        url = "https://www.cnvd.org.cn/flaw/list.htm?flag=true"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
            "Referer": "https://www.cnvd.org.cn/flaw/list.htm?flag=true"
        }
        cookies={
            "Cookie": "__jsluid_s=f5851df1d35fc6af4cf50f4cb71f499c; JSESSIONID=B8DEE118EF65B53A9E8471248EB0B2C9; __jsluid_h=15eb8d4136912f60184620baef8ce9c1; __jsl_clearance=1565704329.069|0|9aL4HWPo24Gs0dHF4BLwtlQRC%2BU%3D"
        }
        page = 0
        s="[Ljava.lang.String;@3a646dbd"
        while 1:
            data = {
                'number': '请输入精确编号',
                'flag': s,
                'max': '20',
                'offset': str(page),
                }
            a=scrapy.Request(url=url, body=json.dumps(data), headers=headers, method="POST",cookies=cookies)
            # s=json.loads(a.body.decode())["flag"]
            s=scrapy.version_info
            page+=1

            print(s,page)



    def parse(self, response):
        print(111111)
        print(response.text)
        return