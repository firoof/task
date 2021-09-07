# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from scrapy.http import HtmlResponse
from time import sleep


class FashioproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 拦截响应内容，使用selenium拿到需要的数据
    def process_response(self, request, response, spider):
        spider.bro.get(request.url)
        sleep(2)
        spider.bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(3)

        # 爬取页面4页点击加载新页面3次
        for num in range(3):
            button_tag = spider.bro.find_element_by_id('js-paginate-next')
            button_tag.click()
            sleep(3)
            try:
                # 捕获到弹窗，关闭弹窗
                tag = spider.bro.find_element_by_id('bx-element-1230003-W4UAQnt')
                tag.click()
            except:
                pass
            spider.bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(3)

        sleep(5)
        page_text = spider.bro.page_source
        new_response = HtmlResponse(url=request.url, body=page_text, request=request, encoding='utf-8')
        return new_response


    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
