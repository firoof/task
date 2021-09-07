# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from openpyxl import Workbook

class FashioproPipeline:

    book = Workbook()
    ws = book.active
    ws.append(['名称', '价格'])

    def process_item(self, item, spider):
        self.ws.append([item['name'], item['price']])

        return item

    def close_spider(self, spider):
        self.book.save('fashionN.xlsx')
        print('over')