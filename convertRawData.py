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
import time
from visual.filedialog import save_file

PI = math.pi
DEG = 180/PI
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


#Reading x y and z data from file
Tnum = []
Xnum = []
Ynum = []
Znum = []

GXnum = []
GYnum = []
GZnum = []

accel_angle_x_data = []
accel_angle_y_data = []
accel_angle_z_data = []
unfiltered_gyro_angle_x_data = []
unfiltered_gyro_angle_y_data = []
unfiltered_gyro_angle_z_data = []

angle_x_data = []
angle_y_data = []
angle_z_data = []

#DECLARE GLOBAL VARIABLES 
#Use the following global variables and access functions to help store the overall
#rotation angle of the sensor
last_read_time = 0
last_x_angle = 0       #These are the filtered angles
last_y_angle = 0
last_z_angle = 0  
last_gyro_x_angle = 0  #Store the gyro angles to compare drift
last_gyro_y_angle = 0
last_gyro_z_angle = 0

#Use the following global variables and access functions
#to calibrate the acceleration sensor
base_x_accel = 0
base_y_accel = 0
base_z_accel = 0
base_x_gyro = 0
base_y_gyro = 0
base_z_gyro = 0


#DEFINE SETTER METHOD
def set_last_read_angle_data(time,x,y,z,x_gyro,y_gyro,z_gyro): 
  global last_read_time
  last_read_time = time;
  global last_x_angle
  last_x_angle = x;
  global last_y_angle
  last_y_angle = y;
  global last_z_angle
  last_z_angle = z;
  global last_gyro_x_angle
  last_gyro_x_angle = x_gyro;
  global last_gyro_y_angle
  last_gyro_y_angle = y_gyro;
  global last_gyro_z_angle
  last_gyro_z_angle = z_gyro;

#DEFINE GETTER METHOD
def get_last_time():
    return last_read_time
def get_last_x_angle():
    return last_x_angle
def get_last_y_angle():
    return last_y_angle
def get_last_z_angle():
    return last_z_angle
def get_last_gyro_x_angle():
    return last_gyro_x_angle
def get_last_gyro_y_angle():
    return last_gyro_y_angle
def get_last_gyro_z_angle():
    return last_gyro_z_angle



def calibrate_sensors(x,y,z,Gx,Gy,Gz):
    num_readings = 10
    x_accel = 0;
    y_accel = 0;
    z_accel = 0;
    x_gyro = 0;
    y_gyro = 0;
    z_gyro = 0;
    print("Starting Calibration")
    for i in range(num_readings):
        print(i)
        print(Tnum[i],Xnum[i],Ynum[i],Znum[i],GXnum[i],GYnum[i],GZnum[i])
        rate(10)
        x_accel += float(Xnum[i])
        y_accel += float(Ynum[i])
        z_accel += float(Znum[i])
        x_gyro += float(GXnum[i])
        y_gyro += float(GYnum[i])
        z_gyro += float(GZnum[i])

    x_accel /= num_readings
    y_accel /= num_readings
    z_accel /= num_readings
    x_gyro /= num_readings
    y_gyro /= num_readings
    z_gyro /= num_readings

    #Store the raw calibration values globally
    global base_x_accel
    base_x_accel = x_accel
    global base_y_accel
    base_y_accel = y_accel
    global base_z_accel
    base_z_accel = z_accel
    global base_x_gyro
    base_x_gyro = x_gyro
    global base_y_gyro
    base_y_gyro = y_gyro
    global base_z_gyro
    base_z_gyro = z_gyro;
    print("Finishing Calibration")


RawDataFile = 'C:\Dev\workspace\VPython/golf-1-11-4.txt'
file = open(RawDataFile, 'rU')
reader = csv.reader(file)
for line in reader:
    reader.next() # This function make space in line
    Tnum.append(line[0]),Xnum.append(line[1]),Ynum.append(line[2]),Znum.append(line[3]),GXnum.append(line[4]),GYnum.append(line[5]),GZnum.append(line[6])

    #Set length of arrays
    accel_angle_x_data.append(line[0])
    accel_angle_y_data.append(line[0])
    accel_angle_z_data.append(line[0])
    unfiltered_gyro_angle_x_data.append(line[0])
    unfiltered_gyro_angle_y_data.append(line[0])
    unfiltered_gyro_angle_z_data.append(line[0])
    angle_x_data.append(line[0])
    angle_y_data.append(line[0])
    angle_z_data.append(line[0])
    
    #Xnum.append(line[1])
    #print(Xnum[1], Ynum[1])  


