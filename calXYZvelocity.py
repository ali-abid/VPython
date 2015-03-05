import csv
from visual import *
scene.background = color.white
scene.width = 400
scene.height = 400
scene.forward = vector(-.5,-.3,-1)
file = open('C:\Dev\Python27\workspace/xyz30round3direction.csv')
reader = csv.reader(file)
G = 6.7e-11

#Coordinated x y z stored in array from .csv file
x = []
y = []
z= []
#Velocity stored in arrays vX vY vZ
vX = []
vY = []
vZ = []
deltaX = []
deltaY = []
deltaZ = []
vscale = 0.1
t= 0
deltaT = 0.07

ball2 = sphere(pos = vector(0,0,0), radius = 0.1, color=color.blue)
ball2.trail = curve(color=ball2.color)
for line in reader:
    x.append(line[1]),y.append(line[2]),z.append(line[3])



 #Label x y and z coordinates
xaxis=cylinder(color=color.red, pos=vector(0,0,0), axis=vector(2,0,0), radius=0.2)
xlbl=label(pos=vector(3,0,0), text="X", color=color.red, opacity=0, height=30, box=0)
yaxis=cylinder(color=color.green, pos=(0,0,0), axis=(0,2,0), radius=0.2)
ylbl=label(pos=vector(0,3,0), text="Y", color=color.green, opacity=0, height=30, box=0)
zaxis=cylinder(color=color.blue, pos=(0,0,0), axis=(0,0,2), radius=0.2)
xlbl=label(pos=vector(0,0,3), text="Z", color=color.blue, opacity=0, height=30, box=0)

r = arrow(pos=vector(0,0,0), axis = vector(0,0,0), color=color.white, shaftwidth=0.1)

#Run loop read all index values from arrys  
for i in range(len(x)-1):
    #No more than 10 loop per second
    rate(40)
    #Reade ball velocity from vX, vY and vZ arrays
    ball2.velocity = vector(float(x[i]),float(y[i]),float(z[i]))*vscale
    #Draw arrow along ball velocity
    r.pos= ball2.velocity*vscale
    r.axis = ball2.pos
    ra = arrow(pos= ball2.pos, axis = ball2.velocity*vscale, color=color.yellow)
    #Update ball position 
    ball2.pos = ball2.pos + ball2.velocity*deltaT
    #Draw trail along ball movement
    ball2.trail.append(pos=ball2.pos)
    print(ball2.velocity)




    

    
#file close
file.close()
