# File which creates and runs a model from OBTestClass.py

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np
from OBTestClass import OBTest

# MODEL
# Model parameters
def runOB(frequency,ExFactor,InhFactor,PGFactor,record_vars,syn_vars,directory,filename):
	celsius = 35
	AMPAgmax = ExFactor*2e-3
	AMPAalpha = 1.0
	AMPAbeta = 1.0/5.5
	AMPAact = 0.0
	AMPAsigma = 0.2
	AMPArev = 0.0
	NMDAgmax = ExFactor*1e-3
	NMDAalpha = 1.0/52.0
	NMDAbeta = 1.0/343.0
	NMDAact = 0.0
	NMDAsigma = 0.2
	NMDArev = 0.0
	GABAgmax = InhFactor*2e-3
	GABAalpha = 1.0/1.25
	GABAbeta = 1.0/18.0
	GABAact = -40.0
	GABAsigma = 2.0
	GABArev = -80.0


	mc_pgc_excitation = True 
	pgc_mc_inhibition = True
	pgc_stim = True

	# STIMULATION
	# Stim parameters
	tstop = 3000
	time = range(0, tstop)
	strength = 0.45
	c2 = 0.18


	# Create model
	model = OBTest(mc_pgc_excitation, pgc_mc_inhibition, celsius, AMPAgmax, AMPAalpha, AMPAbeta, AMPAact, AMPAsigma, AMPArev, NMDAgmax, NMDAalpha, NMDAbeta, NMDAact, NMDAsigma, NMDArev, GABAgmax, GABAalpha, GABAbeta, GABAact, GABAsigma, GABArev)


	# Input current
	input_current = np.ones((tstop,))*[np.cos((t/1000.0)*(2*np.pi*frequency)) for t in time]*c2 + strength
	input_current[0:500] = 0.0
		

	pgc_input_current = (np.ones((tstop,))*[np.cos((t/1000.0)*(2*np.pi*frequency)) for t in time]*c2 + strength)*PGFactor
	pgc_input_current[0:500] = 0.0

	# Record membrane potential and time
	variables = model.record_membranept(record_vars)
	variables = model.record_time(variables)

	# Record synaptic currents
	#if mc_pgc_excitation:
	#	syn_vars.append("mc_pgc_ampa")
	#	syn_vars.append("mc_pgc_nmda")
	#if pgc_mc_inhibition: 
	#	syn_vars.append("pgc_mc_gaba")
		
	synvariables = model.record_syn_currents(syn_vars)

	# Run model
	model.run(variables, tstop, input_current, pgc_input_current, pgc_stim)

	# Calculate spike times, first spike latency and interspike frequency
	vec1 = variables[0]
	l = np.array(vec1)
	MC_spiketimes_list = model.mc_soma_spike_times(l, threshold = 0)
	if len(MC_spiketimes_list) > 0:
		MC_first_spike_latency = model.MC_first_spike_latency(MC_spiketimes_list, a = 500)
		MC_interspike_freq = model.MC_spike_frequencies(MC_spiketimes_list)
	'''
	vec2 = variables[2]
	p = np.array(vec2)
	PGC_spiketimes_list = model.PGC_spike_times(p, threshold = 0)
	if len(PGC_spiketimes_list) > 0:
		PGC_first_spike_latency = model.PGC_first_spike_latency(PGC_spiketimes_list, a = 500)
		PGC_interspike_freq = model.PGC_spike_frequencies(PGC_spiketimes_list)
	'''
	# PLOTTING AND SAVING		

		
	# Plotting membrane potential and input current
	t_vec = variables[-1]
	'''
	for i,x in enumerate(record_vars):
		variable = variables[i]
		if x is "mc_soma":
			model.plotMemPotential_MCSoma(t_vec, variable, "Membrane Potential at MC Soma", directory + filename + "MC_Soma.png")
		if x is "mc_tuft":
			model.plotMemPotential_tuft(t_vec, variable, "Membrane Potential at MC tuft", directory + filename +"MC_Tuft.png")
		if x is "pgc_gemmbody":
			model.plotMemPotential_PGCgemmbody(t_vec, variable, "Membrane Potential at PGC gemmbody", directory + filename +"PGC_gemmbody.png")
	'''
	#model.plotInputCurrent(time, input_current, directory+"Input_Current.png")
		
	# Plotting synaptic currents
	if len(syn_vars) is 1:
		model.plotSynapticCurrent_mcGABA(t_vec, synvariables[0], "Synaptic Current at mcGABA", directory +filename + "SC_mcGABA.png")
	if len(syn_vars) is 2:
		model.plotSynapticCurrent_pgAMPA(t_vec, synvariables[0], "Synaptic Current at pgAMPA", directory +filename + "SC_pgAMPA.png")
		model.plotSynapticCurrent_pgNMDA(t_vec, synvariables[1], "Synaptic Current at pgNMDA", directory +filename + "SC_pgNMDA.png")
	if len(syn_vars) is 3:
		model.plotSynapticCurrent_mcGABA(t_vec, synvariables[0], "Synaptic Current at mcGABA", directory + filename +"SC_mcGABA.png")
		model.plotSynapticCurrent_pgAMPA(t_vec, synvariables[1], "Synaptic Current at pgAMPA", directory + filename +"SC_pgAMPA.png")
		model.plotSynapticCurrent_pgNMDA(t_vec, synvariables[2], "Synaptic Current at pgNMDA", directory + filename +"SC_pgNMDA.png")

	# Save
	#np.save(directory+ filename +"Input_current",input_current)
	for i,x in enumerate(record_vars):
		variable = variables[i]
		np.save(directory +  filename +x, variable)
	#np.save(directory + filename + "Time", variables[-1]) 
	np.save(directory + filename + "MC_Spiketimes", MC_spiketimes_list)
	#if len(MC_spiketimes_list) > 0:
	#	np.save(directory + filename + "MC_Interspike_frequencies", MC_interspike_freq)
	#	np.save(directory +  filename +"MC_First_spike_latency", MC_first_spike_latency)
	#if len(MC_spiketimes_list) == 0:
	#	np.save(directory + filename + "MC_Interspike_frequencies", -1)
	#	np.save(directory +  filename +"MC_First_spike_latency", -1)
	'''
	np.save(directory + filename + "PGC_Spiketimes", PGC_spiketimes_list)
	if len(PGC_spiketimes_list) > 0:
		np.save(directory +  filename +"PGC_Interspike_frequencies", PGC_interspike_freq)
		np.save(directory +  filename +"PGC_First_spike_latency", PGC_first_spike_latency)
	if len(PGC_spiketimes_list) == 0:
		np.save(directory +  filename +"PGC_Interspike_frequencies", -1)
		np.save(directory + filename + "PGC_First_spike_latency", -1)
	if len(syn_vars) is 1:
		np.save(directory +  filename +"pgc_mc_gaba", synvariables[0])
	if len(syn_vars) is 2:
		np.save(directory + filename + "mc_pgc_ampa", synvariables[0])
		np.save(directory +  filename +"mc_pgc_nmda", synvariables[1])
	if len(syn_vars) is 3:
		np.save(directory +  filename +"mc_pgc_ampa", synvariables[0])
		np.save(directory + filename + "mc_pgc_nmda", synvariables[1])
		np.save(directory +  filename +"pgc_mc_gaba", synvariables[2])
	'''
	plt.close("all")

