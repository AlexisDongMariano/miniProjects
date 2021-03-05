# create a directory called scrape_test1 along with the location of this file
# save the html file as w3schools_table.html from url 'https://www.w3schools.com/html/html_tables.asp'
# extract the example table and save as w3schools_table.csv file

import os
import requests
import pandas as pd
from datetime import datetime
from requests_html import HTML


BASE_DIR = os.path.dirname(__file__)


def create_directory(dirname):
    fpath = os.path.join(BASE_DIR, dirname)
    if not os.path.exists(fpath):
        os.makedirs(fpath, exist_ok=True)
    return fpath


def generate_fname(fname_pre):
    current_date = datetime.now().strftime('%b-%d-%Y')
    return f'{fname_pre}_{current_date}'


def get_html_text(url, path, fname, save=True):
    r = requests.get(url)
    if r.status_code == 200:
        if save:
            fname_full = f'{fname}.html'
            fpath = os.path.join(path, fname_full)
            with open(fpath, 'w') as f:
                f.write(r.text)
        return r.text
    else:
        print(r.raise_for_status())


def extract_data(html_text):
    r_html = HTML(html=html_text)
    table_id = '#customers'
    r_table = r_html.find(table_id)
    parsed_table = r_table[0]
    rows = parsed_table.find('tr')
    header_row = rows[0]
    header_names = [col.text for col in header_row.find('th')]

    table_data = []
    for row in rows[1:]:
        cols = row.find('td')
        row_data = []
        for col in cols:
            row_data.append(col.text)
        table_data.append(row_data)

    return header_names, table_data


def save_data(header_names, table_data, fpath, fname):
    df = pd.DataFrame(table_data, columns=header_names)
    csv_fpath = os.path.join(fpath, f'{fname}.csv')
    df.to_csv(csv_fpath, index=False)


dirname = 'scrape_test1'
fname_pre = 'w3schools_table'
url = 'https://www.w3schools.com/html/html_tables.asp'
fpath = create_directory(dirname)
fname = generate_fname(fname_pre)
html_text = get_html_text(url, fpath, fname, False)
header_names, table_data = extract_data(html_text)
save_data(header_names, table_data, fpath, fname)

