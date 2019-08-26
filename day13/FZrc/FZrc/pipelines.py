# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class FzrcPipeline(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="localhost", user="root", password="123456", db="no_3", charset="utf8",
                                  port=3306, )
        self.cursor = self.db.cursor()
        self.num = 0

    def process_item(self, item, spider):
        self.num+=1

        sql = "insert into rcw values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, (item["name"], item["sex"], item["age"], item["education"], item["experience"],
                                  item["marriage"], item["census_register"], item["address"], item["want_position"],
                                  item["want_work"], item["want_salary"], item["job_status"]))
        if self.num == 500:
            self.num =0
            print("提交了")
            self.db.commit()
        return item