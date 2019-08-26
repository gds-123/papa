# -*- coding: utf-8 -*-
from urllib import parse
from ..items import QcwyItem
import scrapy


class QiancwySpider(scrapy.Spider):
    name = 'qiancwy'
    cookies={
        "Cookie": "partner=www_baidu_com; guid=d275a94660af6a90e2fa7b80c71e38a9; 51job=cenglish%3D0%26%7C%26; nsearch="
                  "jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSear"
                  "ch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; nolife=fromd"
                  "omain%3Dwww; slife=lastvisit%3D010000%26%7C%26; search=jobarea%7E%60071300%7C%21ord_field%7E%600%7C%"
                  "21recentSearch0%7E%601%A1%FB%A1%FA071300%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA33%A1%FB%A"
                  "1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA"
                  "%C5%E4%BC%FE%2F%CF%FA%CA%DB%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565762263%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%B7%BF%B2%FA%BE%AD%BC%CD%C8%CB%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565762248%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%CA%FD%BE%DD%B7%D6%CE%F6%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565761968%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%CF%FA%CA%DB%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565761998%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1565762015%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21"
    }
    # allowed_domains = ['qiancwy.com']
    # start_urls = ['http://qiancwy.com/']
    def start_requests(self):
        wk=["平面","销售","数据分析","房产经纪人","配件/销售","汽车","web","服务","金融/投资/证券","人事","会计"]
        page =0
        for i in wk:
            i = parse.quote(i)
            for j in range(2000):
                try:
                    url ="https://search.51job.com/list/000000,000000,0000,00,9,99,"+str(i)+",2,"+str(page)+".html"
                    print("当前在%s城市，第%s页"%(parse.unquote(i),page))
                    yield scrapy.Request(url=url,cookies=self.cookies)
                except:
                    print("错误")
                    page=0
                    break
                page+=1
            page=0

    def parse(self, response):
        item = QcwyItem()
        # print(response.text)
        try:
            position=response.xpath("//div[@class='el']/p/span/a/text()").extract()
        except:
            print("错误")
            return
        try:
            salary=response.xpath("//div[@class='el']/span[@class='t4']/text()").extract()
        except:
            print("错误")
            return
        try:
            work_name=response.xpath("//div[@class='el']/span[@class='t2']/a/text()").extract()
        except:
            print("错误")
            return
        try:
            work_address=response.xpath("//div[@class='el']/span[@class='t3']/text()").extract()
        except:
            print("错误")
            return

        for i in range(len(position)):
            item["position"]=position[i].strip()
            item["salary"] =salary[i].strip()
            item["work_name"] =work_name[i].strip()
            item["work_address"] =work_address[i].strip()
            yield item