# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:34:31 2023

@author: Eason
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 22:18:37 2023

@author: Eason
"""

import pygame
import time

class move:
    def __init__(self,axes,buttons,avg_axes,avg_buttons):
        self.axe_ref = [axes[i]-avg_axes[i] for i in range(len(axes))]
        self.button = [buttons[i] for i in range(len(buttons))]
    def movement(self):
        foot = []
        arm= []
        button = []
        if self.axe_ref[1]<-.1:
            num = abs(self.axe_ref[1])
            num = round(num,1)
            foot.append("forward")
        elif self.axe_ref[1]>.1:
            num = abs(self.axe_ref[1])
            num = round(num,1)
            foot.append("backward")
        if self.axe_ref[0]<-.1:
            num = abs(self.axe_ref[0])
            num = round(num,1)
            foot.append("left")
        elif self.axe_ref[0]>.1:
            num = abs(self.axe_ref[0])
            num = round(num,1)
            foot.append("right")  
        if self.axe_ref[3]<-.1:
            num = abs(self.axe_ref[3])
            num = round(num,1)
            arm.append("forward")
        elif self.axe_ref[3]>.1:
            num = abs(self.axe_ref[3])
            num = round(num,1)
            arm.append("backward")
        if self.axe_ref[2]<-.1:
            num = abs(self.axe_ref[2])
            num = round(num,1)
            arm.append("left")
        elif self.axe_ref[2]>.1:
            num = abs(self.axe_ref[2])
            num = round(num,1)
            arm.append("right") 
            
        if self.button[0]>=0.9:
            num = abs(self.button[0])
            num = round(num,1)
            button.append("button 0")
        elif self.button[1]>=0.9:
            num = abs(self.button[1])
            num = round(num,1)
            button.append("button 1")
        elif self.button[2]>=0.9:
            num = abs(self.button[2])
            num = round(num,1)
            button.append("button 2")
            
        return [foot,arm,button]

# Initialize Pygame
pygame.init()

# Initialize joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

axes_list = []
buttons_list = []
for i in range(10):
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Read joystick input
    axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
    buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

    # Add input to list
    axes_list.append(axes)
    buttons_list.append(buttons)

# Calculate average of axes and buttons arrays
avg_axes = [sum(x) / 10 for x in zip(*axes_list)]
avg_buttons = [sum(x) / 10 for x in zip(*buttons_list)]

print(avg_axes)
print(avg_buttons)

url = "http://192.168.4.1/sendArray"  # Replace with the IP address of your ESP8266


# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Read joystick input
    instant_axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
    instant_buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
    
    
    if instant_buttons[7]==1:
        # Quit game
        pygame.quit()
    
    agent = move(instant_axes,instant_buttons,avg_axes,avg_buttons)
    ret = agent.movement()
    
    if len(ret[0]) != 0:
        print(ret[0][0])
        if ret[0][0] == "forward":
            response = requests.post(url, data=json.dumps([90,0,0,1,1]))
        elif ret[0][0] == "backward":
            response = requests.post(url, data=json.dumps([90,0,0,2,2]))
        elif ret[0][0] == "left":
            response = requests.post(url, data=json.dumps([90,0,0,2,1]))
        elif ret[0][0] == "right":
            response = requests.post(url, data=json.dumps([90,0,0,1,2]))
        
    if len(ret[1]) != 0:
        print("arm: ",ret[1])
        
        
    if len(ret[2]) != 0:
        print("button: ",ret[2])
        
    
    time.sleep(0.05)
    
    
        
