# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MmrcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    age = scrapy.Field()
    education = scrapy.Field()
    experience = scrapy.Field()
    marriage = scrapy.Field()
    census_register = scrapy.Field()
    address = scrapy.Field()
    want_position = scrapy.Field()
    want_work = scrapy.Field()
    want_salary = scrapy.Field()
    job_status = scrapy.Field()
    pass
