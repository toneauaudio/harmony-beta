from pyo import *

def Devices():

    print("List of found devices: \n")
    pm_list_devices()   # prints a list of all devices found by portmidi

    inputDevices = pm_get_input_devices()  # returns midi input devices found by portmidi
    print("Input Devices: \n")
    print(inputDevices)

    outputDevices = pm_get_output_devices() # returns midi output devices found by portmidi
    print("\nOutput Devices: \n")
    print(outputDevices)