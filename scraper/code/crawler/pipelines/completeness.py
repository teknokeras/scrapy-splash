import os
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.exceptions import DropItem

class CompletenessPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('/data/incomplete_%s_products.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        complete = True

        if (item['name'] is None) or (item['name'] == ''):
            complete = False
        if (item['brand'] is None) or (item['brand'] == ''):
            complete = False
        if (item['description'] is None) or (item['description'] == ''):
            complete = False
        if (item['url'] is None) or (item['url'] == ''):
            complete = False
        if (item['original_price'] is None) or (item['original_price'] == ''):
            complete = False
        if (item['price'] is None) or (item['price'] == ''):
            complete = False
        if (item['image_urls'] is None) or (item['image_urls'] == ''):
            complete = False

        if not complete:
            self.exporter.export_item(item)

        return item
