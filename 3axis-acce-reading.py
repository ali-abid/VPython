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

#Create ball sphere
ball = sphere(pos = vector(0,0,0), radius = 0.3, color=color.blue)

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
Xnum = []
Ynum = []
Znum = []
file = open('C:\Dev\workspace\VPython/xyz36round.csv')
reader = csv.reader(file)
for line in reader:
    Xnum.append(line[1]),Ynum.append(line[2]),Znum.append(line[3])

# Vector scale
vscale = 0.1

#Graph
colorx = color.red
colory = color.green
colorz = color.blue
fgcolor=color.white
bgcolor=color.black
posx_graph = gdisplay(x=0, y=000, width=250, height=150, 
             title='x-Position vs. Time', xtitle='t(s)', ytitle='x (m)', 
             xmax=50, xmin=0., ymax=30, ymin=-10, 
             foreground=fgcolor, background=bgcolor)
posx_Plot = gcurve(color=colorx)

velx_graph = gdisplay(x=0, y=150, width=250, height=150, 
             title='x-Velocity vs. Time', xtitle='t(s)', ytitle='vx (m/s)', 
             xmax=50., xmin=0., ymax=30, ymin=-2, 
             foreground=fgcolor, background=bgcolor)
velx_Plot = gcurve(color=colorx)

acc_graph = gdisplay(x=0, y=400, width=250, height=200, 
             title='Acceleration vs. Time', xtitle='t(s)', ytitle='a (m/s^2)', 
             xmax=40, xmin=0., ymax=2, ymin=0, 
             foreground=fgcolor, background=bgcolor)
acc_Plot = gcurve(color=color.yellow)



time = 0
dt = 0.07
g = 0.1
def acc(t,x,v):
    return vector(0.,-g,0.)
    

def updateXYZ(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    ball.vel = vector(x,y,z)*vscale
    ball.pos += ball.vel*dt
    a  = acc(time,ball.pos,ball.vel)
    ball.acc = a
    ball.vel += ball.acc*dt


for i in range(len(Xnum)-1):
    rate(10)
    updateXYZ(Xnum[i],Ynum[i],Znum[i])
    arrow(pos=ball.pos,axis=ball.vel/2.*vscale,color=color.yellow,fixedwidth = 1)
    arrow(pos=ball.pos,axis=(ball.vel.x/2.*vscale,0,0),color=colorx,fixedwidth = 1)
    arrow(pos=ball.pos,axis=(0,ball.vel.y/2.*vscale,0),color=colory,fixedwidth = 1)
    arrow(pos=ball.pos,axis=(0,0,ball.vel.z/2.*vscale),color=colorz,fixedwidth = 1)
#Calculate speed of x y x corrdinates distance per second
    posx_Plot.plot(pos=(time,ball.pos.x))
#Calculate velocity of deltaX delataY and deltaZ displacement per second
    velx_Plot.plot(pos=(time,ball.vel.x))
#Calculate Accecleration of deltaVelocity of x y and z per second square
    acc_Plot.plot(pos=(time,mag(ball.acc)))
    time = time + dt
    #x speed
    print(ball.pos.x/time)
    scene.center=ball.pos-vector(0,1,0) #keep ball in view
    




#plot graphs


    
file.close()


