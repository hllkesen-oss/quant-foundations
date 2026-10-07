import numpy as np
import pandas as pd

# Price series simulation
prices = [100.0, 50.0, 75.0]
df = pd.DataFrame({'Price': prices})

# Simple vs Logarithmic Returns
df['Simple_Return'] = df['Price'].pct_change()
df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))

print("--- PRICE AND RETURN TABLE ---")
print(df)
print("\n" + "=" * 40 + "\n")

simple_sum = df['Simple_Return'].sum()
log_sum = df['Log_Return'].sum()

print(f"Sum of Simple Returns : %{simple_sum * 100:.2f} (Misleading linear sum)")
print(f"Sum of Log Returns    : {log_sum:.4f} (True cumulative performance)")
print(f"Portfolio Final Value : {100 * np.exp(log_sum):.2f} USD")