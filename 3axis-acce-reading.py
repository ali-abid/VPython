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

# Vector scale
vscale = 0.1
#Create ball sphere
ball = sphere(pos = vector(1,1,1), radius = 0.3, color=color.blue)
#Creae ball trail
ball.trail = curve(color=ball.color)
#create arrows
ball.vel = vector(5,10,0)
#Velocity vector arrow
#Create vector arrow
r = arrow(pos=vector(0,0,0), axis = vector(0,0,0), color=color.white, shaftwidth=0.1)


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
Xnum = []
Ynum = []
Znum = []
file = open('C:\Dev\workspace\VPython/2round.csv')
reader = csv.reader(file)
for line in reader:
    Xnum.append(line[1]),Ynum.append(line[2]),Znum.append(line[3])


scene.center=ball.pos #keep ball in view
#Graph
colorx = color.red
colory = color.green
colorz = color.blue
fgcolor=color.white
bgcolor=color.black
b1color = color.red
b2color = color.green
#Position graph
pos_graph = gdisplay(x=0, y=000, width=250, height=200, 
             title='Position vs. Time', xtitle='t(s)', ytitle='x (m)', 
             xmax=5., xmin=0., ymax=10, ymin=0, 
             foreground=fgcolor, background=bgcolor)
pos_Plot = gcurve(color=b1color)
#Velocity graph
vel_graph = gdisplay(x=0, y=200, width=250, height=200, 
             title='Velocity vs. Time', xtitle='t(s)', ytitle='v (m/s)', 
             xmax=5., xmin=0., ymax=10, ymin=0, 
             foreground=fgcolor, background=bgcolor)
vel_Plot = gcurve(color=b1color)
vel2_Plot = gcurve(color=b2color)
#Acceleration graph
acc_graph = gdisplay(x=0, y=400, width=250, height=200, 
             title='Acceleration vs. Time', xtitle='t(s)', ytitle='a (m/s^2)', 
             xmax=5., xmin=0., ymax=10, ymin=-0, 
             foreground=fgcolor, background=bgcolor)
acc_Plot = gcurve(color=b2color)

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
    #print(dt)
    
def updateXYZ(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    ball.vel = vector(x,y,z)*vscale
    ball.pos += ball.vel*dt
    a  = acc(time,ball.pos,ball.vel)
    ball.acc = a
    ball.vel += ball.acc*dt

def updateCar2spe(x,y,z):
    ball.pos = vector(cart2sph(x,y,z))
    #Draw trail along ball movement
    ball.trail.append(pos=vector(ball.pos.x,ball.pos.y,ball.pos.z))
    
#Position and Acceleration graph comparision
def posANDacc(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    ball.vel = vector(x,y,z)*vscale
    pos_Plot.plot(pos=(time,mag(ball.pos)))
    a = acc(time,ball.pos,ball.vel)
    ball.acc = a
    ball.pos += ball.vel*dt
    ball.vel += ball.acc*dt
    vel_Plot.plot(pos=(time,ball.vel.z))
    acc_Plot.plot(pos=(time,mag(ball.acc)))

def vectorVelocity(x,y,z):
    ball.vel = vector(float(Xnum[i]),float(Ynum[i]),float(Znum[i]))*vscale
    r = arrow(pos= ball.pos, axis = ball.vel*vscale, color=color.yellow)
    ball.color = color.red
    ball.pos = ball.pos + ball.vel*dt     #Update ball position 
    
for i in range(len(Xnum)-1):
    rate(5)
# This function calculate velocity and position of x y and z coordinates
    posANDacc(Xnum[i],Ynum[i],Znum[i])
    vectorVelocity(Xnum[i],Ynum[i],Znum[i])
    #updateCar2spe(Xnum[i],Ynum[i],Znum[i])
    scene.center=ball.pos-vector(0,1,0) #keep ball in view
    time = time + dt
    #print(time)
for i in range(len(Xnum)-1):
    rate(5)
    updateCar2spe(Xnum[i],Ynum[i],Znum[i])
    scene.center=ball.pos-vector(0,1,0) #keep ball in view
    time = time + dt
file.close()


