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
# Creates and boots the server.
# The user should send the "start" command from the GUI.

server = Server().boot()

# Signal Processing
###########################
# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.

signalOutput = Sine().out()

# I/O Devices
###########################

midiUtils.Devices()

# GUI Output
###########################

sc = Scope(signalOutput)   # Displays the waveform of the chosen source

sp = Spectrum(signalOutput)    # Displays the spectrum contents of the chosen source

server.gui(locals())     # Opens the server graphical interface.

