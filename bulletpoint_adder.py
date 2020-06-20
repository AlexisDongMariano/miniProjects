'''
Date: Jun-20-2020

Platform: Windows

Description: [Character Appender] - adds an asterisk(*) to the beginning of a list of strings from the 
clipboard and pass it in the updated clipboard to be updated.
**I can use this idea to add docstring template to my new py mini projects

Usage: 
1. Copy a list of strings (sample below) from any source to place it in the clipboard
2. run below in the commandline
python bulletpoint_adder.py
3. use the modified string to paste anywhere that accepts strings (ex. word editor, browser, work files)

Sections: A
'''

#SECTION A

import pyperclip

# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars

text = pyperclip.paste()


# text_list = text.split('\r\n')
# output = ""
# for list in text_list:
#     output += '*' + list + '\n'
# print(output)
# pyperclip.copy(output)

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

print(text)
pyperclip.copy(text)


