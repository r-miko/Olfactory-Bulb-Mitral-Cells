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
		print 'f:', frequency, 'e:', ExFactor, 'i:', InhFactor, 'p:', PGFactor
		filename = 'f' + str(frequency) + '_e' + str(ExFactor) + '_i' + str(InhFactor) + '_p' + str(PGFactor) + '_'
		runOB(frequency,ExFactor,InhFactor,PGFactor,record_vars,syn_vars,directory,filename)

# Function that analyses the batch for firing rates and latency
def analyseBatch(frequencies):
	# Parameters
	directory   = 'npy_files/'
	TC = []
	tuning_curveFR = np.zeros((len(frequencies),))
	tuning_curveL = np.zeros((len(frequencies),))
	
	# For each frequency create tuning curve from firing rate
	for  j,frequency in enumerate(frequencies):
		filenameFR = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_Spiketimes.npy'
		spikes= np.load(directory+filenameFR)
		tuning_curveFR[j] = len(spikes)/3.0
	TC.append(tuning_curveFR)
	# For each frequency create tuning curve from latency
	for  j,frequency in enumerate(frequencies):
		filenameL = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_First_spike_latency.npy'
		latency = np.load(directory+filenameL)
		#tuning_curveL[j] = len(latency)/3.0
	TC.append(tuning_curveL)
	return TC

# Function that plots the tuning curve
def plotTuningCurve(frequencies,tuning_curve, ylabel):
	# Figure
	fig = plt.figure(figsize=(25,15))
	ax = fig.add_subplot(111)

	# Plot frequency against the tuning_curve
	ax.plot(frequencies,tuning_curve,'b*',markersize=15.0)

	# Labels and Legend
	plt.title("MC Tuning", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel(ylabel, fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 23)
	plt.yticks(fontsize = 23)

	#plt.show()
	return fig

# Function that saves the plot
def saveTuningCurve(figure, feature):
	print "Saving Plots..."
	directory = "Tuning_Results2/"
	filename = 'e' + str(e) + '_i' + str(i) + '_p' + str(p) + feature
	
	# Save
	plt.savefig(directory + filename + '.png')

# Main
if __name__ == "__main__":
	#Parameters
	frequencies   = np.arange(1.0, 40.0, 1.0)
	ExFactor  = [2.0, 4.0, 6.0, 8.0, 10.0]
	InhFactor = [1.0, 2.0, 3.0, 4.0, 5.0]
	PGFactor  = [0.2, 0.3, 0.4, 0.5, 0.6]

	#For each combination of the above parameters, run the following functions
	for e in ExFactor:
		for i in InhFactor:
			for p in PGFactor:
				runBatch(e,i,p,frequencies)
				TC = analyseBatch(frequencies)
				figFR = plotTuningCurve(frequencies, TC[1], "Firing Rate (Hz)")
				figL = plotTuningCurve(frequencies, TC[0], "Latency (ms)")
				saveTuningCurve(figFR, "FR")
				saveTuningCurve(figL, "L")

	
