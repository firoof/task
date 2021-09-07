import requests
import time
from openpyxl import Workbook

url = 'https://xueqiu.com/service/v5/stock/screener/quote/list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Referer': 'https://xueqiu.com/hq'
}

# 创建表格
book = Workbook()
ws = book.active
ws.append(['股票代码', '股票名称', '当前价', '涨跌幅', '市值', '市盈率'])

# 发起请求获取数据
for num in range(1, 5):
    time_st = round(time.time() * 1000)
    param = {
        'page': num,
        'size': 30,
        'order': 'desc',
        'orderby': 'percent',
        'order_by': 'percent',
        'market': 'US',
        'type': 'us',
        '_': time_st,
    }
    page_text = requests.get(url=url, headers=headers, params=param).json()
    for shares in page_text["data"]["list"]:
        symbol = shares['symbol']
        name = shares['name']
        current = shares['current']
        percent = shares['percent']
        pe_ttm = shares['pe_ttm']
        market_capital = shares['market_capital']
        # 将数据写入表格
        ws.append([symbol, name, current, percent, market_capital, pe_ttm])
        # print(symbol, name, current, percent, pe_ttm, market_capital, end='\n')

book.save('xueQiu.xlsx')