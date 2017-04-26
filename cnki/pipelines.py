# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from .items import CnkiItem, PaperItem, DetailItem, articleItem


class CnkiPipeline(object):
    def __init__(self):
        self.file = codecs.open('paper.json', 'w', encoding='utf-8')
        self.data = {}

    def process_item(self, item, spider):
        if isinstance(item, PaperItem):
            print("Job pipelines!")
            for i, ele in enumerate(item['title']):
                print("Item pipes ", i)
                self.data[ele] = [item['paper'][0], item['author'][i], 'http://www.cnki.com.cn' + item['link'][i]]
        elif isinstance(item, DetailItem):
            print("detail pipelines!")
            # detail.append(item)
            for j, ele in enumerate(item['title']):
                if ele in self.data.keys():
                    print("Detail pipes ", j, ele)
                    self.data[ele].extend([item['abstract'][1], item['keyword']])
                else:
                    self.data[ele] = [item['abstract'][1], item['keyword']]
        return self.data

    def close_spider(self, spider):
        line = json.dumps(self.data, self.file, indent=4, ensure_ascii=False)
        self.file.write(line)
