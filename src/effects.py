# contains code for effects components

from pyo import *

# Panning
###############################

def rightPan():
    rightPan = Pan(input, outs=2, pan=1, spread=0.5, mul=1, add=0)
    return rightPan

def leftPan():
    leftPan = Pan(input, outs=2, pan=0, spread=0.5, mul=1, add=0)
    return leftPan

# Not sure if 0 = left and 1 = right panning

