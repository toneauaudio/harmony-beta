# contains code for oscillator components

from pyo import *

def whiteNoise():
    return Noise()



"""
def noiseGen():

    n1 = Noise(0.3)
    n2 = PinkNoise(0.3)
    n3 = BrownNoise(0.3)

    sel = Selector([n1, n2, n3]).out()
    sel.ctrl(title = "Input interpolator (0 = White, 1 = Pink, 2 = Brown)")
"""