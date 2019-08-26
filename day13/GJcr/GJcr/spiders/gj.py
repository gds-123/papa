# -*- coding: utf-8 -*-
import scrapy
from ..items import GjcrItem

class GjSpider(scrapy.Spider):
    name = 'gj'
    # allowed_domains = ['c.com']
    # start_urls = ['http://c.com/']
    def start_requests(self):
        adds=["nj","sh","wh","xa","bj","ah","sd","jl","ln","hn","hz","dl","km","xianggang","nb","dg"]
        for i in adds:
            url="http://%s.ganji.com/qiuzhi/"%i
            yield scrapy.Request(url)
    def parse(self, response):
        zurl=response.url[:-8]
        url = response.xpath("//dl//a/@href").extract()
        with open("gj.txt","r") as w:
            u = w.read()
            if u in url:
                url = url[url.index(u):]

        for i in url:
            for j in range(110):
                url=zurl+i+"o"+str(j)
                with open("gj.txt","w") as a:
                    a.write(i)
                yield scrapy.Request(url=url,callback=self.getDetails)
    def getDetails(self,response):
        item = GjcrItem()
        result=response.xpath("//div[@class='basic-info']//span[position()<6]/text()| //div[@class='s-butt s-bb1']/ul//li/text()").extract()

        for i in range(8,len(result),8):
            s=result[i-8:i]
            item["name"] = s[0]

            item["sex"] = s[1]

            item["age"] = s[2]

            item["education"] = s[3]

            item["experience"] = s[4]

            item["census_register"] = ""

            item["address"] = ""

            item["want_position"] = s[5]

            item["want_work"] = s[6]

            item["want_salary"] = s[7]

            item["job_status"] = ""

            item["marriage"] = ""
            yield item