# -*- coding: utf-8 -*-
import scrapy
from ..items import GdrcItem

class GdrcwSpider(scrapy.Spider):
    name = 'gdrcw'
    # gdrcwallowed_domains = ['s.com']
    # start_urls = ['http://s.com/']
    def start_requests(self):
        for i in range(100):
            url = "http://www.020zp.net/resume/resume-list----------"+str(i)+".htm"
            with open("GZRC.txt","w") as a:
                a.write(str(i))
            yield scrapy.Request(url )

    def parse(self, response):

        item = GdrcItem()
        try:
            item["name"] = response.xpath("//*[@id='infolists']/div[2]/div[2]/div[1]/a/text()").extract()
            print(item["name"])
        except:
            item["name"] =""
        result=response.xpath("//*[@id='infolists']/div[2]/div[2]/div[4]/p/text()").extract()[0].split()
        try:
            item["sex"] = ""

        except:
            item["sex"] =""
        try:
            item["age"] = result[6]
        except:
            item["age"] = ""
        try:
            item["education"] = result[0]
        except:
            item["education"] = ""
        try:
            item["experience"] =result[2]
        except:
            item["experience"] = ""
        try:
            item["census_register"] = result[4]
        except:
            item["census_register"] = ""
        try:
            item["address"] = ""

        except:
            item["address"] = ""
        try:
            item["want_position"] = result[-3]
        except:
            item["want_position"] = ""
        try:
            item["want_work"] = ""
        except:
            item["want_work"] = ""

        try:
            item["want_salary"] = ""
        except:
            item["want_salary"] = ""
        try:
            item["job_status"] = ""
        except:
            item["job_status"] = ""
        try:
            item["marriage"] = ""
        except:
            item["marriage"] = ""
        # print(item["name"], item["sex"], item["age"], item["education"], item["experience"],
        #                           item["marriage"], item["census_register"], item["address"], item["want_position"],
        #                           item["want_work"], item["want_salary"], item["job_status"])
        # yield item
