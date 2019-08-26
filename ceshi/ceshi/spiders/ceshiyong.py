# -*- coding: utf-8 -*-
import scrapy
class CeshiyongSpider(scrapy.Spider):
    name = 'ceshiyong'
    allowed_domains = ['ss.com']
    start_urls = ['http://ss.com/']

    def parse(self, response):
        pass
