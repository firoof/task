import requests
data = {'data': '{"msg":"您好吗？再见实打实大所多"}'}
url = 'http://127.0.0.1:5000/chat'
page_text = requests.post(url=url, data=data).text
print(page_text)