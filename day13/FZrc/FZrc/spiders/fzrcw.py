# -*- coding: utf-8 -*-
import scrapy
from ..items import FzrcItem

class FzrcwSpider(scrapy.Spider):
    name = 'fzrcw'
    # allowed_domains = ['c.com']
    # start_urls = ['http://c.com/']
    def start_requests(self):
        i=0
        page = ["0100","0500","0700","1400","0400"]
        while True:
            i+=1
            for j in page:
                try:
                    url = "http://yunjiexidi.com/rencai/"+j+"-20-"+str(i)+".html"
                    yield scrapy.Request(url)
                except:
                    continue
            i=0


    def parse(self, response):
        result = response.xpath("//td[@class='list-job-nane']//td/text() | //td[@class='list-job-nane']/a/text()[1] |//td[@class='list-job-nane']//td/span/text() ").extract()
        for i in range(7,len(result),7):
            item=FzrcItem()
            s=result[i-7:i]

            item["name"] = s[0].strip()

            item["sex"] = ""

            item["age"] =s[6]

            item["education"] = ""

            item["experience"] = s[4]

            item["census_register"] =""

            item["address"] = s[5]

            item["want_position"] = s[1]

            item["want_work"] = s[3]

            item["want_salary"] = s[2]

            item["job_status"] = ""

            item["marriage"] = ""
            yield item