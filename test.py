"""
This file is now a test to commit changes 
"""

#%% Import required modules 
import numpy as np 

#%% Def the required functions 
def circumference(radius):
	circumference = (radius *2*np.pi)
	return circumference
def area(radius):
	area = radius**radius*np.pi
	return area 

#%% Execute the code 
radius = 0.5 
print('the circumference of a circle with  radius {} = {}'.format(radius, circumference(radius)))
print('the area of a circle with radius {} = {}'.format(radius,area(radius)))

