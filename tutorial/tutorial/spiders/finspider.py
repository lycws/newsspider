# -*- coding: utf-8 -*-

import scrapy
import json
import re
import time
from tutorial.items import Finitem
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess

class Finspider(scrapy.Spider):
    name = "finspider"
    #allowed_domains = ["xw.qq.com"]
    start_urls = [
        "http://openapi.inews.qq.com/getQQNewsIndexAndItems?chlid=news_news_finance&refer=mobilewwwqqcom&otype=jsonp&t=1459066349936"
    ]

    def parse(self, response):

        pattern = re.compile(r"http://xw\.qq\.com/finance/.+")
        if re.match(pattern, response.url):
            item = Finitem()

            title = response.xpath("//h1[@class='title']/text()").extract()
            item['title'] = title[0].encode('utf-8')

            content = response.xpath("//p[@class='split']/text() | //div[@class='image split']/img").extract()
            str = ''
            for con in content:
                str += con.encode('utf-8') + "<br/>"

            item['content'] = str

            img = response.xpath("//div[@class='image split']/img/@src").extract()

            if img:
                item['showimg'] = img[0].encode('utf-8')

            time = response.xpath("//span[@class='time']/text()").extract()
            item['time'] = time[0].encode('utf-8')

            src = response.xpath("//span[@class='author']/text()").extract()
            item['src'] = src[0].encode('utf-8')

            item['type'] = 'finance'

            yield item

        else:
            sites = json.loads(response.body[19:-1])
            for news in sites['idlist'][0]['ids']:
                #print news['id']

                #http://xw.qq.com/finance/20160327020761/FIN2016032702076102
                url = "http://xw.qq.com/finance/" + news['id'][3:17] + "/" + news['id']

                yield Request(url, callback=self.parse)