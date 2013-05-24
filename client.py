import lib.mysock
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
		PIDLIST.append(lib.mysock.clsProcs(pid=pid,cmdline=cmdline.read(),statline=statline.read()))
		cmdline.close()
		statline.close()
	return PIDLIST
def build_rproc_list(PIDLIST):
	MSG=[]
	for PROC in PIDLIST:
		if PROC.curState=='R':
			MSG.append(lib.mysock.clsProcs(pid=PROC.pid,cmdline=PROC.cmdline,statline=PROC.statline))
	return MSG

def build_msg_list(MSGLIST):
	msg=''
	for PROC in MSGLIST:
		msg+=str(PROC.pid)+','+str(PROC.cmdline)+','+str(PROC.prio)+','
	return msg	
INTERVAL=10
pids=[]
s=Connect()
while 1:
	PIDLIST=[]
	msg=''
	PIDLIST=build_pidlist()
	MSGLIST=build_rproc_list(PIDLIST)
	msg=build_msg_list(MSGLIST)
	s.mysend((msg))
	time.sleep(INTERVAL)	
	continue
