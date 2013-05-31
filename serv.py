import socket
import pickle
import lib.mysock
import epdb
import time
MSGLEN=32000
TIMEOUT=3

def print_cls(PROCLIST):
	s=time.time()
	for proc in PROCLIST:
		print str(time.strftime("%D %T"))+" From: "+lib.mysock.ccolors.OKNEXT+str(address[0])+lib.mysock.ccolors.ENDC+" PID: "+str(proc.pid)+" CPU Load: "+str(round(proc.cpu,3))+" CMD:"+str(proc.cmdline)
	return	

server=lib.mysock.mySock()
server.mybind('0.0.0.0',8822)
server.mylisten(5)
PROCLIST=[]
msg=''
begin=time.time()
while 1:
	if len(msg)>1 and time.time()-begin > TIMEOUT:
		break
	elif time.time()-begin > (TIMEOUT*2):
		break
	(clientsocket, address)=server.sock.accept()

	msgSt=clientsocket.recv(MSGLEN)
	msg=pickle.loads(msgSt)
	print_cls(msg)
	begin=time.time()




