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



