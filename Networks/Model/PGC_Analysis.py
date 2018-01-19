# Performs analysis on the PGC output results

import numpy as np

# PARAMETERS
data = np.zeros((4, 7, 7, 3))
strengths = [0.27, 0.315, 0.36, 0.405, 0.45, 0.495, 0.6]
frequencies = [1, 2, 5, 10, 20, 30, 40]

# ANALYSIS
for i in range(1, 5):
	a = "Circuit_"+str(i) + "/"
	for l,j in enumerate(strengths):
		b = "c"+str(j) + "/"
		for m,k in enumerate(frequencies):
			c = str(k) + "/"
			latency = np.load(a + b + c + "PGC_First_spike_latency.npy")
			spiketimes = np.load(a + b + c + "PGC_Spiketimes.npy")
			intraburst_freq = np.load(a + b + c + "PGC_Interspike_frequencies.npy")

			# Storing the latency
			data[i-1,l,m,0] = latency
			
			# Storing the firing rate
			numspikes = len(spiketimes)
			t = 6000/1000
			firing_rate = numspikes/t
			data[i-1,l,m,1] = firing_rate

			# Storing the mean intraburst frequency within bursts
			if len(intraburst_freq) == 0:
				meanibfreq = data[i-1,l,m,2]
			else:
				meanibfreq = np.mean(intraburst_freq)
				data[i-1,l,m,2] = meanibfreq

# SAVE
#np.save("feature_data_PGC.npy",data)
