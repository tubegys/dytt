# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
import re

class DyttItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


def date_extract(value):
    match_obj = re.match('.*(\d{4}-\d{2}-\d{2}).*', value.strip())
    if match_obj:
        value = match_obj.group(1)
    return value


class DyttItem(scrapy.Item):
    # 电影标题信息
    film_title = scrapy.Field()
    # 电影发布时间
    create_date = scrapy.Field(
        input_processor=MapCompose(date_extract)
    )
    # 电影下载链接
    film_download_urls = scrapy.Field()  # 可能有多个？？
    # 电影插图url
    image_urls = scrapy.Field()  # 可能有多个？？



if __name__=='__main__':
    date_extract('\r\n\r\n\r\n\r\n发布时间：2016-12-05  \r\n \r\n \r\n\r\n')
