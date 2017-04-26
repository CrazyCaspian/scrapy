# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    paper = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
    detail = scrapy.Field()
    # past = scrapy.Field()
    # pastlink = scrapy.Field()
    # years = scrapy.Field()
    # yearslink = scrapy.Field()

class articleItem(scrapy.Item):
    title =scrapy.Field()


class DetailItem(scrapy.Item):
    abstract = scrapy.Field()
    keyword = scrapy.Field()
    title = scrapy.Field()


class CnkiItem(scrapy.Item):
    name = scrapy.Field()
    otherpaper = scrapy.Field()
    otherpaperlink = scrapy.Field()

