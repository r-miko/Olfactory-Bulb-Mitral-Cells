''' Test file for the stimulation of the basic MC-PGC motif
of the Cleland model'''

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np

# import cell
h.xopen('MC_def.hoc')
h.xopen('PG_def.hoc')

# Parameters
tstop   = 6000
celsius = 35 

AMPAgmax = 1.0*2e-3
AMPAalpha = 1.0
AMPAbeta = 1.0/5.5
AMPAact = 0.0
AMPAsigma = 0.2
AMPArev = 0.0

NMDAgmax = 1.0*1e-3
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

# Instantiate a cell
pgc = h.PGcell()
mc  = h.Mitral()

# connect MC and PGC cells 
# AMPA MC -> PGC
pgAMPA = h.gradAMPA(pgc.gemmbody(0.5))
h.setpointer(mc.tuft(.5)._ref_v,'vpre',pgAMPA)
pgAMPA.gmax = AMPAgmax
pgAMPA.alpha = AMPAalpha
pgAMPA.beta = AMPAbeta
pgAMPA.thetasyn = AMPAact
pgAMPA.sigma = AMPAsigma
pgAMPA.e = AMPArev

# NMDA MC -> PGC
pgNMDA = h.gradNMDA(pgc.gemmbody(0.5))
h.setpointer(mc.tuft(.5)._ref_v,'vpre',pgNMDA)
pgNMDA.gmax = NMDAgmax
pgNMDA.alpha = NMDAalpha
pgNMDA.beta = NMDAbeta
pgNMDA.thetasyn = NMDAact
pgNMDA.sigma = NMDAsigma
pgNMDA.e = NMDArev

# GABA_A PGC -> MC
mcGABA = h.gradGABA(mc.tuft(0.5))
h.setpointer(pgc.gemmbody(.5)._ref_v,'vpre',mcGABA)
mcGABA.gmax = GABAgmax
mcGABA.alpha = GABAalpha
mcGABA.beta = GABAbeta
mcGABA.thetasyn = GABAact
mcGABA.sigma = GABAsigma
mcGABA.e = GABArev

# Variable input current
stim = h.IClamp(mc.tuft(0.5))
stim.delay = 0
stim.dur = 1e9

hz = 3
c = 0.15
time = range(0,tstop)
input_current = np.ones((tstop,))*[np.cos((t/1000.0)*(2*np.pi*hz)) for t in time]*c + c
input_current[0:1000] = 0.0

tvec = h.Vector(tstop)
r=h.Vector(tstop)
for i in range(0,tstop):
	r.x[i] = input_current[i]
	tvec.x[i]=i

#r[tstop-1]=0.0
r.play(stim._ref_amp,tvec,1,sec=mc.tuft)

# Set up recording variables
vsoma_vec = h.Vector() # Membrane potential vector (at the MC soma)
#vdend_vec = h.Vector() # Membrane potential vector (at the MC dend)
vtuft_vec = h.Vector() # Membrane potential vector (at the MC tuft)
#vprim_vec = h.Vector() # Membrane potential vector (at the MC prim)
vgemmbody_vec = h.Vector() # Membrane potential vector (at the PGC gemmbody)
t_vec = h.Vector() # Time stamp vector
vsoma_vec.record(mc.soma(0.5)._ref_v)
#vdend_vec.record(mc.dend(0.5)._ref_v)
vtuft_vec.record(mc.tuft(0.5)._ref_v)
#vprim_vec.record(mc.prim(0.5)._ref_v)
vgemmbody_vec.record(pgc.gemmbody(0.5)._ref_v)
t_vec.record(h._ref_t)

# Run the simulation
h.tstop = tstop
h.run()

# plot the membrane potential
plt.figure(figsize=(8,4))
plt.plot(t_vec,vsoma_vec,'k')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at MC soma (mV)')
'''
plt.figure(figsize=(8,4))
plt.plot(t_vec,vdend_vec,'r')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at dend (mV)')
plt.figure(figsize=(8,4))
plt.plot(t_vec,vtuft_vec,'k')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at tuft (mV)')
plt.figure(figsize=(8,4))
plt.plot(t_vec,vprim_vec,'y')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at prim (mV)')
'''
plt.figure(figsize=(8,4))
plt.plot(time,input_current,'k')
plt.xlabel('time ')
plt.ylabel('input current')
plt.figure(figsize=(8,4))
plt.plot(t_vec,vgemmbody_vec,'k')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at PGC gemmbody (mV)')

plt.show()

