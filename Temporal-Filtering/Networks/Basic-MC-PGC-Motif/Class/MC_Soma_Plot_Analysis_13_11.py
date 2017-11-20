# File which plots the MC Soma analysis

import matplotlib.pyplot as plt
import numpy as np

# LOAD ANALYSIS
y = np.load("feature_data_MC.npy")

# PARAMETERS
x = [0.27,0.315,0.36,0.405,0.45,0.495,0.6]

# PLOTTING
# Plots for latencies
for i in range(1):
	latencies_1 = y[3,:,0,0]
	latencies_2= y[3,:,1,0]
	latencies_5 = y[3,:,2,0]
	latencies_10= y[3,:,3,0]
	latencies_20 = y[3,:,4,0]
	latencies_30= y[3,:,5,0]
	latencies_40= y[3,:,6,0]


	fig = plt.figure(figsize = (35, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, latencies_1,'-*', label = "1Hz")
	ax.plot(x, latencies_2, '-*', label = "2Hz")
	ax.plot(x, latencies_5,'-*', label = "5Hz")
	ax.plot(x, latencies_10, '-*', label = "10Hz")
	ax.plot(x, latencies_20,'-*', label = "20Hz")
	ax.plot(x, latencies_30, '-*', label = "30Hz")
	ax.plot(x, latencies_40, '-*', label = "40Hz")
	plt.xlim((0.265 ,0.605))

	# Labels and Legend
	plt.title("MC Soma Latencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Latency (ms)", fontsize = 30)
	plt.xlabel("Strength (nA)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	plt.savefig("Figures/MC_Soma_latencies_vs_strength_circuit_4.eps",dpi=600)


# Show plots
plt.show()


