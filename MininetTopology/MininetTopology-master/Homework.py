from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.node import RemoteController, OVSSwitch

def main():
	net = Mininet(controller = None, link = TCLink)
	OFSwitchList = []
	for i in range(5):
		OFSwitchList.append(net.addSwitch("s%s"%str(i+1), cls = OVSSwitch))
	h1 = net.addHost("h1", ip = "10.0.0.1/24", mac = "00:04:00:00:00:02")
	h2 = net.addHost("h2", ip = "10.0.0.2/24", mac = "00:05:00:00:00:02")

	net.addLink(h1, OFSwitchList[0], bw=100)
	net.addLink(h2, OFSwitchList[4], bw=100)
	
	net.addLink(OFSwitchList[0], OFSwitchList[1], bw=100)	
	net.addLink(OFSwitchList[0], OFSwitchList[2], bw=100)	
	net.addLink(OFSwitchList[0], OFSwitchList[3], bw=100)	
	
	net.addLink(OFSwitchList[4], OFSwitchList[1], bw=100)	
	net.addLink(OFSwitchList[4], OFSwitchList[2], bw=100)	
	net.addLink(OFSwitchList[4], OFSwitchList[3], bw=100)	
	
	net.start()
	h2.cmdPrint("iperf -s -u -p 50001 > 50001-s.log &")
	h2.cmdPrint("iperf -s -u -p 50002 > 50002-s.log &")
	h2.cmdPrint("iperf -s -u -p 50003 > 50003-s.log &")
	h1.cmdPrint("arp -s 10.0.0.2 00:05:00:00:00:02")
	h2.cmdPrint("arp -s 10.0.0.1 00:04:00:00:00:02")
	
	CLI(net)
	net.stop()

if __name__ == "__main__":
	setLogLevel( "info" )
	main()
