# -*- coding: utf-8 -*-
import re

import scrapy
from ..items import YnrcwwItem as items

class YnrcwwSpider(scrapy.Spider):
    name = 'ynrcw1'
    # allowed_domains = ['c.com']
    # start_urls = ['http://c.com/']
    def start_requests(self):
        for i in reversed(range(57318)):
            url = "http://www.ynzp.com/cms/personsearch.html?page="+str(i)+"&qtype=Q&query=&rp=1000"
            yield scrapy.Request(url)
    def parse(self, response):
        item = items()
        lis = response.xpath('//div[@class="spPrList"]/ul/li')
        try:
            for li in lis:
                try:
                    item["name"] = li.xpath('.//em/a/text()').get().split(' ')[0]
                except:
                    item["name"] =""

                try:
                     results= re.sub(r'\s', '', ''.join(li.xpath('.//dd/text()').getall())).split('|')
                except:
                    results =""
                item["sex"] = results[0]
                item["age"] = results[1]
                height = results[2]
                item["want_salary"]=""
                item["address"]=""
                item["census_register"]=""
                item["marriage"] = results[3]
                item["education"] = results[4]
                results2 = results[5].split('意向地')
                item["experience"] = results2[0]
                results3 = results2[1].split('意向职位')
                item["want_work"] = '意向地' + results3[0]
                item["want_position"] = '意向职位' + results3[1]
                item["job_status"]=""
            print(item["name"], item["sex"], item["age"], item["education"], item["experience"],
                  item["marriage"], item["census_register"], item["address"], item["want_position"],
                  item["want_work"], item["want_salary"], item["job_status"])
        except:
            pass
        yield item
