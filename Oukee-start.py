try:
	import requests,random
	from time import sleep
except Exception as Joker:exit(Joker)
r=requests.session()
lists = 'eobqxiqwertyuiopasdfghjklzxcvbnmxdizbeofbeo'
yes='Successfully registered. Please confirm your email.'
emlErr='User e-mail already exist.'
use='Username already exist.'
print("""
 ██████╗ ██╗   ██╗██╗  ██╗███████╗███████╗    
██╔═══██╗██║   ██║██║ ██╔╝██╔════╝██╔════╝    
██║   ██║██║   ██║█████╔╝ █████╗  █████╗      
██║   ██║██║   ██║██╔═██╗ ██╔══╝  ██╔══╝      
╚██████╔╝╚██████╔╝██║  ██╗███████╗███████╗ 
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝    
Check username |   By JOKER @vv1ck
""")
try:file=open(input('[*] Enter file username : '),'r')
except FileNotFoundError:exit('[-] The file name is incorrect')
def Check_Log():
	while True:
		user = file.readline().split('\n')[0]
		if user=='':exit('by joker \nis over')
		for item in range(5):
			emps = ''
		for item in range(12):
			emps += random.choice(lists)
		eml=emps+'@yahoo.com'
		msg=f"email: {eml} | pass: {emps}"
		headers={
		'Host': 'api.ouukee.cz',
		'Accept': 'application/json',
		'Content-Type': 'text/json',
		'Content-Length': '117',
		'X-Api-Key': 'ouukee',
		'User-Agent': 'OuKee/1.1.92 (cz.pixelmate.ouukee; build:92; iOS 13.5.0) Alamofire/5.2.2',
		'Accept-Language': 'en',
		'Accept-Encoding': 'gzip, deflate'}
		data={
			"email":eml,
			"password":emps,
			"username":f"@{user}",
			"password_confirmation":emps}
		sleep(1)
		send=r.post('https://api.ouukee.cz/api/v1/register',headers=headers,json=data).text
		if yes in send:
			print(f'━━━━━━━━━━━━━━━━━━━━━━━━━\n[+] available : {user} \n[{msg}]\n━━━━━━━━━━━━━━━━━━━━━━━━━')
			with open('new-user.txt', 'a') as J:J.write('user:'+user+' '+msg+'\n')
		elif use in send:print(f'[-] Not available : {user}')
		elif emlErr in send:pass
		else:print(send)
Check_Log()
