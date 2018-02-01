import time
from datetime import datetime as dt

hpath = '/etc/hosts'
websites = ['www.facebook.com', 'facebook.com']
redir = '127.0.0.1'
# Ask user to input block timeframe
wrkbg = int(input('Start time: '))
wrknd = int(input('End time: '))

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, wrkbg) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, wrknd):
		with open(hpath, 'r+') as file:
			data = file.read()
			for site in websites:
				if site in data:
					pass
				else:
					file.write(redir + ' ' + site + '\n')
					print('Blocked: ' + site)
	else:
		with open(hpath, 'r+') as file:
			data = file.readlines()
			file.seek(0)
			for line in data:
				if not any(site in line for site in websites):
					file.write(line)					
			file.truncate()
			print('All websites allowed')

	time.sleep(300)