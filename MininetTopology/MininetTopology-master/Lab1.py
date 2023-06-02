from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.node import RemoteController, OVSSwitch

def main():
	OFSwitchList = []
	HostList = []
	net = Mininet(controller = None, link = TCLink)

	for i in range(1):
		OFSwitchList.append(net.addSwitch("s%s"%str(i+1), cls = OVSSwitch))

	for i in range(2):
		HostList.append(net.addHost("h%s"%str(i+1), ip = "10.0.0.%s/24"%str(i+1), mac = "00:04:00:00:00:%s"%str(i+1)))

	net.addLink(HostList[0], OFSwitchList[0], bw=100)
	net.addLink(HostList[1], OFSwitchList[0], bw=100)

	net.start()
	CLI(net)
	net.stop()

if __name__ == "__main__":
	setLogLevel( "info" )
	main()
