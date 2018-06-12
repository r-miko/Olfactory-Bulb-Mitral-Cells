# File which plots the MC Soma analysis

import matplotlib.pyplot as plt
import numpy as np

# LOAD ANALYSIS
y = np.load("feature_data_MC.npy")

# PARAMETERS
x = [1,2,5,10,20, 30, 40]

# PLOTTING
# Plots for latencies
for i in range(4):
	latencies_27 = y[i,0,:,0]
	latencies_315= y[i,1,:,0]
	latencies_36 = y[i,2,:,0]
	latencies_405= y[i,3,:,0]
	latencies_45 = y[i,4,:,0]
	latencies_495= y[i,5,:,0]
	latencies_6= y[i,6,:,0]


	fig = plt.figure(figsize = (35, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, latencies_27,'-*', label = "0.27nA")
	ax.plot(x, latencies_315, '-*', label = "0.315nA")
	ax.plot(x, latencies_36,'-*', label = "0.36nA")
	ax.plot(x, latencies_405, '-*', label = "0.405nA")
	ax.plot(x, latencies_45,'-*', label = "0.45nA")
	ax.plot(x, latencies_495, '-*', label = "0.495nA")
	ax.plot(x, latencies_6, '-*', label = "0.6nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("MC Soma Latencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Latency (ms)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	plt.savefig("Figures/MC_Soma_latencies_circuit_"+str(i+1)+".eps",dpi=600)
	plt.savefig("Figures/MC_Soma_latencies_circuit_"+str(i+1)+".png",dpi=300) 

# Plot for firing rate
for i in range(4):
	firing_rate_27 = y[i,0,:,1]
	firing_rate_315 = y[i,1,:,1]
	firing_rate_36 = y[i,2,:,1]
	firing_rate_405 = y[i,3,:,1]
	firing_rate_45 = y[i,4,:,1]
	firing_rate_495 = y[i,5,:,1]
	firing_rate_6 = y[i,6,:,1]

	fig = plt.figure(figsize = (35, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, firing_rate_27,'-*', label = "0.27nA")
	ax.plot(x, firing_rate_315, '-*', label = "0.315nA")
	ax.plot(x, firing_rate_36,'-*', label = "0.36nA")
	ax.plot(x, firing_rate_405, '-*', label = "0.405nA")
	ax.plot(x, firing_rate_45,'-*', label = "0.45nA")
	ax.plot(x, firing_rate_495, '-*', label = "0.495nA")
	ax.plot(x, firing_rate_6, '-*', label = "0.6nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("MC Soma Firing Rates", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Firing Rate (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)
	
	# Save
	plt.savefig("Figures/MC_Soma_firing_rate_circuit_"+str(i+1)+".eps",dpi=600)
	plt.savefig("Figures/MC_Soma_firing_rate_circuit_"+str(i+1)+".png",dpi=300) 

# Plot for the means of intraburst frequencies within bursts
for i in range(4):
	mibfrequencies_27 = y[i,0,:,2]
	mibfrequencies_315 = y[i,1,:,2]
	mibfrequencies_36 = y[i,2,:,2]
	mibfrequencies_405 = y[i,3,:,2]
	mibfrequencies_45 = y[i,4,:,2]
	mibfrequencies_495 = y[i,5,:,2]
	mibfrequencies_6 = y[i,6,:,2]

	fig = plt.figure(figsize = (35, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, mibfrequencies_27,'-*', label = "0.27nA")
	ax.plot(x, mibfrequencies_315, '-*', label = "0.315nA")
	ax.plot(x, mibfrequencies_36,'-*', label = "0.36nA")
	ax.plot(x, mibfrequencies_405, '-*', label = "0.405nA")
	ax.plot(x, mibfrequencies_45,'-*', label = "0.45nA")
	ax.plot(x, mibfrequencies_495, '-*', label = "0.495nA")
	ax.plot(x, mibfrequencies_6, '-*', label = "0.6nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("MC Soma Mean Intraburst Frequencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Mean Intraburst Frequency (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	plt.savefig("Figures/MC_Soma_mibfrequencies_circuit_"+str(i+1)+".eps",dpi=600)
	plt.savefig("Figures/MC_Soma_mibfrequencies_circuit_"+str(i+1)+".png",dpi=300) 

# Show plots
#plt.show()


