import requests
data = {'data': '{"value_array": [{"value": 12}, {"value": 18}, {"value": 10}]}'}
url = 'http://127.0.0.1:5000/add'
page_text = requests.post(url=url, data=data).text
print(page_text)