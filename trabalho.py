import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import pandas as pd
import datetime as dt

plt.style.use("fivethirtyeight")
ticker = "AMZN"
start = dt.datetime(2021, 5, 1)
end = dt.datetime(2022,5,1)
stock_data = yf.download(ticker, start, end)
returns = stock_data['Adj Close'].pct_change()

start_test = dt.datetime(2022, 5, 1)
end_test = dt.datetime(2023,5,1)
stock_data_test = yf.download(ticker, start_test, end_test)

std = returns.std()
mu = returns.mean() 
t = 1

fig,ax = plt.subplots()


big_list = []

for i in range(3):
	stock_value = [stock_data["Adj Close"][-1]]
	for day in range(len(stock_data_test["Adj Close"])-1):
		value = stock_value[-1] * np.exp((mu - (std**2)/2) * t + std * np.random.normal(0,1))
		stock_value.append(value)
	ax.plot(range(len(stock_data_test["Adj Close"])), stock_value, alpha=0.13, linewidth=0.9, zorder = 1, color="#ADADAD")
	big_list.append(stock_value)

ax.plot(range(len(stock_data_test["Adj Close"])), stock_value, alpha=0.13, linewidth=0.9, zorder = 1, color="#ADADAD", label = "Simulações")


df = pd.DataFrame(big_list, columns=range(len(stock_data_test["Adj Close"])))
df.loc["mean"] = df.median()
df.loc["std"] = df.std()


ax.plot(range(len(stock_data_test["Adj Close"])), df.loc["mean"], linewidth=2.5, c ="k", label="Média das Simulações")
ax.plot(range(len(stock_data_test["Adj Close"])), stock_data_test["Adj Close"], linewidth = 3, c = "r", label = "Valor Real")
ax.plot(range(len(stock_data_test["Adj Close"])), df.loc["mean"] - df.loc["std"]*1.96/2, color = "k", linestyle = "dotted", linewidth = 2, label="Intervalo de Confiança de 95%")
ax.plot(range(len(stock_data_test["Adj Close"])), df.loc["mean"] + df.loc["std"]*1.96/2, color = "k", linestyle = "dotted", linewidth = 2)
#ax.fill_between(range(366), df.loc["mean"] - df.loc["std"]*1.96/2, df.loc["mean"] + df.loc["std"]*1.96/2, color = "#26A1EE", alpha = 0.2, zorder = 2)

ax.set_title("Previsão de valor de ação da Amazon (01/05/2022 a 01/05/2023)", loc = "left")
ax.set_xlabel("Dias após 1 de Maio de 2022")
ax.set_ylabel("Valor em Doláres Americanos ($)")

plt.legend(fancybox=False)
plt.show()

fig,ax = plt.subplots()
print(df)
ax.hist(df.iloc[:,-1], bins = 50)
ax.set_title("Histograma dos valores previstos para o valor da ação da Google a 01/05/2023", loc = "left")
ax.set_xlabel("Valor em Doláres Americanos ($)")

plt.show()
print(len(big_list))
for index, row in df.iterrows():
		print(row)

