import os

class BerrybenkaPipeline(object):

    def process_price(self, price):
        temp_price = price[0]
        temp_price = temp_price.replace('IDR','').replace('.','')
        return int(temp_price)

    def process_name_description(self, name, desc):
        new_desc = " ".join(desc)
        new_desc = new_desc.replace("\n",".")
        new_desc = new_desc.replace("  "," ")
        return name[0], new_desc

    def process_sizes(self, sizes):
        if len(sizes) == 0:
            return ['ONE_SIZE']

        size_cleaned = list()

        for size in sizes:
            real_size = size.replace('\n','').strip()

            if real_size == '':
                continue

            size_cleaned.append(real_size)

        if len(size_cleaned) == 0:
            return ['ONE_SIZE']

        return size_cleaned

    def process_item(self, item, spider):
        if item['source'] != 'berrybenka':
            return item

        item['price'] = self.process_price(item['price'])
        item['original_price'] = self.process_price(item['original_price'])
        item['name'], item['description'] = self.process_name_description(item['name'], item['description'])
        item['brand'] = item['brand'][0]

        item['sizes'] = self.process_sizes(item['sizes'])

        return item
