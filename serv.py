import lib.mysock
MSGLEN=1024
server=lib.mysock.mySock()
server.mybind('0.0.0.0',8822)
server.mylisten(5)

while 1:
	(clientsocket, address)=server.sock.accept()
	msg=clientsocket.recv(MSGLEN)
	print msg
        continue

