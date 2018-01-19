# Prediction and inverse prediction

def predict(s,f):

	fr = 32.26*s-0.59
	l  = -16*f+645.4

	return fr,l

def inversePredict(fr,l):

	f = -(l-645.4)/16.0
	s = (fr+0.59)/32.26
	return f,s
