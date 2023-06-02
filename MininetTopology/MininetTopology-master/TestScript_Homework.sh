#!/bin/bash
iperf -c 10.0.0.2 -u -b 1000M -t 10 -B 0.0.0.0:50001 -p 50001 -i 1 > 50001-c.log &
iperf -c 10.0.0.2 -u -b 1000M -t 10 -B 0.0.0.0:50002 -p 50002 -i 1 > 50002-c.log &
iperf -c 10.0.0.2 -u -b 1000M -t 10 -B 0.0.0.0:50003 -p 50003 -i 1 > 50003-c.log & 
for i in $(seq 1 10); do
	echo "Testing, $i"
	sleep 1
done
