##################################################################
# Harmony-Beta
#
# Harmony-Beta is a prototype synth built in python using pyo api
#
# © Toneau Audio 2024
##################################################################

from pyo import *
import midiUtils

# Server Initalization
###########################

server = Server().boot()

# Signal Processing
###########################

server.amp = 0.1    # adjusting amplitude to -40 dB

signalOutput = Sine().out()

# I/O Devices
###########################

midiUtils.Devices()

# GUI Output
###########################

# sc = Scope(signalOutput)   # Displays the waveform of the chosen source

# sp = Spectrum(signalOutput)    # Displays the spectrum contents of the chosen source

server.gui(locals())     # Opens the server graphical interface.

