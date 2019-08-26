# -*- coding: utf-8 -*-
import scrapy


class Music163Spider(scrapy.Spider):
    name = 'music163'
    # allowed_domains = ['music.com']
    # start_urls = ['http://music.com/']

    def start_requests(self):
        url="https://music.163.com/discover/toplist"
        scrapy.Request()

    def parse(self, response):
        pass
