# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from dytt.items import DyttItemLoader, DyttItem
import re
from urllib import parse
from scrapy.http import Request


class DyttspiderSpider(scrapy.Spider):
    name = 'dyttspider'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # 获取页面上所有电影的url,交给scrapy下载
        film_urls = response.xpath('//div[@class="co_content8"]//a/@href').extract()
        film_urls = [url for url in film_urls if not 'list' in url]
        film_urls = [parse.urljoin(response.url, url) for url in film_urls]
        # 电影标题
        # film_title = response.xpath('//div[@class="co_content8"]//a/text()').extract()
        # print(film_title)
        for film_url in film_urls:
            # print(film_url)
            yield scrapy.Request(url=film_url, callback=self.parse_detail)

        # 1.获得当前的url  通过select标签的option 判断是否selected
        option_urls = response.css('.co_content8 .x select option').extract()
        index = 0
        for url in option_urls:
            if 'selected' in url:
                current_url = url
                break
            else:
                index += 1
        print("index:", index)
        next_url = option_urls[index+1]  # 获取下一个url
        url_match_obj = re.match('.*value="(.*)".*', next_url)
        if url_match_obj:
            next_url = url_match_obj.group(1)
            next_url = parse.urljoin(response.url, next_url)
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_detail(self, response):
        item_loader = DyttItemLoader(item=DyttItem(), response=response)
        # 电影标题
        item_loader.add_css("film_title", '.bd3r .title_all h1 font::text')
        # 电影发布时间
        item_loader.add_css("create_date", 'div.co_content8 ul::text')
        # 电影下载地址
        item_loader.add_css("film_download_urls", "#Zoom a::attr(href)")
        # 电影插图url
        item_loader.add_css("image_urls", '#Zoom img::attr(src)')
        dytt_item = item_loader.load_item()
        yield dytt_item

