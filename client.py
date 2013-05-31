import lib.mysock
import pickle
import re
import os
import epdb
import time
INTERVAL=60
SERVERIP='0.0.0.0'


def loadInitFile():
	IFILE=open('client.conf','r')
	s=re.split('\s+',IFILE.read())
	for a in range(0,len(s)):
		if s[a]=='server':
			SERVERIP=s[a+1]
	return SERVERIP

def Connect():
	s=lib.mysock.mySock()
	s.sock.connect((SERVERIP,8822))
	return s
def build_pidlist():
	pids=[pid for pid in os.listdir('/proc/') if pid.isdigit()]
	for pid in pids:
		cmdline=open('/proc/'+str(pid)+'/cmdline','r')
		statline=open('/proc/'+str(pid)+'/stat','r')
		statusline=open('/proc/'+str(pid)+'/status','r')
		uptime=open('/proc/uptime','r')
		uptimes=uptime.read().strip().split(' ')
		statuses=re.split('\W+',statusline.read())
		PIDLIST.append(lib.mysock.clsProcs(pid=pid,statuses=statuses,statline=statline.read(),uptime=uptimes[0]))
		cmdline.close()
		statline.close()
	return PIDLIST
def build_rproc_list(PIDLIST):
	MSG=[]
	for PROC in PIDLIST:
		if PROC.cpu>1 :
			MSG.append(lib.mysock.clsProcs(pid=PROC.pid,statuses=PROC.statuses,statline=PROC.statline,uptime=PROC.uptime))
	return MSG

def build_msg_list(MSGLIST):
	msg=[]
	for PROC in MSGLIST:
		msg.append(lib.mysock.clsProcs(pid=PROC.pid,statuses=PROC.statuses,statline=PROC.statline,uptime=PROC.uptime))
	return msg	
pids=[]
SERVERIP=loadInitFile()
while 1:
	s=Connect()
	PIDLIST=[]
	msg=''
	PIDLIST=build_pidlist()
	MSGLIST=build_rproc_list(PIDLIST)
	msg=build_msg_list(MSGLIST)
	msgSt=pickle.dumps(msg)
	s.mysend((msgSt))
	s.sock.shutdown(1)
	time.sleep(INTERVAL)	
	continue
