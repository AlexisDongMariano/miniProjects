'''
Date: Jun-12-2020

Platform: Windows

Description: Simple Project that scans a specified directory for '.jpg' files and creates an equivalent
'.png' files in a specified directory

Usage: python jpg_to_png.py [sourceDirectory] [destinationDirectory]
**directories will be created if doesn't exists

Section: A-E
**Actual working code in SECTION E
'''

##############################################
# SECTION A
# PILLOW BASIC IMAGE METHODS
# img = Image.open('./astro.jpg')

# blurred_img = img.filter(ImageFilter.BLUR)
# blurred_img = img.filter(ImageFilter.SMOOTH)
# blurred_img = img.filter(ImageFilter.SHARPEN)
# blurred_img.save("blurred_pikachu.png", 'png')
# rotated_img = img.rotate(90) #no need to save the image when showing after rotated
# filtered_img = img.convert('L') #converting to grayscale
# filtered_img.save("gy_pikachu.png", 'png') #saving a file
# filtered_img.show() #an output window will show
# resized_img = img.resize((300, 300)) #tuple of pixels
# box_for_cropping = (100, 100, 400, 400) #upper-left, lower-right coordinates for cropping
# cropped_img = img.crop(box_for_cropping)

# img.thumbnail((400, 400)) #create thumbnail then save
# img.save("thumb_astro.png", 'png')

# img_thumb = Image.open('./thumb_astro.png')
# print(img_thumb.size) #img.mode, img.size, img.format, img.info
# img.show()

# file = 'C:\\Users\\Dong\\Desktop\\test.txt'
# with open(file, mode='r') as test_file:
#     print(test_file)
###################################
# SECTION B
# #SCANNING FILES FROM DIRECTORY
# directory = r'C:\Users\admin'
# for entry in os.scandir(directory):
#     if (entry.path.endswith(".jpg")
#             or entry.path.endswith(".png")) and entry.is_file():
#         print(entry.path)
###################################
# SECTION C
# GET WORKING DIRECTORY WINDOWS
# https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
# import os
# cwd = os.getcwd()
###################################
# SECTION D
# ITERATE THROUGH FILES IN A DIRECTORY
# https://www.newbedev.com/python/howto/how-to-iterate-over-files-in-a-given-directory/
# import os
#
# directory = r'C:\Users\admin'
# for entry in os.scandir(directory):
#     if (entry.path.endswith(".jpg")
#             or entry.path.endswith(".png")) and entry.is_file():
#         print(entry.path)

# SECTION E
import sys
import os
from PIL import Image


class ImageProcess():
    def jpg_to_png(self, img, dest_dir, img_filename):
        #clean_name = os.path.splitext(filename)[0] #we can also use os splittext to create tuples
        #that separate filename and extension name
        png_filename = img_filename[:len(img_filename) - 3]
        try:
            img.save((dest_dir + png_filename + 'png'), 'png')
            print(f'{png_filename}png has been successfully created!')
        except ValueError as err:
            raise err
        except IOError as err:
            raise err


# CREATE FROM AND DESTINATION DIRECTORY IF DOESN'T EXISTS
def check_dir(dir_output, dir_input):
    if not os.path.exists(dir_output):
        print(f"{dir_input} directory does not exists!")
        try:
            os.makedirs(dir_output)
            print(f"{dir_input} directory created!")
        except:
            print("unable to create new directory")
    else:
        print(f"{dir_input} already exists :)")


def set_dir(dir_input):
    cwd = os.getcwd()
    if not dir_input.endswith('\\'):
        dir_input += '\\'
    dir_output = cwd + "\\" + dir_input
    check_dir(dir_output, dir_input)
    return dir_output


def process_jpg(from_dir, dest_dir):
    process_img = ImageProcess()
    for img_entry in os.scandir(from_dir): #or os.listdir(path)
        # img_entry.name #name of file
        # img_entry.path #path of file
        if img_entry.name.endswith('jpg') and img_entry.is_file():
            img_filename = img_entry.name
            try:
                img = Image.open(from_dir + img_filename)
                print(f'{img_filename} retrieved...')
            except:
                print(f'Unable to retrieve {img_filename}')
            process_img.jpg_to_png(img, dest_dir, img_filename)


from_dir = set_dir(sys.argv[1])
dest_dir = set_dir(sys.argv[2])
process_jpg(from_dir, dest_dir)
