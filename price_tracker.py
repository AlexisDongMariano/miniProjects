'''
Date: Jun-16-2020

Platform: Windows

Description: [BASIC WEB SCRAPING] - sends an email to the hardcoded recipients
if the item from a shoe shop has dropped its original price

Usage: python price_tracker.py

Sections: A
'''

#SECTION A

import requests
from bs4 import BeautifulSoup
import smtplib
import time

#actual url of the shoe item to be web scraped/monitored
URL = 'https://www.aldoshoes.com/ca/en/men/footwear/casual-shoes/liberace-blue/p/12905197'


def check_price():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
	
    #beautiful soup webscraping initialization
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(class_='c-product-price__formatted-price').get_text()
    item = soup.find(class_='c-heading c-buy-module__product-title').get_text()
    converted_price = price[1:]
	
    #run function if the item of the price drops from the original price posted in the site
    if float(converted_price) < 70:
        send_mail(item, price)

    print(converted_price)
    print(item)


def send_mail(item, price):
    server = smtplib.SMTP('smtp.gmail.com', 587) #specify smtp server, google in our sample
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sender_email@gmail.com', 'password') #specify the sender email and password
	
    #compose the email message 
    subject = 'Aldo Shoe Price Checker'
    body = f'    Item: {item}\n\
    Price: {price}\n\
    Check this link: {URL}'
    msg = f'Subject: {subject}\n\n{body}'
	
    #list of email recipients
    email_addresses = [
        'recipient1_email@gmail.com',
        'recipient2_email@gmail.com',
        'recipient3_email@gmail.com'
    ]
    
    #send the email to the recipients
    for recipient in email_addresses:
        server.sendmail(
            'sender_email@gmail.com',
            recipient,
            msg
        )
        print(f'email sent for {recipient}')

    server.quit()

#run the program every hour
while True:
    check_price()
    time.sleep(60*60)
