import os

class ZaloraPipeline(object):

    def process_price(self, price):
        temp_price = price[0]
        temp_price = temp_price.replace('SEKARANG','')
        temp_price = temp_price.replace('\n','').strip().replace('\xa0','')
        temp_price = temp_price.replace('RP','').replace('.','')
        temp_price = int(temp_price)
        return int(temp_price)

    def process_name_description(self, name, desc):
        return name[0], desc[0]

    def process_size(self, sizes):

        if len(sizes) == 0:
            return ['ONE_SIZE']

        size_cleaned = list()

        for size in sizes:
            size_cleaned.append(size.replace('\n','').strip())

        return size_cleaned

    def process_item(self, item, spider):
        if item['source'] != 'zalora':
            return item

        item['brand'] = item['brand'][0]
        item['price'] = self.process_price(item['price'])
        item['original_price'] = self.process_price(item['original_price'])
        item['name'], item['description'] = self.process_name_description(item['name'], item['description'])
        item['sizes'] = self.process_size(item['sizes'])

        return item
