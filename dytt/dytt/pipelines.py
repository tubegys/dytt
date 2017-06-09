# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import json
import codecs
from dytt.items import DyttItem

class DyttPipeline(object):
    pass


class DyttMysqlPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='123',
                                  db='db_gys',
                                  charset='utf8',
                                  use_unicode=True)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        insert_sql = "insert into tb_dytt(film_title,create_date)values(%s,%s)"
        # print("film_title", item['film_title'])
        print("create_date", item['create_date'])
        self.cursor.execute(insert_sql, (item['film_title'], item['create_date']))
        self.db.commit()

    def spider_closed(self):
        self.db.close()


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('dytt.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()
