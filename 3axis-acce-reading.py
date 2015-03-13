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
myArrow = arrow(axis=(1,0,0), fixedwidth=1, shaftwidth=0.1)
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
#scene.forward=vector(0,0,0)
calibrate=vector(0,0,0)

#Reading x y and z data from file
accX = []
accY = []
accZ = []
file = open('C:\Dev\workspace\VPython/xyz36round.csv')
reader = csv.reader(file)
for line in reader:
    accX.append(line[1]),accY.append(line[2]),accZ.append(line[3])

#Acceleration function
def acc(t,x,v):
    radiusvect=x
    r=mag(radiusvect)
    rhat=radiusvect/r
    mag_a=mag2(v)/r
    return vector(-mag_a*rhat.x,-mag_a*rhat.y,0)
#define box
b1color = color.red
block_height=0.25
tracklength=2 #track
track = box(pos=(tracklength/2,-0.05,0), axis=(1,0,0), length=tracklength, height=.1, width=2, color=color.orange)
c=[] #tick mark on track
for x in arange(tracklength):
    cu = curve(z = arange(-1,2,1), color=(0.25,0.25,1.0))
    c.append(cu)
    c[x].y = 0.01
    c[x].x = x

pos_init=vector(0,0,0) # setup (do not edit these components)
vel_init=vector(1,2,2) 
pos_init.y=0. ; pos_init.z=0 # setup initial POSITIONS (sit on track)
block = box(pos=pos_init, axis=track.axis,
        length=block_height, height=block_height, width=block_height, color=b1color)
block.vel = vel_init 







for i in range(len(accX)-1):
    rate(5)
    myArrow.axis=vector(float(accX[i]),float(accY[i]),float(accZ[i]))-calibrate
    

file.close()


