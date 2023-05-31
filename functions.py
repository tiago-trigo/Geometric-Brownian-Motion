import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt
from scipy.stats import lognorm

plt.style.use("fivethirtyeight")


def gbm(ticker, datalenght, N):
	if datalenght == "6 Months":
		dift = dt.timedelta(days=180)
	elif datalenght == "1 Year":
		dift = dt.timedelta(days=365)
	elif datalenght == "3 Years":
		dift = dt.timedelta(days=1095)
	elif datalenght == "5 Years":
		dift = dt.timedelta(days=1825)

	start = dt.datetime.now() - dift
	end = dt.datetime.now()

	stock_data = yf.download(ticker, start, end)
	returns = stock_data['Adj Close'].pct_change()
	std = returns.std()
	mu = returns.mean() 

	big_list = []

	for i in range(N):
		stock_value = [stock_data["Adj Close"][-1]]
		for day in range(365):
			value = stock_value[-1] * np.exp((mu - (std**2)/2) + std * np.random.normal(0,1))
			stock_value.append(value)
		big_list.append(stock_value)

	df = pd.DataFrame(big_list, columns=range(len(big_list[0])))
	df.loc["mean"] = df.median()
	df.loc["std"] = df.std()
	print(df.tail())
	return df

def prev_graph(df, ticker, N):
	fig, ax = plt.subplots(figsize=(12,6))
	for index, row in df.iterrows():
		if index >= N-2:
			break
		ax.plot(range(len(df.columns)), row, alpha=0.13, linewidth=0.9, zorder = 1, color="#ADADAD")
	
	#ax.plot(range(len(df.columns)), row, alpha=0.13, linewidth=0.9, zorder = 1, color="#ADADAD", label = "Simulações")
	ax.plot(range(len(df.columns)), df.loc["mean"], linewidth=2.5, c ="k", label="Média das Simulações")
	ax.plot(range(len(df.columns)), df.loc["mean"] - df.loc["std"]*1.96/2, color = "k", linestyle = "dotted", linewidth = 2, label="Intervalo de Confiança de 95%")
	ax.plot(range(len(df.columns)), df.loc["mean"] + df.loc["std"]*1.96/2, color = "k", linestyle = "dotted", linewidth = 2)
	ax.set_title(f"Previsão de valor de ação {ticker}", loc = "left")
	ax.set_xlabel("Dias de negociação após o dia presente")
	ax.set_ylabel("Valor em Doláres Americanos ($)")
	
	plt.legend()
	return fig

def hist(df, ticker):
	expected = np.mean(df.iloc[:,-1])

	fig,ax = plt.subplots(figsize=(12,7.5))
	ax.hist(df.iloc[:,-1], bins = 50, color="#ADADAD", density = True)
	ax.set_title(f"Histograma dos valores previstos para o valor da ação {ticker} após 365 dias de negociação", loc = "left")
	ax.set_xlabel("Valor em Doláres Americanos ($)")

	x = np.linspace(np.min(df.iloc[:,-1]), np.max(df.iloc[:,-1]), 100)
	shape,loc,scale = lognorm.fit(df.iloc[:,-1])
	pdf = lognorm.pdf(x, shape, loc, scale)
	ax.plot(x,pdf, color = "red", label = "Lognormal Fit")
	ax.axvline(expected, label = "Expected Value")

	plt.legend()
	return fig

