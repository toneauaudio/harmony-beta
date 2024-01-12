from pyo import *

def Devices():
    device_count = pm_count_devices()   # recieving the count of devices

    if device_count < 1:    # if no devices are found
        print("No Devices Found")
    else:
        print("List of found devices: \n")
        pm_list_devices()   # prints a list of all devices found by portmidi

        inputDevices = pm_get_input_devices()  # returns midi input devices found by portmidi
        print("Input Devices: \n")
        print(inputDevices)

        outputDevices = pm_get_output_devices() # returns midi output devices found by portmidi
        print("\nOutput Devices: \n")
        print(outputDevices)