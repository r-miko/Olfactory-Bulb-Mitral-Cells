# File which runs simulations to evaluate predictions of latency and firingrates

import matplotlib.pyplot as plt
import numpy as np
from prediction import predict

frequencies = np.load('Prediction-Test/frequencies.npy')
strengths = np.load('Prediction-Test/strengths.npy')

latencies = np.zeros((len(frequencies),len(strengths)))
firingrates = np.zeros((len(frequencies),len(strengths)))

latencies_prediction = np.zeros((len(frequencies),len(strengths)))
firingrates_prediction = np.zeros((len(frequencies),len(strengths)))

for i,f in enumerate(frequencies):
	for j,s in enumerate(strengths):
		filename = 'prediction_'+str(s)+'_'+str(f)

		latencies[i,j] = np.load('Prediction-Test/'+filename+'MC_First_spike_latency.npy')
		firingrates[i,j] = len(np.load('Prediction-Test/'+filename+'MC_Spiketimes.npy'))/6.0

		fr,l = predict(s,f)
		latencies_prediction[i,j] = l
		firingrates_prediction[i,j] = fr
		
strengths, frequencies = np.meshgrid(strengths, frequencies)

# Calculate RMSE error
rmse_latencies = np.sqrt(np.sum(np.sum(((latencies-latencies_prediction)**2)))/25.0)
print rmse_latencies

rmse_firingrates = np.sqrt(np.sum(np.sum(((firingrates-firingrates_prediction)**2)))/25.0)
print rmse_firingrates
