#imports
import numpy as np
import random

#6.1
N = 1000000
X = np.random.uniform(-5, 5, N) 

def f(x):
	return np.exp(x + x**2)
f = np.vectorize(f)

result = 10 * np.sum(f(X)) / N
print(f"6.1:\nIntegral 1 é {result:.5E}\n")

#############################

#6.3
X = np.random.uniform(0, 1, N) 
Y = np.random.uniform(0, 1, N)

def g(x,y):
	return np.exp((x+y)**2)
g = np.vectorize(g)

result = np.sum(g(X,Y)) / N
print(f"6.3:\nIntegral 2 é {round(result, 5)}\n")
