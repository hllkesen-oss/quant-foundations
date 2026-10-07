import yfinance as yf
import numpy as np

# Download historical S&P 500 index data (Crisis regime - 2020)
data = yf.download('^GSPC', start='2020-01-01', end='2021-01-01')

# Calculate daily logarithmic returns
data['Log_Return'] = np.log(data['Close'] / data['Close'].shift(1))

# Extract statistical properties
mean_return = data['Log_Return'].mean()
volatility = data['Log_Return'].std()
kurtosis = data['Log_Return'].kurt()

print("Daily Mean Return    :", mean_return)
print("Daily Volatility (Std):", volatility)
print("Kurtosis (Fat Tails) :", kurtosis)