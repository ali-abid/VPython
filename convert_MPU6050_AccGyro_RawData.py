# Convert MPU6050 accelerometer and gyroscope raw data into meaning full data.
# And data stored into txt format, this file read by Processing software for visualize 
# accelerometer and gyroscope movements. 
#
# Version 1.0 (March, 2015)
# Abid Ali
#IMaR Technology Gateway, Institute of Technology

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

#DECLARE ARRAYS
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

#DECLARE GLOBAL VARIABLES, FOR HOLDING ROTATION ANGLE OF SENSOR (ACC & GYRO)
last_read_time = 0
last_x_angle = 0                            #These are the filtered angles
last_y_angle = 0
last_z_angle = 0  
last_gyro_x_angle = 0                       #Store the gyro angles to compare drift
last_gyro_y_angle = 0
last_gyro_z_angle = 0
base_x_accel = 0                            #Calibrate acceleration sensor
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


#DEFINE CALIBRATION METHOD
#First 10 reading to compute the default sensor offset.
#The offset get subtracted from raw data sensor values before the values are converted to angles.
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
    print(base_x_accel,base_y_accel,base_z_accel,base_x_gyro,base_y_gyro,base_z_gyro)
    print("Finishing Calibration")



#READ RAW DATA FILE AND STORE INTO ARRAYS (Tnum, Xnum, Ynum, Znum, GXnum, GYnum, GZnum)
RawDataFile = 'C:\Dev\workspace\VPython/golf-1-11-4.txt'
file = open(RawDataFile, 'rU')
reader = csv.reader(file)
for line in reader:
    reader.next() # This function make space in line
    Tnum.append(line[0]),Xnum.append(line[1]),Ynum.append(line[2]),Znum.append(line[3]),GXnum.append(line[4]),GYnum.append(line[5]),GZnum.append(line[6])
    #Set total length of arrays
    accel_angle_x_data.append(line[0])
    accel_angle_y_data.append(line[0])
    accel_angle_z_data.append(line[0])
    unfiltered_gyro_angle_x_data.append(line[0])
    unfiltered_gyro_angle_y_data.append(line[0])
    unfiltered_gyro_angle_z_data.append(line[0])
    angle_x_data.append(line[0])
    angle_y_data.append(line[0])
    angle_z_data.append(line[0])

#CONVERT RADIAN TO DEGREES
PI = math.pi
DEG = 180/PI

