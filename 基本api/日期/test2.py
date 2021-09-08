import requests
url = 'http://127.0.0.1:5000/get_date'
page_text = requests.get(url=url).text
print(page_text)
