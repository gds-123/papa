# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy_redis.spiders import Spider
from ..items import Chn2Item

headers = '''
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36
Cookie: __jsluid_h=ec5ad04ad2ce5794c0fa67395fbb365c; __jsl_clearance=1566179299.192|0|JqPTB0ntHO4KrHZCqUx9YAjSvOw%3D; tmas_cookie=51947.7697.15402.0000; JSESSIONID=00001tkR24eMETcmieaqqDDBjzD:1bm104rj3

'''

headers = eval('{' + re.sub(r'(.*?):(.*?)\n', r'"\1":"\2",\n', headers).replace(' ','') + "}")


class ChnlogoSpider(Spider):
    name = 'chnlogo'
    def start_requests(self):
        url= 'http://sbgg.saic.gov.cn:9080/tmann/annInfoView/annSearchDG.html'
        page=0
        for i in range(201,400):
            data = """
                    page: 1
                    rows: 100000
                    annNum: """+str(page)+"""
                    annType: 
                    tmType: 
                    coowner: 
                    recUserName: 
                    allowUserName: 
                    byAllowUserName: 
                    appId: 
                    appIdZhiquan: 
                    bfchangedAgengedName: 
                    changeLastName: 
                    transferUserName: 
                    acceptUserName: 
                    regName: 
                    tmName: 
                    intCls: 
                    fileType: 
                    totalYOrN: true
                    appDateBegin: 
                    appDateEnd: 
                    agentName: 
                    """
            page+=1
            data = eval('{' + re.sub(r'(.*?):(.*?)\n', r'"\1":"\2",\n', data).replace(' ', '') + "}")

            yield scrapy.FormRequest(url=url,formdata=data)

    def parse(self, response):
        data=json.loads(response.text)
        item =Chn2Item()
        item["name"]=data["rows"][0]["reg_name"]
        item["id"]=data["rows"][0]["reg_num"]
        print(item["name"],item["id"])
        yield item

