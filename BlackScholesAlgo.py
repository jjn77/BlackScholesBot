import math
import numpy as np
from scipy.stats import norm 


def blackScholes(spotPrice, strikePrice, time, riskFreeRate, volatility):
	day1 = (np.log(spotPrice/strikePrice) + (riskFreeRate + (volatility**2)/2)*time)/(volatility*np.sqrt(time))
	day2 = day1 - volatility*np.sqrt(time)
	estimate = spotPrice * norm.cdf(day1) - strikePrice*np.exp(-1*riskFreeRate*time)*norm.cdf(day2)
	return estimate
