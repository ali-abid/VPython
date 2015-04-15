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