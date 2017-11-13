# File which evaluates predictions

import matplotlib.pyplot as plt
import numpy as np
import random


frequency_lb = 0.5
frequency_ub = 50.0

strength_lb = 0.15
strength_ub = 0.7

frequencies = frequency_lb + (frequency_ub-frequency_lb)*np.random.rand(5,1)
strengths = strength_lb + (strength_ub-strength_lb)*np.random.rand(5,1)

for f in frequencies:
	for s in strengths:
		filename = '..._'+str(s)+'_'+str(f)
		function(s,f,True,True,True,'Prediction-Test',filename)
