#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import hashlib
import termcolor
url='https://md5decrypt.net/en/'
print('''Welcome to hashes [md5], choose your operation:
[1] encrypt
[2] decrypt''')
op = int(input())
if op == 2:
	print('Please Enter your hash: ')
	hash = input()
	with requests.session() as sess:
		try:
			r = sess.post(url, data={'hash': hash, 'decrypt': 'Decrypt'})
			soup = BeautifulSoup(r.text, 'html.parser')
			answer=soup.find('fieldset', id='answer').b.string
			termcolor.cprint('Hash decrypted successfully: {}'.format(answer), 'green')
		except:
			termcolor.cprint('Hash not found', 'red')
elif op == 1:
	print('please enter your word: ')
	word=input()
	enc = hashlib.md5(bytes(word, encoding='utf-8')).hexdigest()
	termcolor.cprint('Word decrypted successfully: {}'.format(enc), 'green')
