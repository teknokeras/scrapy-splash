# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

from tutorial.items import BerrybenkaItem

class BerrybenkaSpider(scrapy.Spider):
    name = 'berrybenka'
    allowed_domains = ['berrybenka.com']
    start_urls = ['http://berrybenka.com/clothing/tops/men/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        """
        Vertical crawl
        """
        detail_links = response.xpath('//a[@class="catalog-img"]/@href').extract()

        detail_exists = False

        for link in detail_links:
            detail_exists = True
            yield SplashRequest(link, self.parse_item,
                endpoint='render.html',
                args={'wait': 0.5},
            )

        if not detail_exists:
            return

        """
        Horizontal crawl
        """
        next_page = response.xpath('//li[@class="next right"]')
        self.page_index += 1

        for url in self.start_urls:
            new_url = url+str(self.page_index * self.items_per_page)

            yield SplashRequest(new_url, self.parse_item,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse_item(self, response):
        item = BerrybenkaItem()
        item['name'] = response.xpath('//div[@class="prod-spec-title"]/h1/text()').extract()
        item['brand'] = response.xpath('//div[@class="prod-spec-title"]/h2/a/text()').extract()
        item['description'] = response.xpath('//p[@id="product_description"]/text()').extract()
        item['price'] = response.xpath('//div[@class="prod-spec-title"]/p/text()').extract()
        item['url'] = response.url

        images = [response.xpath('//div[@class="detail-photo left"]/div[@class="big-photo left"]/a/img/@src').extract()]

        item['image_urls'] = images[0] + response.xpath('//div[@class="detail-photo left"]/div[@class="small-photo left"]/ul/li/a/img/@src').extract()

        return item
