import yfinance as yf
import numpy as np
from statsmodels.tsa.stattools import adfuller

# Download S&P 500 data
data = yf.download('^GSPC', start='2022-01-01', end='2024-01-01')

# 1. Raw Price Series (Non-Stationary)
raw_price = data['Close'].dropna()

# 2. Log Return Series (Transformed / Stationary)
log_return = np.log(raw_price / raw_price.shift(1)).dropna()

def run_adf_test(series, name):
    result = adfuller(series)
    print(f"--- {name} ADF TEST ---")
    print(f"ADF Statistic : {result[0]:.4f}")
    print(f"p-value       : {result[1]:.4f}")
    if result[1] < 0.05:
        print("Decision: STATIONARY (Unit root rejected. Suitable for modeling)\n")
    else:
        print("Decision: NON-STATIONARY (Unit root present. Spurious regression risk!)\n")

run_adf_test(raw_price, "RAW CLOSE PRICE")
run_adf_test(log_return, "LOGARITHMIC RETURN")