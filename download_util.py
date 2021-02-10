import os
import requests
import shutil


def download_file(url, directory, fname=None):
    '''download a file'''
    # the url requires a User-agent header when using get request
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'}
    
    if fname is None:
        fname = os.path.basename(url)

    download_path = os.path.join(directory, fname)

    with requests.get(url, headers=headers, stream=True) as r:
        with open(download_path, 'wb') as file_obj:
            shutil.copyfileobj(r.raw, file_obj)
    
    return download_path


def simple_download(url, directory, fname=None):
    '''used for downloading simple file'''
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'}

    if fname is None:
        fname = os.path.basename(url)

    download_path = os.path.join(directory, fname)
    r = requests.get(url, headers=headers, stream=True)
    r.raise_for_status()

    with open(download_path, 'wb') as f:
        f.write(r.content)
    
    return download_path
