# Performs analysis

import numpy as np

# PARAMETERS
data_pgc = np.zeros((4, 2, 3, 3))
data_mc = np.zeros((4, 2, 3, 3))
strengths = [0.315, 0.54]
frequencies = [2, 10, 40]

# ANALYSIS
for i in range(1, 5):
	for l,j in enumerate(strengths):
		for m,k in enumerate(frequencies):
			suffix = "_circuit"+str(i)+"_c"+str(j)+"_hz"+str(k)
			latency_pgc = np.load("PGC_First_spike_latency"+suffix+".npy")
			spiketimes_pgc = np.load( "PGC_Spiketimes"+suffix+".npy")
			intraburst_freq_pgc = np.load( "PGC_Interspike_frequencies"+suffix+".npy")


			# Storing the latency
			data_pgc[i-1,l,m,0] = latency_pgc
			
			# Storing the firing rate
			numspikes_pgc = len(spiketimes_pgc)
			t = 6000/1000
			firing_rate_pgc = numspikes_pgc/t
			data_pgc[i-1,l,m,1] = firing_rate_pgc

			# Storing the mean intraburst frequency within bursts
			if len(intraburst_freq_pgc) == 0:
				meanibfreq_pgc = data_pgc[i-1,l,m,2]
			else:
				meanibfreq_pgc = np.mean(intraburst_freq_pgc)
				data_pgc[i-1,l,m,2] = meanibfreq_pgc


			latency_mc = np.load("MC_First_spike_latency"+suffix+".npy")
			spiketimes_mc = np.load( "MC_Spiketimes"+suffix+".npy")
			intraburst_freq_mc = np.load( "MC_Interspike_frequencies"+suffix+".npy")

			# Storing the latency
			data_mc[i-1,l,m,0] = latency_mc
			
			# Storing the firing rate
			numspikes_mc = len(spiketimes_mc)
			t = 6000/1000
			firing_rate_mc = numspikes_mc/t
			data_mc[i-1,l,m,1] = firing_rate_mc

			# Storing the mean intraburst frequency within bursts
			if len(intraburst_freq_mc) == 0:
				meanibfreq_mc = data_mc[i-1,l,m,2]
			else:
				meanibfreq_mc = np.mean(intraburst_freq_mc)
				data_mc[i-1,l,m,2] = meanibfreq_mc



# SAVE
np.save("feature_data_PGC.npy",data_pgc)
np.save("feature_data_MC.npy",data_mc)