#CONVERT RAW DATA ACCORDING TO MPU6050 DATA SHEET AND COMBINE ACC & GYRO DATA
def convertAccelGyro(dt, x,y,z,Gx,Gy,Gz):
    #Delta Time
    t_now = float(Tnum[i]);
    last_time = float(Tnum[i-1]);
    dt =((t_now - last_time)+3)/100.0; # 40ms
    #print("Sampling rate: ",dt)
    
    #Default Gyro at 250 degrees/second
    # Output scale is 32786/250 = 131
    #Convert gyro values to degrees/sec
    FS_SEL = 131
    cgx = float(Gx);
    gyro_x = (cgx-base_x_gyro-base_x_gyro)/FS_SEL
    cgy = float(Gy)
    gyro_y = (cgy-base_y_gyro-base_y_gyro)/FS_SEL;
    cgz = float(Gz)
    gyro_z = (cgz-base_z_gyro-base_z_gyro)/FS_SEL;
    #print("Gyro x raw value: ",cgx, "Default base gyro x value: ", base_x_gyro )
    #print("Convert raw gyro line ",i," to Deg/sec. Gyro x: ",gyro_x)

    #Get raw values
    #float G_CONVERT = 16384;
    accel_x = float(x)
    accel_y = float(y)
    accel_z = float(z)
    #print("Accelerometer x: ", accel_x, "y: ", accel_y, "z: ", accel_z, " default +/- 2g");
    
    #Get angle values from accelerometer
    accel_angle_y = atan(-1*accel_x/sqrt(pow(accel_y,2) + pow(accel_z,2)))* DEG;
    accel_angle_x = atan(accel_y/sqrt(pow(accel_x,2) + pow(accel_z,2)))* DEG;
    accel_angle_z = 0
    #print("Accel Angle x: ", accel_angle_x, "y: ", accel_angle_y, "z: ", accel_angle_z)
    
    #Store data into arrays for output
    accel_angle_x_data[i] = accel_angle_x
    accel_angle_y_data[i] = accel_angle_y
    accel_angle_z_data[i] = accel_angle_z
    
    #Compute the (filtered) gyro angles
    gyro_angle_x = gyro_x*dt + get_last_x_angle();
    gyro_angle_y = gyro_y*dt + get_last_y_angle();
    gyro_angle_z = gyro_z*dt + get_last_z_angle();
    print("Gyro Angle z : ", gyro_angle_z)
    #print("Delta t",dt,"Gyro z data:",gyro_z, "Last x angle", get_last_z_angle(), "Filtered Gyro Angle: ",gyro_angle_z)
    #print("Delata T:", dt)
    #print("Filtered Gyro Aanles: gyro x: ",gyro_angle_x, "gyro y: ", gyro_angle_y, "gyro z", gyro_angle_z )
    
    #Compute the drifting gyro angles
    unfiltered_gyro_angle_x = gyro_x*dt + get_last_gyro_x_angle();
    unfiltered_gyro_angle_y = gyro_y*dt + get_last_gyro_y_angle();
    unfiltered_gyro_angle_z = gyro_z*dt + get_last_gyro_z_angle();

    unfiltered_gyro_angle_x_data[i] = unfiltered_gyro_angle_x
    unfiltered_gyro_angle_y_data[i] = unfiltered_gyro_angle_y
    unfiltered_gyro_angle_z_data[i] = unfiltered_gyro_angle_z
    #print("Delata T:", dt)
    #print("Unfiltered Gyro Aanles: gyro x: ",unfiltered_gyro_angle_x, "gyro y: ", unfiltered_gyro_angle_y, "gyro z", unfiltered_gyro_angle_z )

    
    #Apply the complementary filter to figure out the change in angle - choice of alpha is
    #estimated now.  Alpha depends on the sampling rate...
    alpha = 0.96;
    angle_x = alpha*gyro_angle_x + (1.0 - alpha)*accel_angle_x;
    angle_y = alpha*gyro_angle_y + (1.0 - alpha)*accel_angle_y;
    angle_z = gyro_angle_z;     #Accelerometer doesn't give z-angle
    print("Complementary Filter Angle x: ",angle_x, "y: ",angle_y, "z: ",angle_z )
    
    angle_x_data[i] = angle_x
    angle_y_data[i] = angle_y
    angle_z_data[i] = angle_z
    
    #Update the saved data with the latest values
    set_last_read_angle_data(t_now, angle_x, angle_y, angle_z, unfiltered_gyro_angle_x, unfiltered_gyro_angle_y, unfiltered_gyro_angle_z);


#CALL METHOD
for i in range(len(Xnum)-1):
    if(i == 0 ):
        print("\nCablibrate Sensor : ", i+1, " time.\n")
        #Initialize the angles, for calibration sensor should be motionless on horizantal surface
        #read that motionless file
        calibrate_sensors(Xnum[i],Ynum[i],Znum[i],GXnum[i],GYnum[i],GZnum[i])
        #Reset Variable
        set_last_read_angle_data(Tnum[i], 0, 0, 0, 0, 0, 0);
    else:
        convertAccelGyro(Tnum[i], Xnum[i],Ynum[i],Znum[i],GXnum[i],GYnum[i],GZnum[i])


#SAVE PROCESSED DATA INTO TARGET LOCAITON 
fd = save_file()
if fd:
    fd.write("t,x,y,z,Gx,Gy,Gz,FillX,FillY,FillZ")
    fd.write("\n")
    for i in range(len(accel_angle_x_data)-1):
        t_now = float(Tnum[i]);
        last_time = float(Tnum[i-1]);
        dt =((t_now - last_time)+3)/100.0; # 40ms
        fd.write(str(dt))
        fd.write(",\t")
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
