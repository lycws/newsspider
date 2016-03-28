# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Newsitem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    src = scrapy.Field()
    showimg = scrapy.Field()
    type = scrapy.Field()

    pass

class Finitem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    src = scrapy.Field()
    showimg = scrapy.Field()
    type = scrapy.Field()

    pass

class Entitem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    src = scrapy.Field()
    showimg = scrapy.Field()
    type = scrapy.Field()

    pass

class Sportitem(scrapy.Item):

    title = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    src = scrapy.Field()
    showimg = scrapy.Field()
    type = scrapy.Field()

    pass