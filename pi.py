import numpy as np
import random
import matplotlib.pyplot as plt

N=100000

x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

def f(X,Y):
	return  X**2 + Y**2 <= 1

f = np.vectorize(f)
mask = f(x,y)
result = 4 * np.count_nonzero(mask) / N

x_in = np.array(x)[mask]
y_in = np.array(y)[mask]
x_out = np.array(x)[~mask]
y_out = np.array(y)[~mask]

fig, ax = plt.subplots(figsize=(10,10))

ax.scatter(x_in,y_in)
ax.scatter(x_out,y_out)

print(f"pi é aproximadamente {result}")

plt.show()
