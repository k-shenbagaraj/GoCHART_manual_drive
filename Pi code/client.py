import socket
import pickle
import re
from time import sleep

HOST = '192.168.1.2'
PORT = 6061
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     
s.connect((HOST,PORT))
    

reply = 0
def socket_value():
    #sleep(1)
    global reply
    reply1 = s.recv(1024)
    reply = pickle.loads(reply1)
    #reply=re.split (r'\s',reply)
    #print(reply)

    upload = s.send(reply1)
    #print("uploaded")
    return reply
    
