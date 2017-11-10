# File which plots the analysis for circuit 4 only

import matplotlib.pyplot as plt
import numpy as np

# LOAD ANALYSIS
y_pgc = np.load("feature_data_PGC.npy")
y_mc = np.load("feature_data_MC.npy")

# PARAMETERS
x = [2,10,40]


savefig = 1
showfig = 1


latencies_mc_315 = np.zeros((4,3))
latencies_mc_54  = np.zeros((4,3))

fig = plt.figure(figsize = (25, 25))
ax = fig.add_subplot(111)
for i in range(4):
	if i == 3:
		latencies_mc_315[i] = y_mc[i,0,:,0]
		latencies_mc_54[i]  = y_mc[i,1,:,0]



		ax.plot(x, latencies_mc_315[i], '-*',color=(0.1,0.2,0.5,i*0.1+0.4),linewidth=2.0,label='0.315nA')
		ax.plot(x, latencies_mc_54[i],'-*',color=(0.5,0.2,0.1,i*0.1+0.4),linewidth=2.0,label='0.54nA')
plt.xlim((0 ,41))

# Labels and Legend
plt.title("MC Latencies Circuit 4", fontsize = 34)
ax.title.set_position([0.5, 1.03])
plt.ylabel("Latency (ms)", fontsize = 30)
plt.xlabel("Frequency (Hz)", fontsize = 30)
plt.xticks(fontsize = 28)
plt.yticks(fontsize = 28)
ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 14)
#ax.legend()


# Save
if savefig:
	plt.savefig("MC_latencies_C4.eps",dpi=600)
	plt.savefig("MC_latencies_C4.pdf",dpi=600)
	#plt.savefig("MC_latencies_C4.png",dpi=300) 



firing_rate_mc_315 = np.zeros((4,3))
firing_rate_mc_54  = np.zeros((4,3))

fig = plt.figure(figsize = (25, 25))
ax = fig.add_subplot(111)
for i in range(4):
	if i == 3:
		firing_rate_mc_315[i] = y_mc[i,0,:,1]
		firing_rate_mc_54[i]  = y_mc[i,1,:,1]



		ax.plot(x, firing_rate_mc_315[i], '-*',color=(0.1,0.2,0.5,i*0.1+0.4),linewidth=2.0,label='0.315nA')
		ax.plot(x, firing_rate_mc_54[i],'-*',color=(0.5,0.2,0.1,i*0.1+0.4),linewidth=2.0,label='0.54nA')
plt.xlim((0 ,41))

# Labels and Legend
plt.title("MC Firing Rates Circuit 4", fontsize = 34)
ax.title.set_position([0.5, 1.03])
plt.ylabel("Firing Rate (Hz)", fontsize = 30)
plt.xlabel("Frequency (Hz)", fontsize = 30)
plt.xticks(fontsize = 28)
plt.yticks(fontsize = 28)
ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 14)
#ax.legend()


# Save
if savefig:
	plt.savefig("MC_firing_rate_C4.eps",dpi=600)
	plt.savefig("MC_firing_rate_C4.pdf",dpi=600)
	#plt.savefig("MC_firing_rate_C4.png",dpi=300) 


'''
# PLOTTING
# Plots for latencies
for i in range(4):

	latencies_pgc_315= y_pgc[i,0,:,0]
	latencies_pgc_54 = y_pgc[i,1,:,0]



	fig = plt.figure(figsize = (45, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, latencies_pgc_315, '-*', label = "0.315nA")
	ax.plot(x, latencies_pgc_54,'-*', label = "0.54nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("PGC Latencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Latency (ms)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	if savefig:
		plt.savefig("PGC_latencies_circuit_"+str(i+1)+".eps",dpi=600)
		#plt.savefig("PGC_latencies_circuit_"+str(i+1)+".png",dpi=300) 


	latencies_mc_315= y_mc[i,0,:,0]
	latencies_mc_54 = y_mc[i,1,:,0]



	fig = plt.figure(figsize = (45, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, latencies_mc_315, '-*', label = "0.315nA")
	ax.plot(x, latencies_mc_54,'-*', label = "0.54nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("MC Latencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Latency (ms)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	if savefig:
		plt.savefig("MC_latencies_circuit_"+str(i+1)+".eps",dpi=600)
		#plt.savefig("MC_latencies_circuit_"+str(i+1)+".png",dpi=300) 

# Plot for firing rate
for i in range(4):

	firing_rate_pgc_315 = y_pgc[i,0,:,1]
	firing_rate_pgc_54  = y_pgc[i,1,:,1]


	fig = plt.figure(figsize = (45, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, firing_rate_pgc_315, '-*', label = "0.315nA")
	ax.plot(x, firing_rate_pgc_54, '-*', label = "0.54nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("PGC Firing Rates", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Firing Rate (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)
	
	# Save
	if savefig:
		plt.savefig("PGC_firing_rate_circuit_"+str(i+1)+".eps",dpi=600)
		#plt.savefig("PGC_firing_rate_circuit_"+str(i+1)+".png",dpi=300) 

	firing_rate_mc_315 = y_mc[i,0,:,1]
	firing_rate_mc_54  = y_mc[i,1,:,1]


	fig = plt.figure(figsize = (45, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, firing_rate_mc_315, '-*', label = "0.315nA")
	ax.plot(x, firing_rate_mc_54, '-*', label = "0.54nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("MC Firing Rates", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Firing Rate (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)
	
	# Save
	if savefig:
		plt.savefig("MC_firing_rate_circuit_"+str(i+1)+".eps",dpi=600)
		#plt.savefig("MC_firing_rate_circuit_"+str(i+1)+".png",dpi=300) 

# Plot for the means of intraburst frequencies within bursts
for i in range(4):
	mibfrequencies_pgc_315 = y_pgc[i,0,:,2]
	mibfrequencies_pgc_54  = y_pgc[i,0,:,2]


	fig = plt.figure(figsize = (35, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, mibfrequencies_pgc_315, '-*', label = "0.315nA")
	ax.plot(x, mibfrequencies_pgc_54, '-*', label = "0.54nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("PGC Mean Intraburst Frequencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Mean Intraburst Frequency (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	if savefig:
		plt.savefig("PGC_mibfrequencies_circuit_"+str(i+1)+".eps",dpi=600)
		#plt.savefig("PGC_mibfrequencies_circuit_"+str(i+1)+".png",dpi=300) 

	mibfrequencies_mc_315 = y_mc[i,0,:,2]
	mibfrequencies_mc_54  = y_mc[i,0,:,2]


	fig = plt.figure(figsize = (35, 25))
	ax = fig.add_subplot(111)
	ax.plot(x, mibfrequencies_mc_315, '-*', label = "0.315nA")
	ax.plot(x, mibfrequencies_mc_54, '-*', label = "0.54nA")
	plt.xlim((0 ,41))

	# Labels and Legend
	plt.title("MC Mean Intraburst Frequencies", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Mean Intraburst Frequency (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 28)
	plt.yticks(fontsize = 28)
	ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5), fontsize = 28)

	# Save
	if savefig:
		plt.savefig("MC_mibfrequencies_circuit_"+str(i+1)+".eps",dpi=600)
		#plt.savefig("MC_mibfrequencies_circuit_"+str(i+1)+".png",dpi=300)
'''
# Show plots
if showfig:
	plt.show()


