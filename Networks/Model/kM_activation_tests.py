# File which tests the activation for kM

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np
from OBTestClass import OBTest

# MODEL
# Model parameters
mc_pgc_excitation = False
pgc_mc_inhibition = True
celsius = 35
AMPAgmax = 10.0*2e-3
AMPAalpha = 1.0
AMPAbeta = 1.0/5.5
AMPAact = 0.0
AMPAsigma = 0.2
AMPArev = 0.0
NMDAgmax = 10.0*1e-3
NMDAalpha = 1.0/52.0
NMDAbeta = 1.0/343.0
NMDAact = 0.0
NMDAsigma = 0.2
NMDArev = 0.0
GABAgmax = 8.0*2e-3
GABAalpha = 1.0/1.25
GABAbeta = 1.0/18.0
GABAact = -40.0
GABAsigma = 2.0
GABArev = -80.0

# Create model
model = OBTest(mc_pgc_excitation, pgc_mc_inhibition, celsius, AMPAgmax, AMPAalpha, AMPAbeta, AMPAact, AMPAsigma, AMPArev, NMDAgmax, NMDAalpha, NMDAbeta, NMDAact, NMDAsigma, NMDArev, GABAgmax, GABAalpha, GABAbeta, GABAact, GABAsigma, GABArev)

# STIMULATION
# Stim parameters
tstop = 6000
time = range(0, tstop)
hz = 40 #[1, 2, 5, 10, 20, 30, 40]
c1 = 0.27 #[0.27, 0.315, 0.36, 0.405, 0.45, 0.495, 0.6]
c2 = 0.18
factor = 0.2


# Input current
input_current = np.ones((tstop,))*[np.cos((t/1000.0)*(2*np.pi*hz)) for t in time]*c2 + c1
input_current[0:500] = 0.0
		
# PGC stim
pgc_stim = True

pgc_input_current = (np.ones((tstop,))*[np.cos((t/1000.0)*(2*np.pi*hz)) for t in time]*c2 + c1)*factor
pgc_input_current[0:500] = 0.0

variables = []

# Record membrane potential and time
record_vars = ["pgc_gemmbody","pgc_soma"]
variables = model.record_membranept(record_vars)
variables = model.record_km_activation(variables)
variables = model.record_time(variables)

# Run model
model.run(variables, tstop, input_current, pgc_input_current, pgc_stim)

# PLOTTING AND SAVING		
# Directory
directory = "Activation_Tests/kM_Test/"
parameters = "_40Hz_c0.27"
		
# Plotting
t_vec = variables[-1]
model.plotMemPotential_PGCgemmbody(t_vec, variables[0], "PG gemmbody membrane potential", directory + "V_gemmbody" + parameters + ".png")
model.plotMemPotential_PGCgemmbody(t_vec, variables[1], "PG soma membrane potential", directory + "V_soma" + parameters + ".png")
model.plotActivationVariablekM(t_vec, variables[2], "Activation of kM", directory + "kM_activation" + parameters + ".png")

