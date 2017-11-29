DOS ATTACK MULTIPLE IP MULTIPLE PORT

In this section, we are going to discuss one of the most deadly attacks, called the Denial-of-Service attack. The aim of this attack is to consume machine or network resources, making it unavailable for the intended users. Generally, attackers use this attack when every other attack fails. This attack can be done at the data link, network, or application layer. Usually, a web server is the target for hackers. In a DoS attack, the attacker sends a huge number of requests to the web server, aiming to consume network bandwidth and machine memory. In a Distributed Denial-of-Service (DDoS) attack, the attacker sends a huge number of requests from different IPs. In order to carry out DDoS, the attacker can use Trojans or IP spoofing. In this section, we will carry out various experiments to complete our reports.

In this section, we will discuss the multiple IP with multiple port addresses. In this attack, we use different IPs to send the packet to the target. Multiple IPs denote spoofed IPs. The following program will send a huge number of packets from spoofed IPs:

In the preceding code, we used the a, b, c, and d variables to store four random strings, ranging from 1 to 254. The src variable stores random IP addresses. Here, we have used the loop_exit variable to break the for loop after 50 packets. It means 10 packets originate from one IP while the rest of the code is the same as the previous one.

Let's check program:

Kali Linux 2.0
Python 2.7 (you can regulate for 3.x )
Scapy Library
IDE (gedit yeterli bizim için)
WireShark kurulu Test Makinesi (windows..)


Kali Packet Update:

sudo apt-get upgrade
sudo apt-get update
Scapy Kütüphanesi Güncellemesi:

pip install scapy

or

set Scapy final library: http://scapy.net/

cd /tmp
wget --trust-server-names scapy.net   # or wget -O scapy.zip scapy.net
unzip scapy-x.x.x.zip
cd scapy
sudo python setup.py install








