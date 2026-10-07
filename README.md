# Quantitative Finance Foundations: Core Statistical Properties

A modular implementation exploring the empirical and statistical foundations of financial time series. This repository focuses on the fundamental concepts required to build robust quantitative models, avoiding common pitfalls such as linear return biases and spurious regressions.

---

## 1. Logarithmic Returns (`01_log_returns.py`)
- **Core Concept:** Simple percentage returns are asymmetric and non-additive over multi-period horizons. Logarithmic returns (`ln(P_t / P_{t-1})`) provide time-additivity and symmetry.
- **Key Takeaway:** An asset dropping 50% and gaining 50% yields a net loss (-25%), accurately captured by continuous compounding (`sum(r_t) = -0.2877`).

## 2. Volatility & Fat Tails (`02_volatility_kurtosis.py`)
- **Core Concept:** Financial asset returns do not adhere to ideal Gaussian (normal) distributions. Market shocks generate extreme fat-tailed risk (leptokurtosis).
- **Key Takeaway:** Analyzing S&P 500 (`^GSPC`) during market turmoil (2020) demonstrates an empirical excess kurtosis of $\approx 8.66$, confirming that standard risk frameworks underestimate black swan events.

## 3. Stationarity & ADF Test (`03_stationarity_adf.py`)
- **Core Concept:** Time series modeling requires weak stationarity (constant mean, constant variance, and time-independent autocovariance).
- **Key Takeaway:** 
  - Raw closing prices exhibit unit roots ($p > 0.05$), leading to spurious correlations if modeled directly.
  - Applying first differencing via log returns rejects the null hypothesis of a unit root ($p \approx 0.0000$), rendering the series stationary and suitable for econometric modeling.

---

## Dependencies
- `python >= 3.9`
- `numpy`
- `pandas`
- `yfinance`
- `statsmodels`
