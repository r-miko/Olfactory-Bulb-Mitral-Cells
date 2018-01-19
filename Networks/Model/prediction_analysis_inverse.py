# File which runs simulations to evaluate predictions of strength and frequency
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from prediction import inversePredict

frequencies = np.load('Prediction-Test/frequencies.npy')
strengths = np.load('Prediction-Test/strengths.npy')

latencies = np.zeros((len(frequencies),len(strengths)))
firingrates = np.zeros((len(frequencies),len(strengths)))

strengths_prediction = np.zeros((len(frequencies),len(strengths)))
frequencies_prediction = np.zeros((len(frequencies),len(strengths)))

for i,f in enumerate(frequencies):
	for j,s in enumerate(strengths):
		filename = 'prediction_circuit1_'+str(s)+'_'+str(f)

		l = np.load('Prediction-Test/'+filename+'MC_First_spike_latency.npy')
		fr = len(np.load('Prediction-Test/'+filename+'MC_Spiketimes.npy'))/6.0

		latencies[i,j]=l
		firingrates[i,j]=fr

		ff,ss = inversePredict(fr,l)
		strengths_prediction[i,j] = ss
		frequencies_prediction[i,j] = ff
		
strengths, frequencies = np.meshgrid(strengths, frequencies)

# Calculate RMSE error
rmse_strengths = np.sqrt(np.sum(np.sum(((strengths-strengths_prediction)**2)))/25.0)
print rmse_strengths

rmse_frequencies = np.sqrt(np.sum(np.sum(((frequencies-frequencies_prediction)**2)))/25.0)
print rmse_frequencies

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111,projection='3d')
ax.scatter(latencies[:],firingrates[:],strengths[:])
ax.scatter(latencies[:],firingrates[:],strengths_prediction[:])

#plt.show()
