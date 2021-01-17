## Object Detection File

## MEng Mechanical and Electrical Engineering
## EN4604 Individual Project
##Frederik Heda


#Import Necessary Libraries
import os
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import tensorflow as tf
import argparse
import sys

# Set up camera constants
IM_WIDTH = 1280
IM_HEIGHT = 720

#Import Model
