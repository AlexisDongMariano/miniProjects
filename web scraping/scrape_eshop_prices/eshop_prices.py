import os
import requests


BASE_DIR = os.path.dirname(__file__)
URL = 'https://eshop-prices.com/games/on-sale?direction=desc&sort_by=score'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
r = requests.get(URL, headers=headers)


print(r.status_code)
print(r.text)
