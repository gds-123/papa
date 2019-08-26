# -*- coding: utf-8 -*-
import scrapy
from ..items import MmrcItem as items

class MmrcSpider(scrapy.Spider):
    name = 'mmrc'
    # allowed_domains = ['c.com']
    # start_urls = ['http://c.com/']
    def start_requests(self):
        for i in range(100,300):
            url ="http://mm.93zp.com/rc/?page="+str(i)
            yield scrapy.Request(url)
    def parse(self, response):
        url = response.xpath("//a[@class='position_link']/@href").extract()
        for i in url:
            yield scrapy.Request(url=i,callback=self.getDetails)
    def getDetails(self,response):
        item = items()
        try:
            item["name"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[1]/span/text()").extract()[0]
        except:
            item["name"] = ""

        try:
            item["sex"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[2]/text()").extract()[0]

        except:
            item["sex"] = ""
        try:
            item["age"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[3]/text()").extract()[0]
        except:
            item["age"] = ""
        try:
            item["education"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[5]/text()").extract()[0]
        except:
            item["education"] = ""
        try:
            item["experience"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[4]/text()").extract()[0]
        except:
            item["experience"] = ""
        try:
            item["census_register"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[6]/text()").extract()[0]
        except:
            item["census_register"] = ""
        try:
            item["address"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[7]/text()").extract()[0]

        except:
            item["address"] = ""
        try:
            item["want_position"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[3]/ul/li[5]/span/text()").extract()[0]
        except:
            item["want_position"] = ""
        try:
            item["want_work"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[3]/ul/li[6]/text()").extract()[0]
        except:
            item["want_work"] = ""

        try:
            item["want_salary"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[3]/ul/li[2]/text()").extract()[0]
        except:
            item["want_salary"] = ""
        try:
            item["job_status"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[3]/ul/li[1]/text()").extract()[0]
        except:
            item["job_status"] = ""
        try:
            item["marriage"] = response.xpath("/html/body/div[4]/div[2]/div[2]/div[2]/ul/li[1]/span/text()").extract()[0]
        except:
            item["marriage"] = ""
        print(item["name"], item["sex"], item["age"], item["education"], item["experience"],
              item["marriage"], item["census_register"], item["address"], item["want_position"],
              item["want_work"], item["want_salary"], item["job_status"])
        yield item

