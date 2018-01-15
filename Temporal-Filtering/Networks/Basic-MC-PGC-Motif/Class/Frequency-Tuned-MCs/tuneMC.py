# File which tunes parameters for feed-forward inhibition
# Returns the peak frequency of the tuning curves
# Returns the resonance strength

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np
import os

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from OBfunction import runOB

# Function that runs the OB with the given parameters
def runBatch(ExFactor, InhFactor, PGFactor, frequencies):
	# Parameters
	record_vars = ['mc_soma']
	syn_vars    = []
	directory   = 'npy_files/'

	# For each frequency, run function called from OBfunction
	for frequency in frequencies:
		print 'f:', frequency, 'e:', ExFactor, 'i:', InhFactor, 'p:', PGFactor
		filename = 'f' + str(frequency) + '_e' + str(ExFactor) + '_i' + str(InhFactor) + '_p' + str(PGFactor) + '_'
		runOB(frequency, ExFactor, InhFactor, PGFactor, record_vars, syn_vars,directory, filename)

# Function that analyses the batch for firing rates and latency
def analyseBatch(frequencies):
	# Parameters
	directory	= 'npy_files/'
	TC		= []
	tuning_curveFR	= np.zeros((len(frequencies),))
	tuning_curveL	= np.zeros((len(frequencies),))
	
	# For each frequency create tuning curve from firing rate
	for  j,frequency in enumerate(frequencies):
		filenameFR = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_Spiketimes.npy'
		spikes = np.load(directory + filenameFR)
		tuning_curveFR[j] = len(spikes)/3.0
	TC.append(tuning_curveFR)
	# For each frequency create tuning curve from latency
	for  j,frequency in enumerate(frequencies):
		filenameL = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_First_spike_latency.npy'
		latency = np.load(directory + filenameL)
		tuning_curveL[j] = latency
	TC.append(tuning_curveL)

	return TC

# Function that plots the tuning curve
def plotTuningCurve(frequencies, tuning_curve, ylabel):
	# Figure
	fig = plt.figure(figsize=(25, 15))
	ax = fig.add_subplot(111)

	# Plot frequency against the tuning_curve
	ax.plot(frequencies, tuning_curve, 'b*',markersize = 15.0)

	# Labels and Legend
	plt.title("MC Tuning", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	plt.ylabel(ylabel, fontsize = 30)
	plt.xlabel("Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 23)
	plt.yticks(fontsize = 23)
	
	#plt.show()
	return fig

# Function that saves the tuning plot
def saveTuningCurve(figure, feature):
	print "Saving Plots..."
	directory = "Tuning_Results2/"
	filename = 'e' + str(e) + '_i' + str(i) + '_p' + str(p) + feature
	
	# Save
	plt.savefig(directory + filename + '.png')
	plt.close()

	
def extractPeak(tuning_curve):
	peak = np.argmax(tuning_curve)

	return peak

def extractPeakFR(tuning_curve):
	peak = np.max(tuning_curve)

	return peak

def extractMean(tuning_curve):
	mean = np.mean(tuning_curve)

	return mean

def plotPeaks(peaks, X, Y, minvalue, maxvalue):
	# Variables
	l = []
	
	# Figure 
	fig = plt.figure(figsize=(20, 20))
	for i,j in zip(range(len(peaks)), PGFactor):
		l.append([i,j])
		ax = fig.add_subplot(3, 2, i+1)
		im = ax.imshow(peaks[i], extent = (X.min(), X.max(), Y.max(), Y.min()), vmax = maxvalue, vmin = minvalue, interpolation = 'bilinear', cmap = cm.coolwarm, aspect = 1.5)
		ax.set_xlabel('Excitation Factor', fontsize = 20)
		ax.set_ylabel('Inhibition Factor', fontsize = 20)
		ax.set_title('PG Input ' + str(j), loc = 'left', fontsize = 20)
	#fig.text(0.25, 0.95, 'Peak Frequency of the Tuning Curves', va = 'center', rotation = 'horizontal', fontsize = 40)
	fig.text(0.2, 0.95, 'Resonance Strength of the Tuning Curves', va = 'center', rotation = 'horizontal', fontsize = 40)

	# Colour bar
	cax = plt.axes([0.575, 0.1, 0.035, 0.23])
	cbar = fig.colorbar(im, cax = cax)
	
	return fig

# Main
if __name__ == "__main__":
	# Parameters
	frequencies = np.arange(1.0, 40.0, 1.0)
	ExFactor = [2.0, 4.0, 6.0, 8.0, 10.0]
	InhFactor = [1.0, 2.0, 3.0, 4.0, 5.0]
	PGFactor  = [0.2, 0.3, 0.4, 0.5, 0.6]

	# Variables
	FRpeaks = np.zeros((5, 5, 5))

	FRtuningstrength = np.zeros((5, 5, 5))

	# For each combination of the above parameters, run the following functions
	for j,e in enumerate(ExFactor):
		for k,i in enumerate(InhFactor):
			for l,p in enumerate(PGFactor):
				#runBatch(e, i, p, frequencies)
				TC = analyseBatch(frequencies)
				# Plot and save firing rates
				#figFR = plotTuningCurve(frequencies, TC[0], "Firing Rate (Hz)")
				#saveTuningCurve(figFR, "FR")
				# Plot and save latency
				#figL = plotTuningCurve(frequencies, TC[1], "Latency (ms)")
				#saveTuningCurve(figL, "L")
				# Peaks
				#FRpeaks[j, k, l] = extractPeak(TC[0])
				p  = extractPeakFR(TC[0])
				mu = extractMean(TC[0])
				FRtuningstrength[j, k, l] = (p - mu)/mu

	# Plot peaks 
	#peaks = [FRpeaks[:, :, 0], FRpeaks[:, :, 1], FRpeaks[:, :, 2], FRpeaks[:, :, 3], FRpeaks[:, :, 4]]
	#minvalue = np.min(FRpeaks[:])
	#maxvalue = np.max(FRpeaks[:])
	peaks = [FRtuningstrength[:, :, 0], FRtuningstrength[:, :, 1], FRtuningstrength[:, :, 2], FRtuningstrength[:, :, 3], FRtuningstrength[:, :, 4]]
	minvalue = np.min(FRtuningstrength[:])
	maxvalue = np.max(FRtuningstrength[:])
	fig = plotPeaks(peaks, np.array(ExFactor), np.array(InhFactor), minvalue, maxvalue)
	#plt.show()

	#Save contour plot
	print "Saving contour plots..."
	#filename = 'Contour_plot'
	#filename = 'Contour_plot_tuning_frequency'
	filename = 'Contour_plot_tuning_strength'
	plt.savefig(filename + '.png')
	#plt.close()
		



