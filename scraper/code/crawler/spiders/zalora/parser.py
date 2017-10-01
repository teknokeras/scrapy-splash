from scrapy_splash import SplashRequest

from crawler.items import Item

MAIN_URL = 'https://www.zalora.co.id/'
ZALORA_MEDIA_URL = 'http://zalora-media-live-id.s3.amazonaws.com/product/'

def parse_images_urls(images_urls):
    parsed_images_urls = list()
    HTTP_APPENDIX = 'http://'
    real_image_index = 1

    for url in images_urls:
        # zalora change the url when we open on browser,
        # splash cannot handle this so need to manually change the image urls here
        # sample:
        # http://static.id.zalora.net/p/arnold-palmer-4632-0235731-1.jpg
        # http://zalora-media-live-id.s3.amazonaws.com/product/02/35731/1.jpg
        raw_url = HTTP_APPENDIX + url.split(HTTP_APPENDIX)[real_image_index]

        item_url = raw_url.split('/')[-1].split('-')

        section_id_item_id = item_url[-2]
        section_id = section_id_item_id[:2]
        item_id = section_id_item_id[2:]

        raw_url = ZALORA_MEDIA_URL
        raw_url += section_id+'/'
        raw_url += item_id+'/'
        raw_url += item_url[-1]

        parsed_images_urls.append(raw_url)

    return parsed_images_urls

def parse_item(response):
    item = Item()
    item['name'] = response.xpath('//div[@class="product__title fsm"]/text()').extract()
    item['brand'] = response.xpath('//div[@class="js-prd-brand product__brand"]/a/text()').extract()
    item['description'] = response.xpath('//div[@class="product__title fsm"]/text()').extract()
    item['url'] = response.url

    item['original_price'] = response.xpath('//span[@id="js-price"]/text()').extract()

    item['price'] = response.xpath('//span[@class="js-detail_updateSku_lowestPrice"]/text()').extract()

    if len(item['price']) == 0:
        # no discount
        item['price'] = item['original_price']

    image_urls = response.xpath('//ul[@class="prd-moreImagesList ui-listItemBorder ui-listLight swiper-wrapper"]/li/a/img/@src').extract()
    #item['image_urls'] = image_urls
    item['image_urls'] = parse_images_urls(image_urls)

    item['source'] = 'zalora'

    string_size_xpath = '//option[(contains(@data-attribute,"size")) and not(contains(@disabled, "disabled"))]'
    string_size_xpath += '/text()'
    size_xpath = response.xpath(string_size_xpath).extract()

    #item['sizes'] = parse_sizes()
    item['sizes'] = size_xpath

    return item

def parse(response):
    item_selector = response.xpath('//a[@class="b-catalogList__itmLink itm-link"]/@href')
    for url in item_selector.extract():
        item_detail_url = MAIN_URL+url
        yield SplashRequest(item_detail_url, parse_item,
            endpoint='render.html',
            args={'wait': 3.0},
        )

    next_selector = response.xpath('//a[@title="Berikutnya"]//@href')

    prev_url = ''
    for url in next_selector.extract():
        next_url = MAIN_URL + url

        if prev_url == next_url:
            continue

        prev_url = next_url

        yield SplashRequest(next_url, parse,
            endpoint='render.html',
            args={'wait': 0.5},
        )
