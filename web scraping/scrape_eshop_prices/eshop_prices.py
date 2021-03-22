import os
import requests
from requests_html import HTML


BASE_DIR = os.path.dirname(__file__)




def generate_path(data_folder):
    return os.path.join(BASE_DIR, data_folder)


def get_html_text(url, headers, path, fname, save=False):
    fpath = f'{path}_{fname}.html'
    r = requests.get(url, headers=headers)
    if 200 <= r.status_code <= 299:
        if save:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(r.text)
        return r.text
    else:
        print(r.raise_for_status())


def extract_data(html_text):
    r_html = HTML(html=html_text)
    games_content = [games for games in r_html.find('.games-list-item-content')]
    
    for idx, games in enumerate(games_content, 1):
        title = games.find('h5')
        discount = games.find('.discount')
        print(f'{idx}. {title[0].text}', end=' ')
        print(f'({discount[0].text})')



url = 'https://eshop-prices.com/games/on-sale?direction=desc&sort_by=score'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
data_folder = 'data'
fname = 'eshop_prices'

path = generate_path(data_folder)
html_text = get_html_text(url, headers, path, fname, True)
extract_data(html_text)

