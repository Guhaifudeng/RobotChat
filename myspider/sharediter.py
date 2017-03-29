#-*- coding:utf-8 -*-
import scrapy
class SharediterSpider(scrapy.Spider):
    Name = 'shareditor'
    start_urls =['http://www.shareditor.com/']
    def parse(self, response):
        for href in response.css('a::attr(href)')
            full_url = response.urljoin(href.extract())

