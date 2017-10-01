# -*- coding: utf-8 -*-
from urllib.parse import urlparse

import scrapy
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerProcess

from crawler.spiders.zalora.parser import parse as parse_zalora
from crawler.spiders.zalora.urls import get_start_urls

class ZaloraSpider(scrapy.Spider):
    name = "zalora"
    allowed_domains = ["zalora.co.id"]
    start_urls = list()

    def start_requests(self):
        self.start_urls = get_start_urls()

        for url in self.start_urls:
            #www.zalora.co.id
            yield SplashRequest(url, parse_zalora,
                endpoint='render.html',
                args={'wait': 0.5},
            )

if __name__ == "__main__":
    from scrapy.utils.project import get_project_settings
    process = CrawlerProcess(get_project_settings())
    process.crawl(ZaloraSpider)
    process.start() # the script will block here until the crawling is finished
