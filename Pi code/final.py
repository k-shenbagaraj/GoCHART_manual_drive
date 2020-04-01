import re
from client import *
import serial
import os

if os.path.exists ('/dev/ttyACM0') == True:
    port = "/dev/ttyACM0"
    print("ACM0")
    
elif os.path.exists ('/dev/ttyACM1') == True:
    port = "/dev/ttyACM1"
    print("ACM1")

elif os.path.exists ('/dev/ttyACM2') == True:
    port = "/dev/ttyACM2"
    print("ACM2")


    
baudrate = 9600
ser =serial.Serial(port, baudrate)
   
msg = 0
received = 0

def send(msg):
    msg = str(msg)
    msg = msg + '\n'
    x = msg.encode('ascii')
    ser.write(x)
    

def receive():
    global received
    received = ser.read_until()
    return received

    
while True:
    joystick_val = socket_value()
    joystick_val = str(joystick_val)
    #print(joystick_val)
    joystick_split = re.split(r'\s',joystick_val)
    #rec = receive()
    #print(rec)
    
    joy = joystick_split[1]
    joy =joy.replace(',','')
    joy =joy.replace(' ','')
    joy =joy.replace("'","")
    
    joy = (float(joy))
    print(joy,"joy")
    if (joy>3000):
        joy=3000
    elif (joy<-3000):
        joy=-3000
    joy = int(float(joy/60)+50)
    print(joy,"joy")
    
    acc = joystick_split[3]
    acc =acc.replace(',','')
    acc =acc.replace(' ','')
    acc =acc.replace("'","")
    acc = int(float(acc)*10)
    acc = (200-(acc+100))
    print(acc,"acc")
    
    button = joystick_split[7]
    button =button.replace(',','')
    button =button.replace(' ','')
    button =button.replace("'","")
    button =button.replace('}',"")
    print(button)
    button = int(float(button))
    
    send_val = 10000000 + button*1000000+ acc*1000+ joy 
    print(send_val)
    send(send_val)
    print("sent")	
    #send(joystick_split[2])
    #rec = receive()
    	
    
    
    