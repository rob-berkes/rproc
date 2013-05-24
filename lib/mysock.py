import socket
import epdb
MSGLEN=1024

class ccolors:
	OKGREEN='\033[92m'
	ENDC='\033[0m'

class clsProcs:
	pid=0
	cmdline=''
	cpu=0
	memory=0
	statline=''
	curState=''
	prio=''
	address=''
	def __init__(self,pid=0,cmdline='',statline='',prio='',address=''):
		stats=statline.strip().split()
		self.pid=pid
		self.cmdline=cmdline
		self.statline=statline
		self.address=address
		try:
			self.curState=stats[2]
			self.prio=stats[39]
		except IndexError:
			pass
		return
class mySock:
	def __init__(self,sock=None):
		if sock is None:
			self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		else:
			self.sock=sock

	def connect(self,host,port):
		self.sock.connect((host,port))
	def mybind(self,host,port):
		self.sock.bind((host,port))
	def mylisten(self,maxconns):
		self.sock.listen(maxconns)

	def mysend(self,msg):
		totalsent=0
		while totalsent<len(msg):
			sent=self.sock.send(msg)
			if sent==0:
				raise RuntimeError("socket connection broken")
			totalsent+=sent

	def myrecv(self):
		msg=''
		while len(msg) < MSGLEN:
			chunk=self.sock.recv(MSGLEN-len(msg))
			if chunk=='':
				raise RuntimeError("You fucked it up you dumbshit")
			msg+=chunk
		return msg

