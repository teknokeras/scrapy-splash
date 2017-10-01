from scrapy_splash import SplashRequest

from crawler.items import Item

from crawler.spiders.berrybenka.urls import get_start_urls


def parse_item(response):
    item = Item()
    item['name'] = response.xpath('//div[@class="prod-spec-title"]/h1/text()').extract()
    item['brand'] = response.xpath('//div[@class="prod-spec-title"]/h2/a/text()').extract()
    item['description'] = response.xpath('//p[@id="product_description"]/text()').extract()
    item['price'] = response.xpath('//div[@class="prod-spec-title"]/p/text()').extract()
    item['url'] = response.url

    item['original_price'] = response.xpath('//div[@class="prod-spec-title"]/p/span/text()').extract()

    if len(item['original_price']) == 0:
        item['original_price'] = item['price']

    images = [response.xpath('//div[@class="detail-photo left"]/div[@class="big-photo left"]/a/img/@src').extract()]

    item['image_urls'] = images[0] + response.xpath('//div[@class="detail-photo left"]/div[@class="small-photo left"]/ul/li/a/img/@src').extract()
    item['source'] = 'berrybenka'

    string_size_xpath = '//div[@class="filter-size filter-content"]/ul/li/div/label/text()'
    size_xpath = response.xpath(string_size_xpath).extract()

    #item['sizes'] = parse_sizes()
    item['sizes'] = size_xpath

    return item
