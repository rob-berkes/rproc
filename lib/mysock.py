import socket
import epdb
from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

MSGLEN=1024
HERTZ=100

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


class rproc(Protocol):
	def connectionMade(self):
		self.transport.write('mesg recvd!')
		self.transport.loseConnection()

class rprocSrv(Factory):
	def buildProtocol(self,addr):
		return rproc()








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
	uptime=0
	def __init__(self,pid=0,statuses='',statline='',prio='',address='',uptime=''):
		stats=statline.strip().split()
		self.pid=pid
		self.cmdline=statuses[1]
		self.statuses=statuses
		self.statline=statline
		self.address=address
		self.uptime=uptime
		self.cutime=stats[15]
		self.cktime=stats[16]
		self.cputime=(float(self.cutime)+float(self.cktime)+float(self.userjiffies)+float(self.kerneljiffies))/100
		try:
			totaltime=0
			totaltime=int(stats[14])+int(stats[13])
			secsTot=float(self.uptime)-(float(stats[21])/100)
			self.cpu=100*((float(totaltime)/HERTZ)/float(secsTot))
		except IndexError:
			pass
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
		while totalsent<len(msg[totalsent:]):
			sent=self.sock.send(msg)
			if sent==0:
				raise RuntimeError("socket connection broken")
			totalsent+=sent

	def myrecv(self):
		msg=''
		while len(msg) < 999999:
			chunk=self.sock.recv(999999-len(msg))
			msg+=chunk
		return msg

class Echo(Protocol):
	def dataReceived(self,data):
		self.transport.write(data)
	def connectionMade(self):
		self.transport.write("Hello server, I am a client")
		self.transport.loseConnection()
