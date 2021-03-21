import os
import requests


BASE_DIR = os.path.dirname(__file__)




def generate_path(data_folder):
    return os.path.join(BASE_DIR, data_folder)


def get_html_text(url, headers, path, fname, save=False):
    fpath = f'{path}{fname}.html'
    r = requests.get(url, headers=headers)
    if 200 <= r.status_code <= 299:
        # if save:
        #     with open(fpath, 'w') as f:
        #         f.write(r.text)
        return r.text
    else:
        print(r.raise_for_status())


url = 'https://eshop-prices.com/games/on-sale?direction=desc&sort_by=score'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
data_folder = 'data'
fname = 'eshop_prices'

path = generate_path(data_folder)
html_text = get_html_text(url, headers, path, fname, True)
print(html_text)

