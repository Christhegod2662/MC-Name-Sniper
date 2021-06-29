import colorama
import random
import os
import time
import colorama
import datetime
import requests
import ctypes
from datetime import datetime
from colorama import Fore
os.system('cls')
colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW('._.')

def worker():
	while True:
		with open('names.txt', 'r') as f:
			data = f.readlines()
			num = random.randint(0, 131000)
			name = data[num]
			name = name.replace('\n', '')
			r = requests.get(f'https://some-random-api.ml/mc?username={name}')
			if r.status_code == 200:
				pass

			elif r.status_code == 400:
				pass

			else:
				cur = datetime.now()
				a = cur.strftime("%H:%M:%S")
				print(f'{Fore.YELLOW}[{a}]{Fore.RESET} Name: {Fore.GREEN}{name} is open!{Fore.RESET} Link: https://namemc.com/search?q={name}')
				f.close()

			time.sleep(0.7)

worker()