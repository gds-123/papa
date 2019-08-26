# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class QcwyPipeline(object):
    def __init__(self):

        self.db = MySQLdb.connect(host="localhost", user="root", password="123456", db="no_3", charset="utf8",
                                  port=3306, )
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):

        sql = "insert into qcwy values(%s,%s,%s,%s)"
        self.cursor.execute(sql, (item["position"], item["salary"], item["work_name"], item["work_address"]))
        self.db.commit()

        return item
