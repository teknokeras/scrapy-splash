# -*- coding: utf-8 -*-
from urllib.parse import urlparse

import scrapy
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerProcess

from crawler.spiders.berrybenka.parser import parse_item as parse_berrybenka_item
from crawler.spiders.berrybenka.urls import get_start_urls

class BerrybenkaSpider(scrapy.Spider):
    name = "berrybenka"
    allowed_domains = ['berrybenka.com']
    start_urls = list()

    BERRYBENKA_PAGE_INDEX = 0
    BERRYBENKA_ITEMS_PER_PAGE = 48

    def start_requests(self):
        self.start_urls = get_start_urls()

        for url in self.start_urls:
            #berrybenka.com
            yield SplashRequest(url, self.parse_berrybenka,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse_berrybenka(self, response):
        """
        Vertical crawl
        """
        detail_links = response.xpath('//a[@class="catalog-img"]/@href').extract()

        detail_exists = False

        for link in detail_links:
            detail_exists = True
            yield SplashRequest(link, parse_berrybenka_item,
                endpoint='render.html',
                args={'wait': 0.5},
            )

        if not detail_exists:
            return

        """
        Horizontal crawl
        """
        next_page = response.xpath('//li[@class="next right"]')
        self.BERRYBENKA_PAGE_INDEX += 1

        for url in get_start_urls():
            new_url = url+str(self.BERRYBENKA_PAGE_INDEX * self.BERRYBENKA_ITEMS_PER_PAGE)

            yield SplashRequest(new_url, self.parse_berrybenka,
                endpoint='render.html',
                args={'wait': 0.5},
            )

if __name__ == "__main__":
    from scrapy.utils.project import get_project_settings
    process = CrawlerProcess(get_project_settings())
    process.crawl(BerrybenkaSpider)
    process.start() # the script will block here until the crawling is finished
