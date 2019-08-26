# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import Item
from scrapy.pipelines.images import ImagesPipeline
class BizhanSpider(scrapy.Spider):
    name = 'bizhan'
    # headers={
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"
    # }
    # param= {
    #     'callback': 'jqueryCallback_bili_9454341502472945',
    #     'rid': '124',
    #     'type': '0',
    #     'pn': '9',
    #     'ps': '20',
    #     'jsonp': 'jsonp',
    #     '_': '1565772802369'
    # }
    # allowed_domains = ['b.com']
    # start_urls = ['http://b.com/']
    def start_requests(self):
        url="http://duanziwang.com/category/%E6%90%9E%E7%AC%91%E5%9B%BE/2/"
        yield scrapy.Request(url=url)
    def parse(self, response):
        item=Item()
        # print(response.text)

        url=response.xpath("//div[@class='post-content']/p/img/@src").extract()
        print(url)
        item["image_urls"]=url
        yield item
