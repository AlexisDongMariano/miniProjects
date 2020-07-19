import requests
import hashlib

# CBFDAC6008F9CAB4083784CBD1874F76618D2A97 - password13


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def password_leeks_count(hashes, hash_to_check):
    # hashes = (line.split(':') for line in hashes.text.splitlines())
    # for h, count in hashes:
    #     print(h, count)

    hashes_tuple = (line.split(':') for line in hashes.text.splitlines())
    for h in hashes_tuple:
        print(h)
    print(type(hashes_tuple))

def pwned_api_check(password):
    """Converting the password string to sha1 hash"""
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[0:5], sha1password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)
    print(response)
    return password_leeks_count(response, tail)

pwned_api_check('123')