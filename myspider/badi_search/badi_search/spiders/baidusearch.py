#! python2
#encoding:utf-8

import scrapy

class BaiduSearchSpider(scrapy.Spider):
    name = "baidusearch"
    allowed_domains = ["baidu.com"]
    start_urls = [
            "https://www.baidu.com/s?wd=自然语言处理"
    ]

    def parse(self, response):
#        print response.body
#step1       filename = 'result.html'
#step1       with open(filename, 'wb') as f:
#step1            f.write(response.body)
#        hrefs = response.selector.xpath('//div[contains(@class, "c-container")]/h3/a/@href').extract()

#       for href in hrefs:
#step2            print href
#step3
"""
            yield scrapy.Request(href, callback=self.parse_url)
    def parse_url(self, response):
        print len(response.body)
"""
#step4
        hrefs = response.selector.xpath('//div[contains(@class, "c-container")]/h3/a/@href').extract()
        containers = response.selector.xpath('//div[contains(@class, "c-container")]')
        for container in containers:
            href = container.xpath('h3/a/@href').extract()[0]
            title = remove_tags(container.xpath('h3/a').extract()[0])
            c_abstract = container.xpath('div/div/div[contains(@class, "c-abstract")]').extract()
            abstract = ""
            if len(c_abstract) > 0:
                abstract = remove_tags(c_abstract[0])
            request = scrapy.Request(href, callback=self.parse_url)
            request.meta['title'] = title
            request.meta['abstract'] = abstract
            yield request
     def parse_url(self, response):
            print "url:", response.url
            print "title:", response.meta['title']
            print "abstract:", response.meta['abstract']
            content = remove_tags(response.selector.xpath('//body').extract()[0])
            print "content_len:", len(content)
"""
首先我们在提取url的时候顺便把标题和摘要都提取出来，
然后通过scrapy.Request的meta传递到处理函数parse_url中，
这样在抓取完成之后也能接到这两个值，
然后提取出content，这样我们想要的数据就完整了：
url、title、abstract、content
"""
