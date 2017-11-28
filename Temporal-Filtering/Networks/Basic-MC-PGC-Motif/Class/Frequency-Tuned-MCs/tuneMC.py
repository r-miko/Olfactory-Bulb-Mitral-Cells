# File used to tune parameters for feed-forward inhibition

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np
import os

from OBfunction import runOB

# Function that runs the OB with the given parameters
def runBatch(ExFactor,InhFactor,PGFactor,frequencies):
	# Parameters
	record_vars = ['mc_soma']
	syn_vars    = []
	directory   = 'npy_files/'

	# For each frequency, run function called from OBfunction
	for frequency in frequencies:
		print frequency
		filename = 'f' + str(frequency) + '_e' + str(ExFactor) + '_i' + str(InhFactor) + '_p' + str(PGFactor) + '_'
		runOB(frequency,ExFactor,InhFactor,PGFactor,record_vars,syn_vars,directory,filename)

# Function that analyses the batch
def analyseBatch(frequencies):
	# Parameters
	directory   = ''
	tuning_curve = np.zeros((len(frequencies),))
	
	# For each frequency create tuning curve from firing rate
	for  j,frequency in enumerate(frequencies):
		filename = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_Spiketimes.npy'
		spikes= np.load(filename)
		tuning_curve[j] = len(spikes)/3.0
	return tuning_curve

# Function that plots the tuning curve
def plotTuningCurve(frequencies,tuning_curve):
	# Figure
	fig = plt.figure(figsize=(25,15))
	ax = fig.add_subplot(111)

	# Plot frequency against the tuning_curve
	ax.plot(frequencies,tuning_curve,'k*',markersize=5.0)

	# Labels and Legend
	plt.title("MC Tuning", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel("Firing Rate (Hz)", fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 23)
	plt.yticks(fontsize = 23)

	#plt.show()
	return fig

# Function that saves the plot
def saveTuningCurve(figure):
	print "Saving Plots"
	directory = "Tuning_Results/"
	filename = 'e' + str(e) + '_i' + str(i) + '_p' + str(p)
	
	# Save
	plt.savefig(directory + filename + '.png', dpi = 300)

# Main
if __name__ == "__main__":
	#Parameters
	frequencies   = np.arange(1.0, 40.0, 1.0)
	ExFactor  = [3.33, 6.66, 10.0]
	InhFactor = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
	PGFactor  = [0.2, 0.4, 0.6, 0.8, 1.0]

	#For each combination of the above parameters, run the following functions
	for e in ExFactor:
		for i in InhFactor:
			for p in PGFactor:
				runBatch(e,i,p,frequencies)
				tuning_curve = analyseBatch(frequencies)
				fig = plotTuningCurve(frequencies, tuning_curve)
				saveTuningCurve(fig)

	
