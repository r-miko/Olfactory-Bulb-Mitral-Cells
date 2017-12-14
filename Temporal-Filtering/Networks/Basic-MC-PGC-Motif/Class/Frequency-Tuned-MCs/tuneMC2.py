# File used to tune parameters for feed-forward inhibition

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
	directory	= 'npy_files/'
	TC		= []
	tuning_curveFR	= np.zeros((len(frequencies),))
	tuning_curveL	= np.zeros((len(frequencies),))
	
	# For each frequency create tuning curve from firing rate
	for  j,frequency in enumerate(frequencies):
		filenameFR = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_Spiketimes.npy'
		spikes = np.load(directory+filenameFR)
		tuning_curveFR[j] = len(spikes)/3.0
	TC.append(tuning_curveFR)
	# For each frequency create tuning curve from latency
	for  j,frequency in enumerate(frequencies):
		filenameL = 'f' + str(frequency) + '_e' + str(e) + '_i' + str(i) + '_p' + str(p) +'_' + 'MC_First_spike_latency.npy'
		latency = np.load(directory+filenameL)
		tuning_curveL[j] = latency
	TC.append(tuning_curveL)
	return TC

# Function that plots the tuning curve
def plotTuningCurve(frequencies,tuning_curve,ylabel):
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

def plotPeaks(peaks, X, Y):
	# Figure
	fig = plt.figure(figsize = (25,15))
	ax = fig.gca(projection = '3d')
	
	# Plot
	X,Y = np.meshgrid(X, Y)
	surf = ax.plot_surface(X, Y, peaks, cmap = cm.coolwarm, linewidth = 0, antialiased = False)

	# Labels and Legend
	plt.title("Peak Frequency of the Tuning Curve", fontsize = 34)
	ax.title.set_position([0.5, 1.03])
	ax.set_xlabel("Ex Factor", fontsize = 30)
	ax.set_ylabel("Inh Factor", fontsize = 30)
	ax.set_zlabel("Peak Frequency (Hz)", fontsize = 30)
	plt.xticks(fontsize = 23)
	plt.yticks(fontsize = 23)

	#Add a color bar which maps values to colors.
	#fig.colorbar(surf, shrink=0.5, aspect=5)
	#plt.colorbar(surf)

	#plt.show()
	return fig

def plotPeaks2(peaks, X, Y):
	# Figure 
	plt.figure(figsize = (25,15))

	# Plot
	fig = plt.imshow(peaks, extent=(X.min(), X.max(), Y.max(), Y.min()), interpolation = 'bilinear', cmap = cm.coolwarm)

	# Labels and Legend
	plt.title("Peak Frequency of the Tuning Curve", fontsize = 34, y = 1.08)
	plt.xlabel("Excitation Factor", fontsize = 20)
	plt.ylabel("Inhibitory Factor", fontsize = 20)

	#Add a color bar which maps values to colors.
	plt.colorbar(fig)

	#plt.show()
	return fig


def plotPeaks3(peaks, X, Y, minvalue, maxvalue):
	print minvalue,maxvalue
	fig = plt.figure(figsize=(20, 20))
	
	#fig.title("Peak Frequency of the Tuning Curve", fontsize = 34, y = 1.08)
	for i in range(len(peaks)):
		ax = fig.add_subplot(3, 2, i+1)
		im = ax.imshow(peaks[i], extent=(X.min(), X.max(), Y.max(), Y.min()), vmax=maxvalue, vmin=minvalue, interpolation = 'bilinear', cmap = cm.coolwarm)
		ax.set_xlabel('Excitation Factor', fontsize = 12)
		ax.set_ylabel('Inhibitory Factor', fontsize = 12)
		ax.set_title('PG Factor ' + str(p), loc = 'left')
	
	# Figure title
	fig.text(0.33, 0.95, 'Peak Frequency of the Tuning Curve', va = 'center', rotation = 'horizontal', fontsize = 30)

	# Colour bar
	cax = plt.axes([0.575, 0.1, 0.035, 0.23])
	cbar = fig.colorbar(im, cax=cax)
	
	return fig

# Function that saves the contour plot
def saveContourPlot(figure):
	print "Saving Plots..."
	directory = "Contour_Plots/"
	filename = 'PGFactor' + str(p)
	
	# Save
	plt.savefig(directory + filename + '.png')
	plt.close()

# Main
if __name__ == "__main__":
	#Parameters
	frequencies   = np.arange(1.0, 40.0, 1.0)
	ExFactor  = [2.0, 4.0, 6.0, 8.0, 10.0]
	InhFactor = [1.0, 2.0, 3.0, 4.0, 5.0]
	PGFactor  = [0.2, 0.3, 0.4, 0.5, 0.6]


	FRpeaks = np.zeros((5,5,5))

	#For each combination of the above parameters, run the following functions
	for j,e in enumerate(ExFactor):
		for k,i in enumerate(InhFactor):
			for l,p in enumerate(PGFactor):
				#runBatch(e,i,p,frequencies)
				TC = analyseBatch(frequencies)
				# Plot and save firing rates
				#figFR = plotTuningCurve(frequencies, TC[0], "Firing Rate (Hz)")
				#saveTuningCurve(figFR, "FR")
				# Plot and save latency
				#figL = plotTuningCurve(frequencies, TC[1], "Latency (ms)")
				#saveTuningCurve(figL, "L")
				FRpeaks[j,k,l] = extractPeak(TC[0])
				#print FRpeaks[j,k,l]

	# Plot peaks 
	#for m in range(len(PGFactor)):
	#	fig = plotPeaks2(FRpeaks[:,:,m], np.array(ExFactor), np.array(InhFactor))
	peaks = [FRpeaks[:,:,0],FRpeaks[:,:,1],FRpeaks[:,:,2],FRpeaks[:,:,3],FRpeaks[:,:,4]]
	minvalue = np.min(FRpeaks[:])
	maxvalue = np.max(FRpeaks[:])
	fig = plotPeaks3(peaks,np.array(ExFactor), np.array(InhFactor),minvalue,maxvalue)
	plt.show()
	# Save peak plots
	#for l,p in enumerate(PGFactor):
	#	saveContourPlot(fig)
		



