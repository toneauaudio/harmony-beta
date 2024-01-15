# contains code for gui components

from pyo import *

# visual monitoring
###########################

def scope():
    sc = Scope(input, length=0.05, gain=0.67, function=None, wintitle="Scope")   # Displays the waveform of the chosen source
    return sc

def spectrum():
    sp = Spectrum(input, size=1024, wintype=2, function=None, wintitle="Spectrum")    # Displays the spectrum contents of the chosen source
    return sp