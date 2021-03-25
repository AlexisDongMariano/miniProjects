import os
import requests
from requests_html import HTML
import smtplib


BASE_DIR = os.path.dirname(__file__)


def generate_path(data_folder):
    return os.path.join(BASE_DIR, data_folder)


def get_html_text(url, headers, path, fname, save=False):
    fpath = os.path.join(path, f'{fname}.html')
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
    games_list = []
    for games in games_content:
        title = games.find('h5')
        discount = games.find('.discount')
        games_list.append((title[0].text, discount[0].text))
    return games_list


def format_to_str(data):
    data_str = ''
    for idx, e in enumerate(data, 1):
        data_str += f'{idx}. {e[0]} ({e[1]}) \n'
    return data_str


def save_output(data, path, fname):
    os.makedirs(path, exist_ok=True)
    fpath = os.path.join(path, f'{fname}.txt')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(f'{x[0]} {x[1]}' for x in data))
        

def send_mail(url, data):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('<email_sender>', '<email_sender_password>')
    #compose the email message 
    subject = 'Eshop popular games sale'
    body = f'{data}\
    \n\
    \n Check this link: {url}'
    msg = f'Subject: {subject}\n\n{body}'
    fmt = '{}'
    #list of email recipients
    email_addresses = [
        '<email_recipient1>',
        '<email_recipient2>'
    ]
    #send the email to the recipients
    for recipient in email_addresses:
        server.sendmail(
            'cupnoodlesseafood22@gmail.com',
            recipient,
            fmt.format(msg).encode('utf-8')
        )
        print(f'email sent for {recipient}')
    server.quit()


def run():
    url = 'https://eshop-prices.com/games/on-sale?direction=desc&sort_by=score'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}
    data_folder = 'data'
    fname = 'eshop_prices'

    path = generate_path(data_folder)
    html_text = get_html_text(url, headers, path, fname, True)
    games_list = extract_data(html_text)
    save_output(games_list, path, fname)
    data_str = format_to_str(games_list)
    send_mail(url, data_str)


if __name__ == '__main__':
    run()
