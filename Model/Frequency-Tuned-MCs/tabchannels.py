"""
Read function tables for tabchannels.
Needed for kfasttab.mod, kslowtab.mod and nagran.mod.
All data now in a single file, tabchannels.dat.

Author: Andrew Davison, July 2003, converted to Python November 2010
"""

npoints = 1001
from neuron import h, load_mechanisms

load_mechanisms("Channels")

datafile = h.File()
datafile.ropen("tabchannels.dat")
datafile.seek(0)

vvec = h.Vector(npoints)
vvec.scanf(datafile,1,13)
datafile.seek() # goes to beginning of file
datavec = []
for i in range(12):
  datavec.append(h.Vector(npoints))
  datavec[i].scanf(datafile,i+2,13)
  datafile.seek()

datafile.close()

assert vvec.size() == npoints

h.table_tabninf_kfasttab(datavec[0]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabntau_kfasttab(datavec[1]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabkinf_kfasttab(datavec[2]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabktau_kfasttab(datavec[3]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabninf_kslowtab(datavec[4]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabntau_kslowtab(datavec[5]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabkinf_kslowtab(datavec[6]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabktau_kslowtab(datavec[7]._ref_x[0], npoints, vvec._ref_x[0])
'''
h.table_tabminf_nagrantab(datavec[8]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabmtau_nagrantab(datavec[9]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabhinf_nagrantab(datavec[10]._ref_x[0], npoints, vvec._ref_x[0])
h.table_tabhtau_nagrantab(datavec[11]._ref_x[0], npoints, vvec._ref_x[0])
'''
