'''
Date: Jun-17-2020

Platform: Windows

Description: [CMD Unsecured Password Manager] - type the account (hardcoded)
as argument1 and the password will be copied to clipboard!

Usage: python pw.py [account]

SECTIONS: A-B
'''

# SECTION A

import sys
import pyperclip

#hardcode for now the password dictionary, set the password in the value
PASSWORDS = {'email': 'email_pw@123',
             'fb': 'fb_pw@123',
             'github': 'github_pw@123'}

#the commandline needs 1 argument to extract password
#argument value will be compared to the PASSWORDS keys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('password copied to clipboard!')
else:
    print('account doesn\'t exists')


# Follow if you want this python file to be a Windows batch script
# SECTION B
# On Windows, save the fle as pw.bat in the C:\Windows folder:
# -----------------------------
# @py.exe C:\Python34\pw.py %*
# @pause
# -----------------------------
# win-r and type: pw <account name>.
