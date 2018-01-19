import matplotlib.pyplot as plt
import numpy as np

y = np.load("Circuit_4/c0.45/1/Interspike_frequencies.npy")
x = range(len(y))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y,'k*')
plt.show()
