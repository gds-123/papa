# -*- coding: utf-8 -*-
import scrapy
from ..items import NingxiaItem as nxitem



class NingxiaSpider(scrapy.Spider):
    name = 'nxrcw'
    # allowed_domains = ['ningxia.com']
    # start_urls = ['http://www.nxrc.com.cn/resume/resume_list/page/8000.htm']

    def start_requests(self):
        for i in range(8559):
            url = "http://www.nxrc.com.cn/resume/resume_list/page/"+str(i)+".htm"
            yield scrapy.Request(url=url)

    def parse(self, response):
        try:
            url = response.xpath("/html/body/div[5]/div[1]/div[2]/div[7]/div[2]/a/@href").extract()[0]
            url = "http://www.nxrc.com.cn"+url
        except:
            return
        yield scrapy.Request(url=url,callback=self.getdetails)


    def getdetails(self,response):
        item = nxitem()
        try:
            item["name"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[2]/div[1]/text()").extract()[0].strip()
        except:
            item["name"] =""
        try:
            item["sex"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[3]/text()[1]").extract()[0].strip()

        except:
            item["sex"] =""
        try:
            item["age"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[3]/text()[2]").extract()[0].strip()
        except:
            item["age"] = ""
        try:
            item["education"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[3]/text()[3]").extract()[0].strip()
        except:
            item["education"] = ""
        try:
            item["experience"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[3]/text()[4]").extract()[0].strip()
        except:
            item["experience"] = ""
        try:
            item["census_register"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[4]/text()").extract()[0].strip()
        except:
            item["census_register"] = ""
        try:
            item["address"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[5]/text()").extract()[0].strip()
        except:
            item["address"] = ""
        try:
            item["want_position"] = response.xpath("//*[@id='content']/div[1]/div/div[2]/div[2]/text()[1]").extract()[0].strip()
        except:
            item["want_position"] = ""
        try:
            item["want_work"] = response.xpath("//*[@id='content']/div[1]/div/div[2]/div[2]/text()[1]").extract()[0].strip()
        except:
            item["want_work"] = ""

        try:
            item["want_salary"] = response.xpath("//*[@id='content']/div[1]/div/div[2]/div[2]/text()[3]").extract()[0].strip()
        except:
            item["want_salary"] = ""
        try:
            item["job_status"] = response.xpath("//*[@id='content']/div[1]/div/div[2]/div[2]/text()[5]").extract()[0].strip()
        except:
            item["job_status"] = ""
        try:
            item["marriage"] = response.xpath("//*[@id='content']/div[1]/div/div[1]/div[2]/div[3]/text()[6]").extract()[0].strip()
        except:
            item["marriage"] = ""
        print(item["name"], item["sex"], item["age"], item["education"], item["experience"],
                                  item["marriage"], item["census_register"], item["address"], item["want_position"],
                                  item["want_work"], item["want_salary"], item["job_status"])
        yield item