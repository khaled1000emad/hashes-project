import requests
from bs4 import BeautifulSoup
import hashlib
import termcolor
url='https://md5decrypt.net/en/'
op=0
while not op == 3:
	print('''Welcome to hashes [md5], choose your operation:
	[1] encrypt
	[2] decrypt
	[3] quit''')
	op = int(input())
	if op == 2:
		print('Please Enter your hash: ')
		hash = input()
		with requests.session() as sess:
			try:
				r = sess.post(url, data={'hash': hash, 'decrypt': 'Decrypt'})
				soup = BeautifulSoup(r.text, 'html.parser')
				answer = soup.find('fieldset', id='answer').b.string
				termcolor.cprint('Hash decrypted successfully: {}'.format(answer), 'green')
			except:
				termcolor.cprint('Hash not found', 'red')
	elif op == 1:
		print('please enter your word: ')
		word = input()
		enc = hashlib.md5(bytes(word, encoding='utf-8')).hexdigest()
		termcolor.cprint('Word decrypted successfully: {}'.format(enc), 'green')
