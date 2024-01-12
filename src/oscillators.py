# contains code for oscillator components

from pyo import *

# Noise Generators
#################################

def noiseGen():
    def whiteNoise():
        return Noise()      # white noise - flat spectrum
    def pinkNoise():
        return PinkNoise()      # pink noise - 3dB rolloff per octave
    def brownNoise():
        return BrownNoise()     # brown noise - 6dB rolloff per octave

"""
def noiseGen():

    n1 = Noise(0.3)
    n2 = PinkNoise(0.3)
    n3 = BrownNoise(0.3)

    sel = Selector([n1, n2, n3]).out()
    sel.ctrl(title = "Input interpolator (0 = White, 1 = Pink, 2 = Brown)")
"""

# Low Frequency Oscillator
##################################

def sawUp():
    sawUp = LFO(freq=100, sharp=0.5, type=0, mul=1, add=0)  # Saw Up LFO
    return sawUp

def sawDown():
    sawDown = LFO(freq=100, sharp=0.5, type=1, mul=1, add=0)  # Saw Down LFO
    return sawDown

def square():
    square = LFO(freq=100, sharp=0.5, type=2, mul=1, add=0)  # Square LFO
    return square

def triangle():
    triangle = LFO(freq=100, sharp=0.5, type=3, mul=1, add=0)  # Triangle LFO
    return triangle

def pulse():
    pulse = LFO(freq=100, sharp=0.5, type=4, mul=1, add=0)  # Pulse LFO
    return pulse

def bipolarPulse():
    bipolarPulse = LFO(freq=100, sharp=0.5, type=5, mul=1, add=0)  # Bipolar Pulse LFO
    return bipolarPulse

def sampleAndHold():
    sampleAndHold = LFO(freq=100, sharp=0.5, type=6, mul=1, add=0)  # Sample and Hold LFO
    return sampleAndHold

def modulatedSine():
    modulatedSine = LFO(freq=100, sharp=0.5, type=7, mul=1, add=0)  # Modulated Sine LFO
    return modulatedSine

