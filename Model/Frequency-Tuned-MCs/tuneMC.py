# File which tunes parameters for feed-forward inhibition
# Returns the peak frequency of the tuning curves
# Returns the resonance frequency and resonance strength

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np
import os

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from OBfunction import runOB

# Run the OB with the given parameters
def runBatch(ExFactor, InhFactor, PGFactor, frequencies):
	# Parameters
	record_vars = ['mc_soma']
	syn_vars = []
	directory = 'npy_files/'

	# For each frequency, run function called from OBfunction
	for frequency in frequencies:
		print 'f:', frequency, 'e:', ExFactor, 'i:', InhFactor, 'p:', PGFactor
		filename = 'f' + str(frequency) + '_e' + str(ExFactor) + '_i' + str(InhFactor) + '_p' + str(PGFactor) + '_'
		runOB(frequency, ExFactor, InhFactor, PGFactor, record_vars, syn_vars,directory, filename)

# Analyse batch for firing rates and latency
def analyseBatch(frequencies):
	# Parameters
	directory = 'npy_files/'
	TC = []
	tuning_curveFR = np.zeros((len(frequencies),))
	tuning_curveL = np.zeros((len(frequencies),))
	
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

# Plot tuning curve
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
	plt.xticks(fontsize = 30)
	plt.yticks(fontsize = 30)
	
	#plt.show()
	return fig

# Save tuning plot
def saveTuningCurve(figure, feature):
	print "Saving Plots..."
	directory = "Tuning_Results2/"
	filename = 'e' + str(e) + '_i' + str(i) + '_p' + str(p) + feature
	
	# Save
	plt.savefig(directory + filename + '.png')
	plt.close()

# Extract peak from tuning curves
def extractPeak(tuning_curve):
	peak = np.argmax(tuning_curve)
	return peak

def extractPeakFR(tuning_curve):
	peak = np.max(tuning_curve)
	return peak

# Extract mean from tuning curves
def extractMean(tuning_curve):
	mean = np.mean(tuning_curve)
	return mean

# Plot the peaks
def plotPeaks(peaks, X, Y, minvalue, maxvalue, RFbool):
	# Variables
	l = []
	
	# Figure 
	fig = plt.figure(figsize=(20, 20))
	for i,j in zip(range(len(peaks)), PGFactor):
		l.append([i,j])
		ax = fig.add_subplot(3, 2, i+1)
		im = ax.imshow(peaks[i], extent = (X.min(), X.max(), Y.max(), Y.min()), vmax = maxvalue, vmin = minvalue, interpolation = 'bilinear', cmap = cm.coolwarm, aspect = 2.0)
		ax.set_xlabel('$W_{exc.}$', fontsize = 30)
		ax.set_ylabel('$W_{inh.}$', fontsize = 30)
		ax.set_title('PGC Input = ' + str(j), loc = 'left', fontsize = 25)
		ax.tick_params(labelsize = 18)
	fig.subplots_adjust(left = None, bottom = None, right = None, top = None, wspace = None, hspace = 0.3)
	
	if RFbool:
		fig.text(0.175, 0.95, 'Resonance Frequency of the Tuning Curves', va = 'center', rotation = 'horizontal', fontsize = 45)
	else:
		fig.text(0.15, 0.95, 'Resonance Strength (Q) of the Tuning Curves', va = 'center', rotation = 'horizontal', fontsize = 45)

	# Colour bar
	cax = plt.axes([0.575, 0.1, 0.035, 0.23])
	cax.tick_params(labelsize = 18)
	cbar = fig.colorbar(im, cax = cax)
	
	if RFbool:
		cbar.ax.set_ylabel("Resonance Frequency (Hz)", fontsize = 25, labelpad = 25)
	else:
		cbar.ax.set_ylabel("Resonance Strength (Q)", fontsize = 25, labelpad = 25)

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
	# Resonance Frequency
	#peaks = [FRpeaks[:, :, 0], FRpeaks[:, :, 1], FRpeaks[:, :, 2], FRpeaks[:, :, 3], FRpeaks[:, :, 4]]
	#minvalue = np.min(FRpeaks[:])
	#maxvalue = np.max(FRpeaks[:])
	#fig = plotPeaks(peaks, np.array(ExFactor), np.array(InhFactor), minvalue, maxvalue, True)
	#plt.show()

	# Resonance Strength
	peaks = [FRtuningstrength[:, :, 0], FRtuningstrength[:, :, 1], FRtuningstrength[:, :, 2], FRtuningstrength[:, :, 3], FRtuningstrength[:, :, 4]]
	minvalue = np.min(FRtuningstrength[:])
	maxvalue = np.max(FRtuningstrength[:])
	fig = plotPeaks(peaks, np.array(ExFactor), np.array(InhFactor), minvalue, maxvalue, False)
	#plt.show()

	# Save contour plot
	results_directory = "Tuning_Results/"
	print "Saving contour plots..."
	
	#filename = 'Contour_plot_tuning_frequency'
	filename = 'Contour_plot_tuning_strength'
	
	plt.savefig(results_directory + filename + '.pdf')
	#plt.close()
		



