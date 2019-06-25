#! python

import sys
import pyperclip

# pw.py - An insecure password locker program, must be ran in the terminal

# cd into the dir holding this .py, then type "./pw.py {arg}

PASSWORDS = {'email': 'p@ssw0rd1',
             'blog': 'Pa$$bl0g',
             'luggage': '1234'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])  # get the corresponding value of the key
    print(f'Password for {account} copied to clipboard.')
else:
    print('There is no account named ' + account)
