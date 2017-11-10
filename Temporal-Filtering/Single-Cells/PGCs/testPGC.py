''' Test file for MC single cell stimulation as in MC_Stim.hoc 
of the Cleland model'''

from neuron import h,gui
import tabchannels
import matplotlib.pyplot as plt
import numpy as np

# import cell
h.xopen('PG_def.hoc')

# Parameters
tstop   = 6000
celsius = 35 

# Instantiate a cell
pgc = h.PGcell()

# Current injection
T1  = 1500      
Dur = 4000
Ic1 = 0.36     

'''
stim1 = h.IClamp(mitral.soma(0.5))
stim1.delay = T1
stim1.dur = Dur
stim1.amp = Ic1





# Odour input
F0 = 2.0
F1 = 2.0

stim2 = h.OdorInput(mitral.tuft(0.5))
stim2.delay  = 1000
stim2.dur  = Dur
stim2.torn = 3000
stim2.r    = 100
stim2.f0   = F0
stim2.f1   = F1
'''

# Variable input current

stim3 = h.IClamp(pgc.gemmbody(0.5))
stim3.delay = 0
stim3.dur = 1e9

hz = 3
c = 0.01
time = range(0,tstop)
input_current = np.ones((tstop,))*[np.cos((t/1000.0)*(2*np.pi*hz)) for t in time]*c + c
input_current[0:1000] = 0.0


tvec = h.Vector(tstop)
r=h.Vector(tstop)
for i in range(0,tstop):
	r.x[i] = input_current[i]
	tvec.x[i]=i

#r[tstop-1]=0.0
r.play(stim3._ref_amp,tvec,1,sec=pgc.gemmbody)





# Set up recording variables
vsoma_vec = h.Vector() # Membrane potential vector (at the soma)
vdend_vec = h.Vector() # Membrane potential vector (at the dend)
vgemmshaft_vec = h.Vector() # Membrane potential vector (at the gemmshaft)
vgemmbody_vec = h.Vector() # Membrane potential vector (at the gemmbody)
t_vec = h.Vector() # Time stamp vector
vsoma_vec.record(pgc.soma(0.5)._ref_v)
vdend_vec.record(pgc.dend(0.5)._ref_v)
vgemmshaft_vec.record(pgc.gemmshaft(0.5)._ref_v)
vgemmbody_vec.record(pgc.gemmbody(0.5)._ref_v)
t_vec.record(h._ref_t)

# Run the simulation
h.tstop = tstop
h.run()


# plot the membrane potential
plt.figure(figsize=(8,4))
plt.plot(t_vec,vsoma_vec)
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at soma (mV)')
plt.figure(figsize=(8,4))
plt.plot(t_vec,vdend_vec,'r')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at dend (mV)')
plt.figure(figsize=(8,4))
plt.plot(t_vec,vgemmshaft_vec,'k')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at gemmshaft (mV)')
plt.figure(figsize=(8,4))
plt.plot(t_vec,vgemmbody_vec,'y')
plt.xlabel('time (ms)')
plt.ylabel('membrane potential at gemmbody (mV)')
plt.figure(figsize=(8,4))
plt.plot(time,input_current,'k')
plt.xlabel('time ')
plt.ylabel('input current')

plt.show()

