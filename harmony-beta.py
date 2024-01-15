##################################################################
# Harmony-Beta
#
# Harmony-Beta is a prototype synth built in python using pyo api
#
# © Toneau Audio 2024
##################################################################

from pyo import *
from src import midiUtils, oscillators, filters, effects

# Server Initalization
###########################

server = Server().boot()

# Signal Processing
###########################

server.amp = 0.1    # adjusting amplitude to -40 dB

oscillatorOutput = oscillators.bipolarPulse().out(0)    # temp audio output for debugging

filterOutput = filters.lowPassFilter(oscillatorOutput, 1000).out()  # currently debugging

# I/O Devices
###########################

midiUtils.Devices()

# GUI Output
###########################

gui.spectrum(oscillatorOutput)

server.gui(locals())     # Opens the server graphical interface.

