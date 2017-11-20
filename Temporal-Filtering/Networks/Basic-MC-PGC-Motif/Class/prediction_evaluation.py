# File which runs simulations to evaluate predictions

import matplotlib.pyplot as plt
import numpy as np
import random
from OBfunction import runOB
'''
frequency_lb = 0.5
frequency_ub = 50.0

strength_lb = 0.15
strength_ub = 0.7

frequencies = [float("{0:.2f}".format(x[0])) for x in  frequency_lb + (frequency_ub-frequency_lb)*np.random.rand(5,1)]
strengths = [float("{0:.2f}".format(x[0])) for x in strength_lb + (strength_ub-strength_lb)*np.random.rand(5,1)]
'''
frequencies = np.load('Prediction-Test/frequencies.npy')
strengths = np.load('Prediction-Test/strengths.npy')



print frequencies
print strengths

for f in frequencies:
	print 'frequency',f
	for s in strengths:
		print 'strength',s
		filename = 'prediction_circuit3_'+str(s)+'_'+str(f)
		runOB(s,f,True,True,False,['mc_soma'],[],'Prediction-Test/',filename)

#np.save('Prediction-Test/frequencies.npy',frequencies)
#np.save('Prediction-Test/strengths.npy',strengths)