#Initialize the angles
#For calibration sensor should be motionless on horizantal surface
#Read that motionless file
calibrate_sensors(Xnum[i],Ynum[i],Znum[i],GXnum[i],GYnum[i],GZnum[i])
set_last_read_angle_data(Tnum[i], 0, 0, 0, 0, 0, 0);


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
             xmax=100, xmin=0., ymax=2, ymin=-2, 
             foreground=fgcolor, background=bgcolor)
vel_Plot = gcurve(color=colory)


#Acceleration graph
acc_graph = gdisplay(x=0, y=400, width=250, height=200, 
             title='Acceleration vs. Time', xtitle='t(s)', ytitle='a (m/s^2)', 
             xmax=100, xmin=0., ymax=2, ymin=-2, 
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
    #print(ball.vel)
    ball.acc = a
    ball.pos += ball.vel*dt
    ball.vel += ball.acc*dt
    vel_Plot.plot(pos=(time,ball.vel.x))
    #velx_Plot.plot(pos=(time,mag(ball.pos)))       #Plot Postion of object
    acc_Plot.plot(pos=(time,mag(ball.acc)))       #Plot Acceleration 

#This method show velocity vector and ball position 
def vectorVelocity(x,y,z):
    ball.vel = vector(float(Xnum[i]),float(Ynum[i]),float(Znum[i]))*vscale
    r = arrow(pos= ball.pos, axis = ball.vel*vscale, color=color.yellow)
    ball.pos = ball.pos + ball.vel*dt     #Update ball position

def convertADCtoDecimal(x,y,z):
    Adcx = float(x)
    Adcy = float(y)
    Adcz = float(z)
    Vx = Adcx * 3.3/65535       #AdcX * RefVoltage/ 2^16 -1
    Vy = Adcy * 3.3/65635
    Vz = Adcz * 3.3/65635
    print(Vx,Vy,Vz)


def convertADCtoDecimalStore(x,y,z):
    VxZeroG = 1.65
    VyZeroG = 1.65
    VzZeroG = 1.65
    Adcx = float(Xnum[i])
    Adcy = float(Ynum[i])
    Adcz = float(Znum[i])
    Vx = Adcx * 3.3/65535       #AdcX * RefVoltage/ 2^16 -1
    Vy = Adcy * 3.3/65635
    Vz = Adcz * 3.3 /65635
    #Delta DVx DVy DVz
    DVx = Vx - VxZeroG/0.10
    VxZeroG = Vx
    DVy = Vy - VyZeroG/0.10
    VxZeroG = Vy
    DVz = Vz - VyZeroG/0.10
    VzZeroG = Vz
    Xnum[i] = DVx
    Ynum[i] = DVy
    Znum[i] = DVz
    print(Xnum[i],Ynum[i],Znum[i]);


#Convert Raw data
def convertAccelGyro(dt, x,y,z,Gx,Gy,Gz):
    #Convert gyro values to degrees/sec
    FS_SEL = 131
    cgx = float(Gx);
    gyro_x = (cgx-base_x_gyro)/FS_SEL
    cgy = float(Gy)
    gyro_y = (cgy-base_y_gyro)/FS_SEL;
    cgz = float(Gz)
    gyro_z = (cgz-base_z_gyro)/FS_SEL;
    
    #Get raw values
    #float G_CONVERT = 16384;
    accel_x = float(x)
    accel_y = float(y)
    accel_z = float(z)

    #Get angle values from accelerometer
    accel_angle_y = atan(-1*accel_x/sqrt(pow(accel_y,2) + pow(accel_z,2)))* DEG;
    accel_angle_x = atan(accel_y/sqrt(pow(accel_x,2) + pow(accel_z,2)))* DEG;
    accel_angle_z = 0

    #Store data into arrays for output
    accel_angle_x_data[i] = accel_angle_x
    accel_angle_y_data[i] = accel_angle_y
    accel_angle_z_data[i] = accel_angle_z
    
    #Compute the (filtered) gyro angles
    t_now = float(Tnum[i]);
    last_time = float(Tnum[i-1]);
    dt =(t_now - last_time)/1000.0;
    gyro_angle_x = gyro_x*dt + get_last_x_angle();
    gyro_angle_y = gyro_y*dt + get_last_y_angle();
    gyro_angle_z = gyro_z*dt + get_last_z_angle();

    #Compute the drifting gyro angles
    unfiltered_gyro_angle_x = gyro_x*dt + get_last_gyro_x_angle();
    unfiltered_gyro_angle_y = gyro_y*dt + get_last_gyro_y_angle();
    unfiltered_gyro_angle_z = gyro_z*dt + get_last_gyro_z_angle();

    unfiltered_gyro_angle_x_data[i] = unfiltered_gyro_angle_x
    unfiltered_gyro_angle_y_data[i] = unfiltered_gyro_angle_y
    unfiltered_gyro_angle_z_data[i] = unfiltered_gyro_angle_z

    
    #Apply the complementary filter to figure out the change in angle - choice of alpha is
    #estimated now.  Alpha depends on the sampling rate...
    alpha = 0.96;
    angle_x = alpha*gyro_angle_x + (1.0 - alpha)*accel_angle_x;
    angle_y = alpha*gyro_angle_y + (1.0 - alpha)*accel_angle_y;
    angle_z = gyro_angle_z;     #Accelerometer doesn't give z-angle

    angle_x_data[i] = angle_x
    angle_y_data[i] = angle_y
    angle_z_data[i] = angle_z
    
    #Update the saved data with the latest values
    set_last_read_angle_data(t_now, angle_x, angle_y, angle_z, unfiltered_gyro_angle_x, unfiltered_gyro_angle_y, unfiltered_gyro_angle_z);
  
    #print(angle_z)




#Main Loop 
for i in range(len(Xnum)-1):
    rate(100)
# This function calculate velocity and position of x y and z coordinates
    #print("Raw Values:")
    #print("Time: ",time,"X: ", Xnum[i],"Y: ",Ynum[i],"Z: ", Znum[i])
    convertAccelGyro(Tnum[i], Xnum[i],Ynum[i],Znum[i],GXnum[i],GYnum[i],GZnum[i])
    #print(Tnum[i],Xnum[i] = file_output)
    #print(last_read_time)
    #posANDacc(Xnum[i],Ynum[i],Znum[i])      # This will show graph
    #convertADCtoDecimal(Xnum[i],Ynum[i],Znum[i])
    #print("Time: ",Tnum[i],"X: ", Xnum[i],"Y: ",Ynum[i],"Z: ", Znum[i])
    #convertADCtoDecimalStore(Xnum[i],Ynum[i],Znum[i])
    #vectorVelocity(Xnum[i],Ynum[i],Znum[i]) # This will show moving vector direction
    scene.center=ball.pos-vector(0,1,0) #keep ball in view
    time = time + dt

fd = save_file()
if fd:
    for i in range(len(accel_angle_x_data)-1):
        print("Accel x angle: ", angle_z_data[i])
        fd.write(str(accel_angle_x_data[i]))
        fd.write(",\t")
        fd.write(str(accel_angle_y_data[i]))
        fd.write(",\t")
        fd.write(str(accel_angle_z_data[i]))
        fd.write(",\t")
        fd.write(str(unfiltered_gyro_angle_x_data[i]))
        fd.write(",\t")
        fd.write(str(unfiltered_gyro_angle_y_data[i]))
        fd.write(",\t")
        fd.write(str(unfiltered_gyro_angle_z_data[i]))
        fd.write(",\t")
        fd.write(str(angle_x_data[i]))
        fd.write(",\t")
        fd.write(str(angle_y_data[i]))
        fd.write(",\t")
        fd.write(str(angle_z_data[i]))
        fd.write("\n")
        
    fd.close()

file.close()
