# File which calculates simple classifier

import matplotlib.pyplot as plt
import numpy as np

# LOAD ANALYSIS
y = np.load("feature_data_MC.npy")

strengths = [0.27,0.315,0.36,0.405,0.45,0.495,0.6]
frequencies = [1, 2, 5, 10, 20, 30, 40]

# Only looking at circuit 4!

# Calculate mean firing rates over frequencies for each strength
mean_firing_rates = np.zeros((7,))
std_firing_rates = np.zeros((7,))
for i in range(7):
	mean_firing_rates[i] = np.mean(y[3,i,:,1])
	std_firing_rates[i] = np.std(y[3,i,:,1])

# fit line
pFR = np.polyfit(strengths,mean_firing_rates,deg=1)
print pFR[0],pFR[1]

# Calculate mean latency over strengths for each frequency
mean_latencies = np.zeros((7,))
std_latencies = np.zeros((7,))
for i in range(7):
	mean_latencies[i] = np.mean(y[3,:,i,0])
	std_latencies[i] = np.std(y[3,:,i,0])

pL = np.polyfit(frequencies,mean_latencies,deg=1)
print pL[0],pL[1]

fig = plt.figure(figsize=(20,20))
ax=fig.add_subplot(111)
ax.errorbar(strengths,mean_firing_rates,yerr=std_firing_rates,linewidth=2.0)

fig = plt.figure(figsize=(20,20))
ax=fig.add_subplot(111)
ax.errorbar(frequencies,mean_latencies,yerr=std_latencies,linewidth=2.0)

plt.show()
