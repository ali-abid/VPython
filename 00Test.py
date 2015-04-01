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
import re
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

#Create ball sphere
ball = sphere(pos = vector(1,1,1), radius = 0.3, color=color.blue)

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

s = "Hello"
print(s[0])

#Reading x y and z data from file
Xnum = []
Ynum = []
Znum = []
file = open('C:\Dev\workspace\VPython/testgolf-1-14-58.csv', 'rU')
reader = csv.reader(file)
for line in reader:
    reader.next() # This function make space in line
    Xnum.append(line[1]),Ynum.append(line[2]),Znum.append(line[3])
    #Xnum.append(line[1])
    #print(line[1])  
    

for i in range(len(Xnum)-1):
    print(Ynum[i])

# Vector scale
vscale = 0.1

#Graph
colorx = color.red
colory = color.green
colorz = color.blue
fgcolor=color.white
bgcolor=color.black

#Velocity graph
vel_graph = gdisplay(x=0, y=200, width=250, height=200, 
             title='Velocity vs. Time', xtitle='t(s)', ytitle='v (m/s)', 
             xmax=50, xmin=0., ymax=10, ymin=0, 
             foreground=fgcolor, background=bgcolor)
vel_Plot = gcurve(color=colory)


#Acceleration graph
acc_graph = gdisplay(x=0, y=400, width=250, height=200, 
             title='Acceleration vs. Time', xtitle='t(s)', ytitle='a (m/s^2)', 
             xmax=50, xmin=0., ymax=1, ymin=-1, 
             foreground=fgcolor, background=bgcolor)
acc_Plot = gcurve(color=colorx)


PI=math.pi
DEG=PI/180

ball.vel = vector(1.0*cos(70*DEG),1.0*sin(70*DEG),0)
time = 0.1
dt = 0.07
g = 0.1
def acc(t,x,v):
    radiusvect = x
    r = mag(radiusvect)
    rhat = radiusvect/r
    mag_a = mag2(v)/r
    return vector(-mag_a*rhat.x,-mag_a*rhat.y,0)
    
def cart2sph(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    XsqPlusYsq = x**2 + y**2
    r = m.sqrt(XsqPlusYsq + z**2)#r
    elev = m.atan2(z,m.sqrt(r))#phi
    az = m.atan2(y,x)#theta
    return r, elev, az


#// velocity
#vx += ((ax + ax0)/2) * (t - t0);
#vy += ((ay + ay0)/2) * (t - t0);
#vz += ((az + az0)/2) * (t - t0);
#// position;
#px += ((vx + vx0)/2) * (t - t0);
#py += ((vy + vy0)/2) * (t - t0);
#pz += ((vz + vz0)/2) * (t - t0);
def updateVel(x,y,z):
    vx = 0
    vx0 = 0
    ax0 = 0
    px = 0
    x = float(x)
    y = float(y)
    z = float(z)
    ball.vel = vector(x,y,z)*vscale
    a = acc(time, ball.pos, ball.vel)
    ax = a.x
    # Velocity of x
    vx += ((ax + ax0)/2) * (dt)
    ax0 = ax
    #Positin of x
    px += ((vx + vx0)/2) * (dt)
    vx0 = vx
    velx_Plot.plot(pos=(time,vx))
    velx_Plot2.plot(pos=(time,px))
    print(dt)
    

    
#Velocity vs Time and Acceleration vs Time Graph function
def posANDacc(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    ball.vel = vector(x,y,z)*vscale
    a = acc(time,ball.pos,ball.vel)
    print(ball.vel)
    ball.acc = a
    ball.pos += ball.vel*dt
    ball.vel += ball.acc*dt
    vel_Plot.plot(pos=(time,mag(ball.vel)))
    #velx_Plot.plot(pos=(time,mag(ball.pos)))       #Plot Postion of object
    acc_Plot.plot(pos=(time,mag(ball.acc)))       #Plot Acceleration 

#This method show velocity vector and ball position 
def vectorVelocity(x,y,z):
    ball.vel = vector(float(Xnum[i]),float(Ynum[i]),float(Znum[i]))*vscale
    r = arrow(pos= ball.pos, axis = ball.vel*vscale, color=color.yellow)
    ball.pos = ball.pos + ball.vel*dt     #Update ball position

#Main Loop 
for i in range(len(Xnum)-1):
    rate(50)
# This function calculate velocity and position of x y and z coordinates
    #vectorVelocity(Xnum[i],Ynum[i],Znum[i]) # This will show moving vector direction
    posANDacc(Xnum[i],Ynum[i],Znum[i])      # This will show graph
    scene.center=ball.pos-vector(0,1,0) #keep ball in view
    time = time + dt

file.close()
