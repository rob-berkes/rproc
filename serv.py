import lib.mysock
import epdb
MSGLEN=1024


def convert_msg_to_cls(msg,address):
	PROCS=[]
	COUNT=0
	msglen=len(msg)
	msgs=msg.strip().split(',')
	while COUNT<msglen:
		try:
			PROCS.append(lib.mysock.clsProcs(pid=msgs[COUNT+0],cmdline=msgs[COUNT+1],prio=msgs[COUNT+2],address=address))
		except IndexError:
			break
		COUNT+=3
	return PROCS
def print_cls(PROCLIST):
	for proc in PROCLIST:
		print "From: "+lib.mysock.ccolors.OKGREEN+str(address[0])+lib.mysock.ccolors.ENDC+" PID: "+str(proc.pid)+" PRIO: "+str(proc.prio)+" CMD:"+str(proc.cmdline)+"\n"
	return	

server=lib.mysock.mySock()
server.mybind('0.0.0.0',8822)
server.mylisten(5)
PROCLIST=[]
while 1:
	(clientsocket, address)=server.sock.accept()
#	epdb.st()
	msg=clientsocket.recv(MSGLEN)
	PROCLIST=convert_msg_to_cls(msg,address[0])
	print_cls(PROCLIST)
        continue

