import matplotlib.pyplot as plt
import numpy as np

#plt.plot? to look at the documentation for the plot function
plt.plot(2, 2, '.')
plt.show()

plt.xlim([0, 5])
plt.ylim([0, 5])

x = np.array([1, 2, 3, 4, 5])
y = x*10
plt.plot(x, y, 'o-')
plt.show()

# artist layer
fig = plt.figure()
ax = plt.subplots()


