# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QcwyItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()
    salary = scrapy.Field()
    work_name = scrapy.Field()
    work_address = scrapy.Field()

