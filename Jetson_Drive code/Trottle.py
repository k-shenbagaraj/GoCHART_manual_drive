import pygame
from time import sleep
pygame.init()
pygame.joystick.init()
pygame.event.pump()


throttle = 0

#print pygame.my_joystick.Joystick(0)

while True:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
    #sleep(1)
    for event in pygame.event.get():

	pygame.event.pump()
	if event.type ==pygame.JOYAXISMOTION:
	    pygame.event.pump()	    
	    #print(my_joystick.get_axis(0))
	    throttle = my_joystick.get_axis(1)
	    #print(throttle)
	    pygame.event.pump()
            	  
	    

	    #print(event.value)
	#elif event.type ==pygame.JOYBUTTONDOWN:
	 #   print(event.button)
	
	     
        
        
   
