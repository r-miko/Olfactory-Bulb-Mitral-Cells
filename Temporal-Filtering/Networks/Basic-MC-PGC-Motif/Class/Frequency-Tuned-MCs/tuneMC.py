# File which creates and runs a model from OBTestClass.py

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np

from OBfunction import runOB




def runBatch(ExFactor,InhFactor,PGFactor,frequencies):
	record_vars = ['mc_soma']
	syn_vars    = []
	directory   = ''
	fname    = 'test'

	for  frequency in frequencies:
		print frequency
		filename = fname + '_' + str(frequency) +'_'
		runOB(frequency,ExFactor,InhFactor,PGFactor,record_vars,syn_vars,directory,filename)

def analyseBatch(frequencies):
	directory   = ''
	fname    = 'test'
	tuning_curve = np.zeros((len(frequencies),))
	for  i,frequency in enumerate(frequencies):
		filename = fname + '_' + str(frequency) +'_'+'MC_Spiketimes.npy'
		spikes= np.load(filename)
		tuning_curve[i] = len(spikes)/3.0
	return tuning_curve

def plotTuningCurve(frequencies,tuning_curve):
	fig = plt.figure(figsize=(15,25))
	ax = fig.add_subplot(111)
	ax.plot(frequencies,tuning_curve,'k*',markersize=5.0)
	plt.show()

if __name__ == "__main__":
	frequencies   = np.arange(1.0,40.0,1.0)
	ExFactor  = 3.33
	InhFactor = 4.0
	PGFactor  = 0.6
	runBatch(ExFactor,InhFactor,PGFactor,frequencies)
	tuning_curve = analyseBatch(frequencies)
	plotTuningCurve(frequencies, tuning_curve)
