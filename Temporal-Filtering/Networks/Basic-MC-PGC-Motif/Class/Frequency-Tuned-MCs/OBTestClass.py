# Class that generates all the MC-PGC motifs

from neuron import h,gui
from nrn import *
import tabchannels
import matplotlib.pyplot as plt
import numpy as np

class OBTest(object):
	def __init__(self, mc_pgc_excitation, pgc_mc_inhibition, celsius = 35, AMPAgmax = 1.0*2e-3, AMPAalpha = 1.0, AMPAbeta = 1.0/5.5, AMPAact = 0.0, AMPAsigma = 0.2, AMPArev = 0.0, NMDAgmax = 1.0*1e-3, NMDAalpha = 1.0/52.0, NMDAbeta = 1.0/343.0, NMDAact = 0.0, NMDAsigma = 0.2, NMDArev = 0.0, GABAgmax = 8.0*2e-3, GABAalpha = 1.0/1.25, GABAbeta = 1.0/18.0, GABAact = -40.0, GABAsigma = 2.0, GABArev = -80.0):
		
		# CELLS AND CONNECTIONS
		# Parameters
		self.celsius = celsius
		
		self.AMPAgmax = AMPAgmax
		self.AMPAalpha = AMPAalpha
		self.AMPAbeta = AMPAbeta
		self.AMPAact = AMPAact
		self.AMPAsigma = AMPAsigma
		self.AMPArev = AMPArev
		
		self.NMDAgmax = NMDAgmax
		self.NMDAalpha = NMDAalpha
		self.NMDAbeta = NMDAbeta
		self.NMDAact = NMDAact
		self.NMDAsigma = NMDAsigma
		self.NMDArev = NMDArev
		
		self.GABAgmax = GABAgmax
		self.GABAalpha = GABAalpha
		self.GABAbeta = GABAbeta
		self.GABAact = GABAact
		self.GABAsigma = GABAsigma
		self.GABArev = GABArev
		
		self.mc_pgc_excitation = mc_pgc_excitation
		self.pgc_mc_inhibition = pgc_mc_inhibition
		
		# import cell
		h.load_file('MC_def.hoc', 'mc')
		h.load_file('PG_def.hoc', 'pg')
		
		# Instantiate a cell
		self.pgc = h.PGcell()
		self.mc = h.Mcell()
		
		# Determine connection
		if mc_pgc_excitation:

			# AMPA MC -> PGC
			self.pgAMPA = h.gradAMPA(self.pgc.gemmbody(0.5))
			h.setpointer(self.mc.tuft(.5)._ref_v,'vpre',self.pgAMPA)
			self.pgAMPA.gmax = self.AMPAgmax
			self.pgAMPA.alpha = self.AMPAalpha
			self.pgAMPA.beta = self.AMPAbeta
			self.pgAMPA.thetasyn = self.AMPAact
			self.pgAMPA.sigma = self.AMPAsigma
			self.pgAMPA.e = self.AMPArev
			
			# NMDA MC -> PGC
			self.pgNMDA = h.gradNMDA(self.pgc.gemmbody(0.5))
			h.setpointer(self.mc.tuft(.5)._ref_v,'vpre',self.pgNMDA)
			self.pgNMDA.gmax = self.NMDAgmax
			self.pgNMDA.alpha = self.NMDAalpha
			self.pgNMDA.beta = self.NMDAbeta
			self.pgNMDA.thetasyn = self.NMDAact
			self.pgNMDA.sigma = self.NMDAsigma
			self.pgNMDA.e = self.NMDArev
			
		if pgc_mc_inhibition:
			# GABA_A PGC -> MC
			self.mcGABA = h.gradGABA(self.mc.tuft(0.5))
			h.setpointer(self.pgc.gemmbody(.5)._ref_v,'vpre',self.mcGABA)
			self.mcGABA.gmax = self.GABAgmax
			self.mcGABA.alpha = self.GABAalpha
			self.mcGABA.beta = self.GABAbeta
			self.mcGABA.thetasyn = self.GABAact
			self.mcGABA.sigma = self.GABAsigma
			self.mcGABA.e = self.GABArev
	
	# RECORDING PARAMETERS
	# Record membrane potential
	def record_membranept(self, record_vars):
		variables = []
		for x in record_vars:
			if x is "mc_soma":
				# Membrane potential vector (at the MC soma)
				vsoma_vec = h.Vector() 
				vsoma_vec.record(self.mc.soma(0.5)._ref_v)
				variables.append(vsoma_vec)

			if x is "pgc_soma":
				# Membrane potential vector (at the PGC soma)
				vsoma_vec = h.Vector() 
				vsoma_vec.record(self.pgc.soma(0.5)._ref_v)
				variables.append(vsoma_vec)
				
			if x is "mc_tuft":
				# Membrane potential vector (at the MC tuft)
				vtuft_vec = h.Vector() 
				vtuft_vec.record(self.mc.tuft(0.5)._ref_v)
				variables.append(vtuft_vec)

			if x is "pgc_gemmbody":
				# Membrane potential vector (at the PGC gemmbody)
				vgemmbody_vec = h.Vector() 
				vgemmbody_vec.record(self.pgc.gemmbody(0.5)._ref_v)
				variables.append(vgemmbody_vec)
		return variables
	
	# Record synaptic currents
	def record_syn_currents(self,syn_vars):
		variables = []
		for s in syn_vars:
			# Synaptic current at pgAMPA
			if s is "mc_pgc_ampa":
				mc_pgc_ampa_vec = h.Vector()
				mc_pgc_ampa_vec.record(self.pgAMPA._ref_i)
				variables.append(mc_pgc_ampa_vec)
			# Synaptic current at pgNMDA
			if s is "mc_pgc_nmda":
				mc_pgc_nmda_vec = h.Vector()
				mc_pgc_nmda_vec.record(self.pgNMDA._ref_i)
				variables.append(mc_pgc_nmda_vec)
			# Synaptic current at mcGABA
			if s is "pgc_mc_gaba":
				pgc_mc_gaba_vec = h.Vector()
				pgc_mc_gaba_vec.record(self.mcGABA._ref_i)
				variables.append(pgc_mc_gaba_vec)
		return variables

	# Record time
	def record_time(self, variables):
		t_vec = h.Vector()
		t_vec.record(h._ref_t)
		variables.append(t_vec)
		return variables	

	# RECORDING ACTIVATION AND INACTIVATION
	# Na
	# Record Na Activation
	def record_na_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).nax._ref_m)
		variables.append(i_vec)
		return variables

	# Record Na Inactivation
	def record_na_inactivation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).nax._ref_h)
		variables.append(i_vec)
		return variables

	# KDRmt
	# Record KDRmt Activation
	def record_kdrmt_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).kdrmt._ref_m)
		variables.append(i_vec)
		return variables

	# kAmt
	# Record kAmt Activation
	def record_kamt_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).kamt._ref_m)
		variables.append(i_vec)
		return variables

	# Record kAmt Inactivation
	def record_kamt_inactivation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).kamt._ref_h)
		variables.append(i_vec)
		return variables

	# kM
	# Record kM Activation
	def record_km_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).kM._ref_x)
		variables.append(i_vec)
		return variables

	# Icapn
	# Record Icapn Activation
	def record_icapn_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).Icapn._ref_m)
		variables.append(i_vec)
		return variables

	# Record Icapn Inactivation
	def record_icapn_inactivation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).Icapn._ref_h)
		variables.append(i_vec)
		return variables

	# Ikca
	# Record Ikca Activation
	def record_ikca_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).Ikca._ref_Y)
		variables.append(i_vec)
		return variables
	# Icat
	# Record Icat Activation
	def record_icat_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).Icat._ref_m)
		variables.append(i_vec)
		return variables

	# Record Icat Inactivation
	def record_icat_inactivation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).Icat._ref_h)
		variables.append(i_vec)
		return variables

	# cad2
	# Record cad2 Activation
	def record_cad2_activation(self, variables):
		i_vec = h.Vector()
		i_vec.record(self.pgc.soma(0.5).cad2._ref_cai)
		variables.append(i_vec)
		return variables
	
	# RUN
	# Setup input current and run simulation				
	def run(self, variables, tstop, input_current, pgc_input_current, pgc_stim):
		# Input current	and PGC stimulation	
		stim = h.IClamp(self.mc.tuft(0.5))
		stim.delay = 0
		stim.dur = 1e9
		
		if pgc_stim:
			stim2 = h.IClamp(self.pgc.gemmbody(0.5))
			stim2.delay = 0
			stim2.dur = 1e9
		
		tvec = h.Vector(tstop)
		r=h.Vector(tstop)
		for i in range(0,tstop):
			r.x[i] = input_current[i]
			tvec.x[i]=i
		
		r.play(stim._ref_amp,tvec,1,sec=self.mc.tuft)
		if pgc_stim:
			tvec2 = h.Vector(tstop)
			r2=h.Vector(tstop)
			for i in range(0,tstop):
				r2.x[i] = pgc_input_current[i]
				tvec2.x[i]=i
			r2.play(stim2._ref_amp,tvec2,1,sec=self.pgc.gemmbody)
			
		h.tstop=tstop
		
		# Run the simulation
		h.run()

	# SPIKE CALCULATIONS
	# Calculate the spike times
	def _find_spike_times(self, vec, threshold = 0):
		gtT = vec > threshold
		leqT = np.logical_not(gtT)
		leqT = np.roll(leqT, 1)
		leqT[0] = True
		spikes = np.nonzero(np.logical_and(gtT, leqT))
		return spikes[0] * 0.025
	
	# Return the spike times at MC Soma
	def mc_soma_spike_times(self, vsoma_vec, threshold = 0):
		MC_spiketimes_list = self._find_spike_times(vsoma_vec, threshold)
		return MC_spiketimes_list

	# Return the spike times at PGC Gemmbody
	def PGC_spike_times(self, vgemmbody_vec, threshold = 0):
		PGC_spiketimes_list = self._find_spike_times(vgemmbody_vec, threshold)
		return PGC_spiketimes_list
	
	# Calculates the first spike latency
	def _first_spike_latency(self, spiketimes_list, a = 500):
		if len(spiketimes_list) > 1:
			b = spiketimes_list[0]
			if b < 510:
				b = spiketimes_list[1]
			first_spike_latency = b - a
		if len(spiketimes_list) < 2:
			first_spike_latency = -1
		return first_spike_latency
	
	# Returns first spike latency at MC Soma
	def MC_first_spike_latency(self, MC_spiketimes_list, a = 500):
		MC_first_spike_latency = self._first_spike_latency(MC_spiketimes_list, a)
		return MC_first_spike_latency

	# Returns first spike latency at PGC Gemmbody
	def PGC_first_spike_latency(self, PGC_spiketimes_list, a = 500):
		PGC_first_spike_latency = self._first_spike_latency(PGC_spiketimes_list, a)
		return PGC_first_spike_latency

	# Calculates the frequencies associated with interspike times
	def _spike_frequencies(self, spiketimes_list):
		spike_times = spiketimes_list
		interspike_times = np.diff(spike_times)
		interspike_frequencies = 1000/interspike_times
		return interspike_frequencies
		# Code in this method has been adapted from Mike Vella (2017)
	
	# Returns interspike frequency at MC Soma
	def MC_spike_frequencies(self, MC_spiketimes_list):
		MC_interspike_frequencies = self._spike_frequencies(MC_spiketimes_list)
		return MC_interspike_frequencies

	# Returns interspike frequency at PGC Gemmbody
	def PGC_spike_frequencies(self, PGC_spiketimes_list):
		PGC_interspike_frequencies = self._spike_frequencies(PGC_spiketimes_list)
		return PGC_interspike_frequencies

	# PLOTTING
	# General plot method used internally
	def _plott(self, t_vec, variable, giveTitle, saveName):
		fig = plt.figure(figsize=(8,4))
		axes = fig.add_subplot(111)
		axes.plot(t_vec, variable)
		title = axes.set_title(giveTitle)
		fig.savefig(saveName,dpi=600)
		
	# Plot the membrane potential
	def plotMemPotential_MCSoma(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotMemPotential_tuft(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotMemPotential_PGCgemmbody(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)
		
	# Plot input current
	def plotInputCurrent(self, time, input_current, saveName):
		fig = plt.figure(figsize=(8,4))
		axes = fig.add_subplot(111)
		axes.plot(time, input_current)
		title = axes.set_title("Input Current")
		fig.savefig(saveName)
	
	# Plot the synaptic current
	def plotSynapticCurrent_pgAMPA(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotSynapticCurrent_pgNMDA(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotSynapticCurrent_mcGABA(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)
	
	# Plot Activation and Inactivation of Channels
	# Na
	def plotActivationVariableNa(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotInactivationVariableNa(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# KDRmt
	def plotActivationVariableKDRmt(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# kAmt
	def plotActivationVariablekAmt(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotInactivationVariablekAmt(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# kM
	def plotActivationVariablekM(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# Icapn
	def plotActivationVariableIcapn(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotInactivationVariableIcapn(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# Ikca
	def plotActivationVariableIkca(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# Icat
	def plotActivationVariableIcat(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	def plotInactivationVariableIcat(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

	# cad2
	def plotActivationVariablecad2(self, t_vec, variable, giveTitle, saveName):
		self._plott(t_vec, variable, giveTitle, saveName)

