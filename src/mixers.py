# contains code for mixer components

from pyo import *

# Fader
#############################

def fader():
    fader = Fader(fadein=0.01, fadeout=0.1, dur=0, mul=1, add=0)
    return fader

