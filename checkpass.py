'''
Date: Aug-11-2020

Platform: Windows

Description: [PASSWORD CHECKER] - checks every password in a file if
it has been used/pawned/hacked according to pwnedpasswords.com api
by other users or sites and basically returns if the password is safe
to use or not

Usage: python checkpass.py [password.txt]
**password.txt should be in the same dir as the checkpass.py file
**every line in the password.txt should be a password and will be
checked by the script

Sections: A
'''

#SECTION A
import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def password_leeks_count(hashes, hash_to_check):
    # hashes.text.splitlines() produces a list
    # line.split(':'), splits a line entry into 2 with colon as delimiter
    # below is actually a generator, there is no tuple comprehension
    hashes_tuple = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes_tuple:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    """Converting the password string to sha1 hash"""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[0:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    return password_leeks_count(response, tail)


def main(args):
    """open the file specified in the command line args and
    check every passwords in every line"""
    with open(args, mode='r') as password_file:
        print(f'successfully opened {args}')
        passwords = [line.rstrip('\n') for line in password_file]

    print('checking password...')
    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times...change your password')
        else:
            print(f'{password} was not found')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))




