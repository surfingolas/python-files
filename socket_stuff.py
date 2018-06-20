import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/mbox-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    stuff = mysock.recv(512)
    if (len(stuff) < 1):
        break
    print(stuff.decode())
mysock.close()
