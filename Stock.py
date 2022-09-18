import yfinance as yf
import pandas as pd



#Stock Name
stock_name = "NVDA"
stock = yf.Ticker(stock_name)

dataset = stock.history(period="max")

file_name = 'MarksData.csv'

dataset.to_csv(file_name)



print(stock.info)