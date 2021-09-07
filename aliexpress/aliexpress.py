import requests
import re
from openpyxl import Workbook

url = 'https://www.aliexpress.com/wholesale?SearchText=hat'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}
page_text = requests.get(url=url, headers=headers).text

# 正则拿到数据，是'[]'的用eval()还原
ex = r'"itemList":\{"content":(.*?)}},"resultCount"'
page_li = re.findall(ex, page_text, re.S)

# 解决eval()报错
globals_ = {

    'true': 0

}
page_li = eval(page_li[0], globals_)

# 创建表格
book = Workbook()
ws = book.active
ws.append(['商品名称', '图片url', '售价', '评分', '销量'])



# 解析数据
for det in page_li:
    pic_url = det["image"]["imgUrl"]
    title = det["title"]["displayTitle"]
    price = det["prices"]["salePrice"]["minPrice"]
    try:
        evaluation = det["evaluation"]["starRating"]
    except Exception as e:
        evaluation = '暂无评分'
    sale_v = det["trade"]["tradeDesc"]
    # 将数据写入表格
    ws.append([title, pic_url, price, evaluation, sale_v])
    # print(pic_url, title, price, evaluation, sale_v, end='\n')

book.save('alie.xlsx')