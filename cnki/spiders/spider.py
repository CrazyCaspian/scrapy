# -*- coding:utf-8 -*-#
__author__ = 'RJS'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from ..items import CnkiItem,PaperItem, DetailItem
from scrapy.linkextractors import LinkExtractor

class CnkiSpider(CrawlSpider):
    name = "cnki"
    # allowed_domains = ["http://www.cnki.com.cn/Journal/C-C3-HERE-2016-08.htm"]
    start_urls = [
        "http://www.cnki.com.cn/Journal/C-C3-HERE-2016-08.htm"
    ]

    def parse(self, response):
        info = PaperItem()
        paper = CnkiItem()
        for sel in response.xpath('//div[@class="body_div"]/table'):
            info['paper'] = sel.xpath('//h1/text()').extract()
            info['title'] = sel.xpath('//table[@id="articleList"]//a/text()').extract()
            info['link'] = sel.xpath('//table[@id="articleList"]//a/@href').extract()
            info['author'] = sel.xpath('//span[@class="font_gray_12"]/text()').extract()
            # info['past'] = sel.xpath('//table[@id="issueList"]//a/@href').extract()
            # info['pastlink'] = sel.xpath('//table[@id="issueList"]//a/@href').extract()
            # info['years'] = sel.xpath('//table[@id="yearList"]//a/text()').extract()
            # info['yearslink'] = sel.xpath('//table[@id="yearList"]//a/@href').extract()
            # paper['otherpaper'] = sel.xpath('//table[@id="TongLeiQiKan"]//a/text()').extract()
            # paper['otherpaperlink'] = sel.xpath('//table[@id="yearList"]//a/@href').extract()
            yield info

        for i, url in enumerate(info['link']):
            print('sub parse', i)
            absurl = 'http://www.cnki.com.cn' + url
            yield scrapy.Request(absurl, callback=self.parse_sub)


    def parse_sub(self, response):
        print('Hi, this is sub page!', response.url)
        item = DetailItem()
        item['abstract']= response.xpath('//div[@id="content"]/div[2]/div[4]/text()').extract()
        item['keyword'] = response.xpath('//div[@id="content"]/div[2]/div[5]//a/strong/text()').extract()
        item['title'] = response.xpath('//div[@id="content"]/div[2]/div[2]/h1/text()').extract()
        yield item

