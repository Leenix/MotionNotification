#!/usr/bin/env python

import socket
import datetime

SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8888

# Connect to the server
client_socket = socket.socket()
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Send the payload
payload = {'id': 'noise_request', 'timestamp': datetime.datetime.now().isoformat()}
client_socket.send(str(payload) + '\n')
client_socket.close()
