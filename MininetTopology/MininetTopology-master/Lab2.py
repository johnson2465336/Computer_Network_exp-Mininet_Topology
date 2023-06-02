from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.node import RemoteController, OVSSwitch
import os

def main():
	OFSwitchList = []
	HostListA = []
	HostListB = []
	net = Mininet(controller = None, link = TCLink)

	for i in range(3):
		OFSwitchList.append(net.addSwitch("s%d"%(i+1), cls = OVSSwitch))

	for i in range(1,5):
		HostListA.append(net.addHost("A%d"%i, ip = "10.0.0.%d/24"%i, mac = "00:04:00:00:00:%02x"%i))
		HostListB.append(net.addHost("B%d"%i, ip = "10.0.1.%d/24"%i, mac = "00:05:00:00:00:%02x"%i))

	
	net.addLink(OFSwitchList[0], OFSwitchList[1], bw=100)
	net.addLink(OFSwitchList[1], OFSwitchList[2], bw=100)
	net.addLink(OFSwitchList[2], OFSwitchList[0], bw=100)
	
	net.addLink(HostListA[0], OFSwitchList[0], bw=100)
	net.addLink(HostListA[1], OFSwitchList[1], bw=100)
	net.addLink(HostListA[2], OFSwitchList[2], bw=100)
	net.addLink(HostListA[3], OFSwitchList[0], bw=100)
	
	net.addLink(HostListB[0], OFSwitchList[0], bw=100)
	net.addLink(HostListB[1], OFSwitchList[2], bw=100)
	net.addLink(HostListB[2], OFSwitchList[2], bw=100)
	net.addLink(HostListB[3], OFSwitchList[1], bw=100)	
	
	net.start()
	HostListA[0].cmd("ip route add default dev A%d-eth0"%(1))
	HostListB[0].cmd("ip route add default dev B%d-eth0"%(1))
	for i in range(1,4):	
		HostListA[i].cmdPrint("tcpdump -i A%d-eth0 port 50000 |tee A%d-output.log &"%(i+1,i+1))
		HostListB[i].cmdPrint("tcpdump -i B%d-eth0 port 50000 |tee B%d-output.log & "%(i+1,i+1))
		HostListA[i].cmd("ip route add default dev A%d-eth0"%(i+1))
		HostListB[i].cmd("ip route add default dev B%d-eth0"%(i+1))
	CLI(net)
	os.system("killall tcpdump")
	net.stop()

if __name__ == "__main__":
	setLogLevel( "info" )
	main()
