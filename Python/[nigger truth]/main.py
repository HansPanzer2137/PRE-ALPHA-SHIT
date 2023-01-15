import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 100, 20
x = mu + sigma*np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=1, facecolor='green', alpha=0.75)
y = norm.pdf(bins, mu, sigma)

l = plt.plot(bins, y, 'r--', linewidth=1)
plt.xlabel('IQ')
plt.ylabel('Probability')
plt.title('IQ Histogram')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()