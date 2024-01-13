# contains code for filter components

from pyo import *

# Filters
##############################

def lowPassFilter(input_signal, cutoff_frequency):  # applies a simple lowpass filter to the input signal.

"""
Args:
    input_signal (Sig): The input signal to be filtered.
    cutoff_frequency (Sig): The cutoff frequency of the filter.

Returns:
    Sig: The filtered output signal.

------------------------------------

# Example usage:
s = Server().boot()

n = Noise(0.5)
freq = Sig(1000)
freq.ctrl([SLMap(50, 5000, "lin", "value", 1000)], title="Cutoff Frequency")

filtered_signal = simple_lowpass_filter(n, freq)

filtered_signal.out()

s.gui(locals())
"""

    filterType = "Tone"
    filterObj = locals()[filterType](input_signal, cutoff_frequency)
    return filterObj


