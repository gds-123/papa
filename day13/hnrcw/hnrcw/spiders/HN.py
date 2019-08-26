# -*- coding: utf-8 -*-
import scrapy
from ..items import HnrcwItem as items


class HnSpider(scrapy.Spider):
    name = 'HN'
    def start_requests(self):
        for i in range(5240):
            url = "http://www.0577job.com/resume/index.php?all=0_0_0_0_0_0_0_0_0&tp=0&page=" + str(i)
            with open("2.txt","w") as a:
                a.write(str(i))
            yield scrapy.Request(url=url)

    def parse(self, response):
        item = items()
        result = response.xpath("/html/body/div[3]/div/div[4]/div[2]/div[2]/span/text()").extract()
        try:
            item["name"] = response.xpath("/html/body/div[3]/div/div[4]/div[1]/div[2]/a/text()").extract()[0].split()[0]
        except:
            item["name"] =""

        try:
            item["sex"] = ""

        except:
            item["sex"] =""
        try:
            item["age"] = result[0]
        except:
            item["age"] = ""
        try:
            item["education"] = result[2]
        except:
            item["education"] = ""
        try:
            item["experience"] = result[1]
        except:
            item["experience"] = ""
        try:
            item["census_register"] = ""
        except:
            item["census_register"] = ""
        try:
            item["address"] = ""

        except:
            item["address"] = ""
        try:
            item["want_position"] = response.xpath("/html/body/div[3]/div/div[4]/div[2]/div[2]/div[2]/span[1]/text()").extract()[0]
        except:
            item["want_position"] = ""
        try:
            item["want_work"] = response.xpath("/html/body/div[3]/div/div[4]/div[3]/div[2]/div[1]/span/text()").extract()[0]
        except:
            item["want_work"] = ""

        try:
            item["want_salary"] = ""
        except:
            item["want_salary"] = ""
        try:
            item["job_status"] = response.xpath("/html/body/div[3]/div/div[4]/div[2]/div[2]/div[3]/div/text()").extract()[0].split("：")[1]
        except:
            item["job_status"] = ""
        try:
            item["marriage"] = ""
        except:
            item["marriage"] = ""
        print(item["name"], item["sex"], item["age"], item["education"], item["experience"],
                                  item["marriage"], item["census_register"], item["address"], item["want_position"],
                                  item["want_work"], item["want_salary"], item["job_status"])
        yield item

