# ==============================
#         Information
# ==============================

# Title: Download an Image from a URL
# Date: Feb-09-2020
# Difficulty: Easy
# Language: Python


# ==============================
#         Description
# ==============================

# This program accepts the following two arguments in the command line:
# argument 1: url of the image to be downloaded
# argument 2: filename and file extension of the image to be saved
# 
# This program will also create a folder named 'downloads' (if does not exists)
# in the same directory of this python file.
#
# If the url of the image is valid, the image will be downloaded to the
# created 'downloads' folder.


# ==============================
#           Usage
# ==============================

# In the command line, change the dir to the location of this python file.
# format:
# python [name_of_this_python_file] [url_of_the_image_to_be_downloaded] [image_file_name]
# example:
# python download_image.py 
#   https://2e8ram2s1li74atce18qz5y1-wpengine.netdna-ssl.com/wp-content/uploads/2019/11/shutterstock_1386882278-1-768x512.jpg
#   python.jpg


# ==============================
#           Code
# ==============================

import os
import sys
from download_util import download_file, simple_download


def create_downloads_dir():
    this_file_dir = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_dir)
    downloads_dir = os.path.join(BASE_DIR, 'downloads')
    downloads_path = os.path.basename(downloads_dir)

    if not os.path.exists(downloads_dir):
        print(f'Creating {downloads_path} folder')
        os.makedirs(downloads_dir, exist_ok=True)
    
    return downloads_dir


def image_exists(download_path):
    fname = os.path.basename(download_path)
    if os.path.exists(download_path):
        print(f'File <{fname}> is successfully downloaded.')


# driver code function
def main(args1, args2):
    url = sys.argv[1]
    file_name = sys.argv[2]
    downloads_dir = create_downloads_dir()

    download_path = download_file(url, downloads_dir)
    image_exists(download_path)

    download_path = simple_download(url, downloads_dir, file_name)
    image_exists(download_path)
    

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])