# -*- coding: utf-8 -*-
import re

import scrapy
from ..items import YnrcItem as items

class YnrcwSpider(scrapy.Spider):
    name = 'ynrcw'
    # allowed_domains = ['c.com']
    # start_urls = ['http://c.com/']
    def start_requests(self):
        for i in range(32045,63771):
            url = "http://www.ynzp.com/cms/personsearch.html?page="+str(i)+"&qtype=Q&query=&rp=20&jobPosCat=&fullTime=0&jobExp=0&edu=0&refreshTime=0&region=0&companyGroup=&regionIndex=&disp=&speciality=0&sex=0&age_lower=0&age_upper=0&sortname=UpdateTime&SalaryRange=0&param="
            yield scrapy.Request(url)
    def parse(self, response):
        item = items()
        lis = response.xpath('//div[@class="spPrList"]/ul/li')
        try:
            for li in lis:
                item["name"] = li.xpath('.//em/a/text()').get().split(' ')[0]
                results = re.sub(r'\s', '', ''.join(li.xpath('.//dd/text()').getall())).split('|')
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
