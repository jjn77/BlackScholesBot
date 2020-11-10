from Robinhood import Robinhood
import credentials
import datetime
import math
import numpy as np
import pandas as pd
import scipy.stats
import BlackScholesAlgo

client = Robinhood()

client.login(credentials.name, credentials.passw)

    #Note: Sometimes more than one instrument may be returned for a given stock symbol
stock_instrument = client.instruments("AMC")[0]
print(stock_instrument)
print('\n')

#Get a stock's quote
print(client.print_quote("AMC"))
print('\n')

#View all data for a given stock ie. Ask price and size, bid price and size, previous close, adjusted previous close, etc.
quote_info = client.quote_data("AMC")
print(quote_info)

spotPrice = float(client.quote_data("AMC")['ask_price'])
print("Spot Price -")
print(spotPrice)

print("Strike Price -")
strikePrice = 3
print(strikePrice)

print("Risk Free Rate -")
riskFreeRate = float(client.quote_data("AMC")['bid_price'])/float(client.quote_data("AMC")['previous_close']) - 1
print(riskFreeRate)

print("Time (in years) -")
time = abs((7 - datetime.datetime.now().day)/250)
print(time)

print("Volatility -")
volatility = np.sqrt(time)*riskFreeRate
print(volatility)

print("Call Option Estimate -")
answer = BlackScholesAlgo.blackScholes(spotPrice, strikePrice, time, riskFreeRate, volatility)
print(answer)

print("Call Option Actual Value -")
shareAmnt = (client.equity()-48.56)/100
print(shareAmnt)
