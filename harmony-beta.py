##################################################################
# Harmony-Beta
#
# Harmony-Beta is a prototype synth built in python using pyo api
#
# © Toneau Audio 2024
##################################################################

from pyo import *

# Creates and boots the server.
# The user should send the "start" command from the GUI.
s = Server().boot()
# Drops the gain by 20 dB.
s.amp = 0.1

# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.
a = Sine().out()

# I/O Devices
###########################

print("List of found devices: \n")
pm_list_devices()   # prints a list of all devices found by portmidi

inputDevices = pm_get_input_devices()  # returns midi input devices found by portmidi
print("Input Devices: \n")
print(inputDevices)

outputDevices = pm_get_output_devices() # returns midi output devices found by portmidi
print("\nOutput Devices: \n")
print(outputDevices)

# GUI Output
###########################

sc = Scope(a)   # Displays the waveform of the chosen source

sp = Spectrum(a)    # Displays the spectrum contents of the chosen source

s.gui(locals())     # Opens the server graphical interface.

