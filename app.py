import streamlit as st
import pandas as pd
import numpy as np
from functions import gbm, prev_graph, hist
from pytickersymbols import PyTickerSymbols

st.set_page_config(page_title = "Stock Forecasting", layout = "wide")

stock_data = PyTickerSymbols()
us_stocks = stock_data.get_stocks_by_index("S&P 500")
df = pd.DataFrame.from_dict(list(us_stocks), orient='columns')
tickers = df["symbol"]

with st.container(): 
	st.title("📈 Stock Price Forecasting")
	st.write("Forecasting future stock prices with geometric brownian motion modeled by a random walk")
#st.markdown("App made by Diogo Pedrosa and Tiago Gonçalves for *Simulação e Processos Estocásticos* subject from Faculdade de Ciências da Universidade do Porto")
st.markdown("**This app is not meant to give financial advice nor are we credited to do so**")
st.write("---")

col1, col2, col3 = st.columns(3)

ticker = col1.selectbox("Select a stock", tickers)
prev_data = col2.selectbox("Select the lenght of training data", ["6 Months", "1 Year", "3 Years", "5 Years"])
runs = col3.selectbox("Select the number of simulations", [1000, 2500, 5000])

st.write("---")

df = gbm(ticker, prev_data, runs)

col1, col2 = st.columns(2)

col1.pyplot(prev_graph(df, ticker), use_container_width = True)
col2.pyplot(hist(df, ticker), use_container_width = True)


