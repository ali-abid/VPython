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

