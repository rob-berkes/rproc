import lib.mysock
import pickle
import re
import os
import epdb
import time

def Connect():
	s=lib.mysock.mySock()
	s.sock.connect(("0.0.0.0",8822))
	return s
def build_pidlist():
	pids=[pid for pid in os.listdir('/proc/') if pid.isdigit()]
	for pid in pids:
		cmdline=open('/proc/'+str(pid)+'/cmdline','r')
		statline=open('/proc/'+str(pid)+'/stat','r')
		statusline=open('/proc/'+str(pid)+'/status','r')
		statuses=re.split('\W+',statusline.read())
		PIDLIST.append(lib.mysock.clsProcs(pid=pid,statuses=statuses,statline=statline.read()))
		cmdline.close()
		statline.close()
	return PIDLIST
def build_rproc_list(PIDLIST):
	MSG=[]
	for PROC in PIDLIST:
		if PROC.cmdline=='Terminal':
			MSG.append(lib.mysock.clsProcs(pid=PROC.pid,statuses=PROC.statuses,statline=PROC.statline))
	return MSG

def build_msg_list(MSGLIST):
	msg=[]
	for PROC in MSGLIST:
		msg.append(lib.mysock.clsProcs(pid=PROC.pid,statuses=PROC.statuses,statline=PROC.statline))
	return msg	
INTERVAL=10
pids=[]
while 1:
	s=Connect()
	PIDLIST=[]
	msg=''
	PIDLIST=build_pidlist()
	MSGLIST=build_rproc_list(PIDLIST)
	msg=build_msg_list(MSGLIST)
	msgSt=pickle.dumps(msg)
	print len(msgSt)
	s.mysend((msgSt))
	s.sock.shutdown(1)
	time.sleep(INTERVAL)	
	continue
