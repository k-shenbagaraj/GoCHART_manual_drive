import pygame
from time import sleep
pygame.init()
pygame.joystick.init()
pygame.event.pump()

steer = 0 
throttle = 0
brake = 0
button = 0

def myjoy():
	
	my_joystick = pygame.joystick.Joystick(0)
	my_joystick.init()
	sleep(0.1)
	       
	for event in pygame.event.get():
  	    if event.type ==pygame.JOYAXISMOTION:
		pygame.event.pump()	
		
		global steer
		global throttle
		global brake
		global button		
		steer = my_joystick.get_axis(0) *10000
		throttle = (my_joystick.get_axis(1))*10 
		brake = my_joystick.get_axis(2)
		pygame.event.pump()
			
	    elif event.type == pygame.JOYBUTTONDOWN:
		button = 0
		button = event.button
		
	return steer, throttle , brake , button
	 

	
	     
        
        
   
