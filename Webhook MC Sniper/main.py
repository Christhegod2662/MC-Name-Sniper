import dhooks
import colorama
import discord
import threading
import time
import datetime
import random
import requests
import os
import ctypes
import json
from colorama import Fore
from dhooks import Webhook
ctypes.windll.kernel32.SetConsoleTitleW(':P')
os.system('cls')
colorama.init()
with open('config.json', 'r') as f:
	data = json.load(f)
	webh = data["webhook"]
	f.close()

def verify():
	r = requests.get(webh)
	res = r.json()
	if r.status_code == 200:
		print(f'{Fore.GREEN}Webhook Name: {res["name"]}{Fore.RESET}\n')

	else:
		print(f'{Fore.RED}Invalid webhook!{Fore.RESET}')
		print(f'{Fore.YELLOW}Press any key to quit the MC-Name sniper!{Fore.RESET}')
		os.system('pause >null')
		quit()

verify()

print(f'{Fore.GREEN}Currently sniping MC names!{Fore.RESET}\n\n{Fore.YELLOW}Please Note: Embed wont send if the username is taken, itll only send if the user is open!{Fore.RESET}')
def worker():
	while True:
		link = Webhook(webh)
		f = open('text.txt', 'r')
		data = f.readlines()
		num = random.randint(0, 131000)
		user = data[num]
		user = user.replace("\n", " ")
		api = f'https://some-random-api.ml/mc?username={user}'
		r = requests.get(api)
		if r.status_code == 200:
			pass

		elif r.status_code == 404:
			pass

		else:
			em = discord.Embed(title = 'MC-Names sniffer!', description = f'**User: {user} is open!\n\nDate available: [Click Here](https://namemc.com/search?q={user})**', color = (0x56ed12))
			em.timestamp = datetime.datetime.utcnow()
			em.set_footer(text='Did you know, MC-Sniffer is checking 37 Names per minute!')
			link.send(embed=em)

		time.sleep(1.4)

t = threading.Thread(target=worker)
t.start()