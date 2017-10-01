# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Item(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    original_price = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    source = scrapy.Field()
    sizes = scrapy.Field()
