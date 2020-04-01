import pygame
import pickle
import socket
import joystick
import codecs

from time import sleep
from joystick import myjoy
steer = 0
throttle = 0
brake = 0
button = 0

HOST = '192.168.1.2' # Server IP or Hostname
PORT = 6061 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#managing error exception
while True:
    try:
	s.bind((HOST, PORT))
    except socket.error:
	print("Bind failed")
	sleep(1)
	
	continue
    break

s.listen(5)
print("Socket awaiting messages")
(conn, addr) = s.accept()
print("Connected")

while True:
	
	x = myjoy()
	if x is not None:
	    try:		
		steer, throttle ,brake , button= myjoy()
		print(steer,throttle,brake , button, "1")
		#reply1 = {1:int(steer),2:int(throttle),3:int(brake),4:int(button)}
		reply1 = {1:str(steer),2:str(throttle),3:str(brake),4:str(button)}                
		reply = pickle.dumps(reply1)
		#reply = codecs.encode(pickle.dumps(reply1),"base64").decode()
	# Sending reply
		conn.send(reply)
		download1 = conn.recv(1024)
		print(download1,"2")
		#conn.close() # Close connection
		
	    except:
		reply1 = {1:str(steer),2:str(throttle),3:str(brake),4:str(button)}
                #reply = codecs.encode(pickle.dumps(reply1),"base64").decode()		
                reply = pickle.dumps(reply1)
		download1 = conn.recv(1024)
		print(download1,"3")
	# Sending reply
		conn.send(reply)
		
		#conn.close() # Close connection
		print(steer, throttle,brake ,button, "4")
	else:	
	    reply1 = {1:str(steer),2:str(throttle),3:str(brake),4:str(button)}
	    #reply = codecs.encode(pickle.dumps(reply1),"base64").decode() 
            reply = pickle.dumps(reply)
	# Sending reply
	    conn.send(reply1)
	    download1 = conn.recv(1024)
	    print(download1,"5")
	    
	    #conn.close() # Close connection
	    print(steer,throttle,brake)




	

	

