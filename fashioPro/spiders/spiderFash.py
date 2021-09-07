import scrapy
from selenium import webdriver
from fashioPro.items import FashioproItem


class SpiderfashSpider(scrapy.Spider):
    name = 'spiderFash'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.fashionnova.com/collections/all?sort_by=best-selling']



    # 实例化浏览器对象
    def __init__(self):
        self.bro = self.bro = webdriver.Chrome(executable_path='D:/projects/pythonProject/spiders1/Chapter_seven_selenium/chromedriver.exe')

    # 解析商品信息
    def parse(self, response):
        div_list = response.xpath('//*[@id="MainContent"]/div[3]/div[2]/div[2]/div/div')
        for div in div_list:
            name = div.xpath('./div/@data-title').extract_first()
            price = div.xpath('./div/@data-price').extract_first()
            item = FashioproItem()
            item['name'] = name
            item['price'] = price
            # print(name, price, end='\n\n')
            yield item


    # 关闭浏览器
    def closed(self, spider):
        self.bro.quit()

