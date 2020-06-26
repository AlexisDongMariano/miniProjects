'''
Date: Jun-26-2020

Platform: Windows

Description: Copy text from any source and this script will extract the
phone numbers (000-000-0000) and email (username@domain.com) then place
in the clipboard to be pasted in text editor or same form.

Sections: A-D (Working code located in Section C)
'''
####################################################################
# SECTION A
'''
Solution Creation High-level Steps:
1. Extract the text from the clipboard
    1.a. Use module 'pyperclip'
2. Use regex to extract phone number and email
    2.a. Create regex for phone number and email separately
    2.b. Match both regex in the text from the clipboard
3. Format the extracted values
    3.a. Maybe place the values in a string separated by
        new lines
4. Replace the clipboard with the formatted values
    4.a Use module 'pyperclip'
'''
####################################################################
# SECTION B
# Sample string to extract the phone numbers and email:
'''
This is just a sample text from admin@company.com with number
123-456-7890 to be used in this program to extract emails like
name1.surname1@company.com and number like 098-765-4321 with
examples below:
email: name2.surname2@company.com
cp no: 420-881-8261
email: peter_cetera@singers.com
cp no: 444-9999 (postal optional)
invalid samples:
email: user@user@company.com
cp no: 420,881,8261
'''
# Output of the program
# *following will be copied to clipboard to use:
'''
123-456-7890
098-765-4321
420-881-8261
444-9999
admin@company.com
name1.surname1@company.com
name2.surname2@company.com
peter_cetera@singers.com
user@company.com
'''
####################################################################
# SECTION C

import pyperclip
import re

text = pyperclip.paste() #place the clipboard contents in a variable

#define the regex
num_pattern = re.compile(r'((\d{3}-)?\d{3}-\d{4})')
email_pattern = re.compile(r'(([a-z0-9]+[._-]?[a-z0-9]+)@[a-z0-9-]+\.[a-z]{2,3})', re.I)

#find the regex matches
num_items = num_pattern.findall(text)
email_items = email_pattern.findall(text)

num_items_str = ""
email_items_str = ""

for item in num_items:
    num_items_str += item[0] + '\n'

for item in email_items:
    email_items_str += item[0] + '\n'

print('Copied to clipboard:')
print(num_items_str)
print(email_items_str)

#copy the resulting string to the clipboard
pyperclip.copy(num_items_str + email_items_str)

####################################################################
# SECTION D
# *Another Solution
# import pyperclip, re
#
#
# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))? # area code
# (\s|-|\.)? # separator
# (\d{3}) # first 3 digits
# (\s|-|\.) # separator
# (\d{4}) # last 4 digits
# (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
# )''', re.VERBOSE)
#
# # Create email regex.
# emailRegex = re.compile(r'''(
# u [a-zA-Z0-9._%+-]+ # username
# v @ # @ symbol
# w [a-zA-Z0-9.-]+ # domain name
# (\.[a-zA-Z]{2,4}) # dot-something
# )''', re.VERBOSE)
#
# # Find matches in clipboard text.
# text = str(pyperclip.paste())
#
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])
# if groups[8] != '':
#     phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
#
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])
#
# # Copy results to the clipboard.
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Copied to clipboard:')
#     print('\n'.join(matches))
# else:
#     print('No phone numbers or email addresses found.')
