import numpy as np

amostra1 = [0.18, 0.54, 0.37, 0.18, 0.77, 0.67, 0.35, 0.81, 0.38, 0.95, 0.05, 0.39, 0.78, 0.13, 0.08, 0.91, 0.47, 0.99, 0.35, 0.73, 0.26, 0.07,
0.50, 0.33, 0.56]

amostra2 = [0.71, 0.95, 0.66, 0.29, 0.40, 0.86, 0.19, 0.32, 0.39, 0.90, 0.12, 0.23, 0.79, 0.69, 0.25, 0.49, 0.74, 0.07, 0.33, 0.17, 0.96, 0.04,
0.94, 0.25, 0.91]

std1 = np.std(amostra1) / np.sqrt(len(amostra1))
std2 = np.std(amostra2) / np.sqrt(len(amostra1))

def f(X):
	return  np.sqrt(1-X**2)

f = np.vectorize(f)

result1 = np.mean(f(amostra1))
result2 = np.mean(f(amostra2))
teor_result = np.pi / 4

print("1ª amostra")
print(f"IC a 95%: [{round(result1-1.96*std1,5)}, {round(result1+1.96*std1,5)}]")
print(f"Média amostral: {round(result1,5)}")
print(f"Erro {round(abs(result1 - np.pi/4) * 100 ,3)}%\n")
print("2ª amostra")
print(f"IC a 95%: [{round(result2-1.96*std2,5)}, {round(result2+1.96*std2,5)}]")
print(f"Média amostral: {round(result2,5)}")
print(f"Erro {round(abs(result2 - np.pi/4) * 100 ,3)}%\n")
