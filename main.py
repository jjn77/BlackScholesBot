from Robinhood import Robinhood
import credentials
import datetime
import math
import numpy as np
import time
import pandas as pd
import scipy.stats
import BlackScholesAlgo

client = Robinhood()

client.login(credentials.name, credentials.passw)

while(True): 
	spotPrice = float(client.quote_data("AMC")['ask_price'])
	print("Spot Price -")
	print(spotPrice)

	print("Strike Price -")
	strikePrice = 3
	print(strikePrice)

	print("Risk Free Rate -")
	riskFreeRate = abs(float(client.quote_data("AMC")['bid_price'])/float(client.quote_data("AMC")['previous_close']) - 1)
	print(riskFreeRate)

	print("Time (in years) -")
	stockTime = abs((7 - datetime.datetime.now().day)/250)
	print(stockTime)

	print("Volatility -")
	volatility = np.sqrt(stockTime)*riskFreeRate
	print(volatility)

	print("Call Option Estimate -")
	answer = BlackScholesAlgo.blackScholes(spotPrice, strikePrice, stockTime, riskFreeRate, volatility)
	print(answer)

	print("Call Option Actual Value -")
	shareAmnt = (client.equity()-48.56)/100
	print(shareAmnt)
	
	time.sleep(7200)

