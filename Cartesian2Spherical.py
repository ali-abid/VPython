# Cartesian to Sperical Conversion
# Version 1.0 (March. 2, 2015)
# Abid Ali
#IMaR Gateway Technology, Institute of Technology

from __future__ import print_function, division
from visual import *
import numpy as np
import math as m
import csv
from visual.graph import *

sphericalGraph = display(title = "Cartesian to Spherical Conversion", x=0, y=0, width=450, height=500, forward=(-1,-1,-1), up=(0,1,0))

                 
#Vector scale 
vscale = 0.1
#initial time and time interval
t= 0
deltaT = 0.07

# Reading x y z coordinates from csv file
file = open('C:\Dev\workspace\VPython/xyz36round.csv')
reader = csv.reader(file)
#reading x y z values from csv file
Xnum = []
Ynum = []
Znum = []
# storing x y and z values into arrays
for line in reader:
    Xnum.append(line[1]),Ynum.append(line[2]),Znum.append(line[3])


# X Y Z Labels

rho = 3
xAxis = arrow(pos = (0,0,0), axis = (1,0,0), color = (1,0,0), length = rho + 1, shaftwidth = 0.1, fixedwidth = True)
yAxis = arrow(pos = (0,0,0), axis = (0,1,0), color = (0,1,0), length = rho + 1, shaftwidth = 0.1, fixedwidth = True)
zAxis = arrow(pos = (0,0,0), axis = (0,0,1), color = (0,0,1), length = rho + 1, shaftwidth = 0.1, fixedwidth = True)
xLabel = label(pos = (rho,0,0), text = "X", box = False, color = color.red)
yLabel = label(pos = (0,rho,0), text = "Y", box = False, color = color.green)
zLabel = label(pos = (0,0,rho), text = "Z", box = False, color = color.cyan)



#Convert Cartesian to Spherical
x = 0
y = 0
z = 0
def cart2sph(x,y,z):
    x = float(x)
    y = float(y)
    z = float(z)
    XsqPlusYsq = x**2 + y**2
    r = m.sqrt(XsqPlusYsq + z**2)#r
    elev = m.atan2(z,m.sqrt(r))#phi
    az = m.atan2(y,x)#theta
    return r, elev, az


#Create ball sphere
ball2 = sphere(pos = vector(0,0,0), radius = 0.3, color=color.blue)
#Creae ball trail
ball2.trail = curve(color=ball2.color)
#Create vector arrow
r = arrow(pos=vector(0,0,0), axis = vector(0,0,0), color=color.white, shaftwidth=0.1)


#Update XYZ coordinates and convert into Spherical rho, theta , phi
def updateXYZ(x,y,z):
    ball2.pos = vector(cart2sph(x,y,z))
    #Draw trail along ball movement
    ball2.trail.append(pos=ball2.pos)
    

### MAIN LOOP ###
#updating x y z value and moving position rho theta and phi
for i in range(len(Xnum)-1):
    #rate(50)
    updateXYZ(Xnum[i],Ynum[i],Znum[i])

b1color=color.blue   
BW=0
if BW==0:
    fgcolor=color.black; bgcolor=color.white
else:
    fgcolor=color.white; bgcolor=color.black
    
posx_graph = gdisplay(x=0, y=000, width=500, height=300, 
             title='x-Position vs. Time', xtitle='t(s)', ytitle='x (m)', 
             xmax=100, xmin=0., ymax=50, ymin=0, 
             foreground=fgcolor, background=bgcolor)


#Reading values from Xnum[], Ynum[], Znum[] arrays and move ball positions  
for i in range(len(Xnum)-1):
    rate(100)
    x = Xnum[i]
    ball2.velocity = vector(float(Xnum[i]),float(Ynum[i]),float(Znum[i]))*vscale
    ball2.pos += ball2.pos + ball2.velocity*deltaT
    print(i, ball2.pos.x)
    posx_Plot = gcurve(color=b1color)
    posx_Plot.plot(pos=(t,ball2.x))
    scene.center=ball2.pos #keep block in view
    t = t + deltaT # final time is equal to initial time plus delta time.
        

f1 = gcurve(color=color.cyan)	# a graphics curve
#for x in arange(0, 8.05, 0.1):	# x goes from 0 to 8
f1.plot(pos=(100,30))# plot
    
file.close()
