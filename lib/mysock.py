import socket
import epdb
MSGLEN=1024

class ccolors:
	OKGREEN='\033[92m'
	OKGRAY='\033[90m'
	OKPINK='\033[91m'
	OKYELLOW='\033[93m'
	OKBLUE='\033[94m'
	OKPURPLE='\033[95m'
	OKAQUA='\033[96m'
	OKWHITE='\033[97m'
	OKNEXT='\033[92m'
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
	statuses=[]
	kerneljiffies=0
	userjiffies=0
	def __init__(self,pid=0,statuses='',statline='',prio='',address=''):
		stats=statline.strip().split()
		self.pid=pid
		self.cmdline=statuses[1]
		self.statline=statline
		self.address=address
		self.statuses=statuses
		try:
			self.curState=stats[2]
		except IndexError:
			pass
		try:
			self.prio=stats[39]
		except IndexError:
			pass
		try:
			self.kerneljiffies=stats[14]
		except IndexError:
			pass
		try:
			self.userjiffies=stats[13]
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
		while len(msg) < 599900:
			chunk=self.sock.recv()
			msg+=chunk
		return msg

