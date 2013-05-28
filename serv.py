import socket
import pickle
import lib.mysock
import epdb
MSGLEN=1024


def print_cls(PROCLIST):
	for proc in PROCLIST:
		print "From: "+lib.mysock.ccolors.OKNEXT+str(address[0])+lib.mysock.ccolors.ENDC+" PID: "+str(proc.pid)+" KernelTime: "+str(proc.kerneljiffies)+" UserTime: "+str(proc.userjiffies)+" CMD:"+str(proc.cmdline)+"\n"
	return	

server=lib.mysock.mySock()
server.mybind('0.0.0.0',8822)
server.mylisten(5)
PROCLIST=[]
while 1:
	(clientsocket, address)=server.sock.accept()
	msgSt=clientsocket.recv(999999)
	msg=pickle.loads(msgSt)
	print_cls(msg)
        continue

