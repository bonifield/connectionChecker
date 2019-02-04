#!/usr/bin/python3

import os, subprocess, time

ips = ['1.1.1.1', '8.8.8.8', '9.9.9.9']

def loggy(ip, status):
	with open('/var/log/pinglog/pinglog.log', 'a') as f:
		f.write('{} {} {}\n'.format(time.strftime("%s"), ip, status))
	f.close()

def pingy(ip):
	NULLY = open(os.devnull, 'w')
	p = subprocess.call(['ping', '-W', '1', '-c', '1', ip], stdout=NULLY, stderr=NULLY)
	if p == 0:
		loggy(ip, 'reachable')
	else:
		loggy(ip, 'unreachable')
	NULLY.close()

# run 12 times during the 1-minute cron window
for i in range(12):
	for ip in ips:
		pingy(ip)
	time.sleep(5)
