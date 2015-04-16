import csv
from visual import *
#Set background graph parameters
scene.background = color.white
scene.width = 400
scene.height = 400
scene.forward = vector(-.5,-.3,-1)
#Reading file
file = open('C:\Dev\Python27\workspace/xyz30round3direction.csv')
reader = csv.reader(file)
#Garavity force
G = 6.7e-11
#Coordinated x y z stored in array from .csv file
x = []
y = []
z= []
#Velocity stored in arrays vX vY vZ
vX = []
vY = []
vZ = []
#Delta velocity stored in arrays
deltaX = []
deltaY = []
deltaZ = []
#Vector scale 
vscale = 0.1
#initial time and time interval
t= 0
deltaT = 0.07

#Reading x y and z coordinates from .csv file
for line in reader:
    x.append(line[1]),y.append(line[2]),z.append(line[3])

#Following three loops calculating x y and z velocity. e.g X velocity = deltaX/deltaY
for i in range(len(x)-1):
    deltax = float(x[i+1]) - float(x[i])#calculate displacement
    x[i+1] = deltax #store delatax as inital point in x[i+1]
    vX.append(deltax/deltaT)# store velocit deltatX/deltaT inside vX[]

for i in range(len(y)-1):
    deltay = float(y[i+1]) - float(y[i]) # substact from y final point to y inital point
    y[i+1] = deltay # Store deltay value as y inial point.
    vY.append(deltay/deltaT)#Store y velocity into vY[]

for i in range(len(z)-1):
    deltaz = float(z[i+1]) - float(z[i])
    z[i+1] = deltaz
    vZ.append(deltaz/deltaT)

#Creating ball sphere
ball2 = sphere(pos = vector(0,0,0), radius = 0.1, color=color.blue)
#Creating ball trail
ball2.trail = curve(color=ball2.color)

#Label x y and z coordinates
xaxis=cylinder(color=color.red, pos=vector(0,0,0), axis=vector(2,0,0), radius=0.2)
xlbl=label(pos=vector(3,0,0), text="X", color=color.red, opacity=0, height=30, box=0)
yaxis=cylinder(color=color.green, pos=(0,0,0), axis=(0,2,0), radius=0.2)
ylbl=label(pos=vector(0,3,0), text="Y", color=color.green, opacity=0, height=30, box=0)
zaxis=cylinder(color=color.blue, pos=(0,0,0), axis=(0,0,2), radius=0.2)
xlbl=label(pos=vector(0,0,3), text="Z", color=color.blue, opacity=0, height=30, box=0)
#Create vector arrow
r = arrow(pos=vector(0,0,0), axis = vector(0,0,0), color=color.white, shaftwidth=0.1)

#Read calculated velocity values from vX[] vY[] vZ[] arrays and move ball positions  
for i in range(len(vX)-1):
    #No more than 10 loop per second
    rate(40)
    #Read ball velocity from vX, vY and vZ arrays
    ball2Velocity = vector(float(x[i]),float(y[i]),float(z[i]))*vscale
    #Draw arrow along ball velocity
    r.pos= ball2Velocity*vscale
    r.axis = ball2.pos
    ra = arrow(pos= ball2.pos, axis = ball2Velocity*vscale, color=color.yellow)
    #Update ball position 
    ball2.pos = ball2.pos + ball2Velocity*deltaT
    #Draw trail along ball movement
    ball2.trail.append(pos=ball2.pos)
    print(ball2Velocity)
#file close
file.close()
