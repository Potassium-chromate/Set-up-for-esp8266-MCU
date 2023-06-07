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
        self.button = [buttons[i]-avg_buttons[i] for i in range(len(buttons))]
    def movement(self):
        foot = []
        arm= []
        button = []
        if self.axe_ref[1]<-.1:
            num = abs(self.axe_ref[1])
            num = round(num,1)
            foot.append("foward :"+str(num))
        elif self.axe_ref[1]>.1:
            num = abs(self.axe_ref[1])
            num = round(num,1)
            foot.append("backward :"+str(num))
        if self.axe_ref[0]<-.1:
            num = abs(self.axe_ref[0])
            num = round(num,1)
            foot.append("left :"+str(num))
        elif self.axe_ref[0]>.1:
            num = abs(self.axe_ref[0])
            num = round(num,1)
            foot.append("right :"+str(num))  
        if self.axe_ref[3]<-.1:
            num = abs(self.axe_ref[3])
            num = round(num,1)
            arm.append("foward :"+str(num))
        elif self.axe_ref[3]>.1:
            num = abs(self.axe_ref[3])
            num = round(num,1)
            arm.append("backward :"+str(num))
        if self.axe_ref[2]<-.1:
            num = abs(self.axe_ref[2])
            num = round(num,1)
            arm.append("left :"+str(num))
        elif self.axe_ref[2]>.1:
            num = abs(self.axe_ref[2])
            num = round(num,1)
            arm.append("right :"+str(num)) 
            
        if self.button[0]==1:
            num = abs(self.button[0])
            num = round(num,1)
            button.append("button :"+str(num))
         
            
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
        
        print("foot: ",ret[0])
    if len(ret[1]) != 0:
        print("arm: ",ret[1])
        
    if len(ret[2]) != 0:
        print("button: ",ret[2])
    
    time.sleep(0.15)
    
    
        
