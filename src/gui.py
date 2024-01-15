# contains code for gui components

from pyo import *

# visual monitoring
###########################

def scope():
    sc = Scope()   # Displays the waveform of the chosen source
    return sc

def spectrum():
    sp = Spectrum(oscillatorOutput)    # Displays the spectrum contents of the chosen source
    return sp