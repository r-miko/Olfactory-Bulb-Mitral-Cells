# File which simply loads the results from a single run and prints them

import matplotlib.pyplot as plt
import numpy as np

# LOAD ANALYSIS
directory = 'Test/'
spiketimes = np.load(directory+"MC_Spiketimes.npy")
latency = np.load(directory+"MC_First_spike_latency.npy")


print len(spiketimes)/6.0 # 6.0s stimulation 
print '\n'
print latency
