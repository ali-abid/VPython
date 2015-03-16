# Three axis accelerometer data reading
# Version 1.0 (March. 12, 2015)
# Abid Ali
#IMaR Gateway Technology, Institute of Technology

from __future__ import print_function, division
from visual import *
from random import *
import numpy as np
import math as m
import csv
from visual.graph import *

PI = math.pi
DEG = PI/180
scene.x = 0
scene.y = 0
scene.width = 600
scene.height = 600
scene.autoscale = 0
scene.title = "3 axis accelro reading"
scene.range = (2,2,2)

#create arrows
#myArrow = arrow(axis=(1,0,0), fixedwidth=1, shaftwidth=0.1)
arrow(color=color.red, axis=(1,0,0), shaftwidth=0.01, fixedwidth=1)
arrow(color=color.green, axis=(0,1,0), shaftwidth=0.01, fixedwidth=1)
arrow(color=color.blue, axis=(0,0,1), shaftwidth=0.01, fixedwidth=1)
#arrow title
xLabel = label(pos = (1,0,0), text = "X", box = False, color = color.red)
yLabel = label(pos = (0,1,0), text = "Y", box = False, color = color.green)
zLabel = label(pos = (0,0,1), text = "Z", box = False, color = color.blue)

#adjest arrow setting
scene.autoscale=0
scene.eye=vector(0,0,0)
scene.up=vector(0,1,0)


#Reading x y and z data from file
accX = []
accY = []
accZ = []
file = open('C:\Dev\workspace\VPython/xyz36round.csv')
reader = csv.reader(file)
for line in reader:
    accX.append(line[1]),accY.append(line[2]),accZ.append(line[3])

<<<<<<< HEAD
#Graph
fgcolor=color.white
bgcolor=color.black
b1color=color.red
posx_graph = gdisplay(x=0, y=000, width=250, height=150, 
             title='x-Position vs. Time', xtitle='t(s)', ytitle='x (m)', 
             xmax=50, xmin=0., ymax=30, ymin=-10, 
             foreground=fgcolor, background=bgcolor)
posx_Plot = gcurve(color=b1color)

#Calculate speed of x y x corrdinates distance per second



#Calculate velocity of deltaX delataY and deltaZ displacement per second 

#Calculate Accecleration of deltaVelocity of x y and z per second square

#plot graphs


    
=======


>>>>>>> 737b130626bb18d733e6758a454b0f57d2fa6e4d
file.close()


