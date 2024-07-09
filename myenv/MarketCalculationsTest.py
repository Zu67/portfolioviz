import yfinance as yf
import mysql.connector
from datetime import datetime
import numpy as np
import pandas as pd
from scipy.stats import linregress

symbols = ['AAPL', 'MSFT', 'GOOG']

# Fetch market data and insert into MARKET_DATA table
for symbol in symbols:
    stock_data = yf.download(symbol, start="2023-01-01", end="2023-12-31")
    for date, row in stock_data.iterrows():
        cursor.execute("""
            INSERT INTO MARKET_DATA (DATE, SYMBOL, VALUE)
            VALUES (%s, %s, %s)
        """, (date.strftime('%Y-%m-%d'), symbol, row['Close']))

# Commit the transaction
cnx.commit()

# Placeholder risk-free rate and market return
risk_free_rate = 0.03

# Function to calculate beta
import pandas as pd

import pandas as pd

def calculate_beta(stock_returns, market_returns):
    # Convert both series to DataFrames and align them
    stock_returns = pd.Series(stock_returns)
    market_returns = pd.Series(market_returns)

    # Ensure both series have the same time zone or are both naive
    if stock_returns.index.tz is not None and market_returns.index.tz is not None:
        stock_returns = stock_returns.tz_convert(None)
        market_returns = market_returns.tz_convert(None)
    elif stock_returns.index.tz is not None:
        stock_returns = stock_returns.tz_localize(None)
    elif market_returns.index.tz is not None:
        market_returns = market_returns.tz_localize(None)

    # Align the indices and drop missing values
    aligned_returns = pd.DataFrame({'stock': stock_returns, 'market': market_returns}).dropna()
    
    # Calculate beta
    covariance_matrix = aligned_returns.cov()
    beta = covariance_matrix.loc['stock', 'market'] / covariance_matrix.loc['market', 'market']
    
    return beta

# Example usage:
# Assuming stock_returns and market_returns are already defined
beta_p = calculate_beta(stock_returns, market_returns)
print(beta_p)



# Fetch market calculations and insert into PORTFOLIO_CALCULATIONS table
for symbol in symbols:
    stock_data = yf.Ticker(symbol)
    history = stock_data.history(period="1y")
    
    market_data = yf.download('SPY', start="2023-01-01", end="2023-12-31")
    market_returns = market_data['Close'].pct_change().dropna()

    stock_returns = history['Close'].pct_change().dropna()

    # Debug: print lengths of arrays before alignment
    print(f"Before alignment: {symbol}")
    print("Length of stock_returns:", len(stock_returns))
    print("Length of market_returns:", len(market_returns))

    # Calculate beta
    beta_p = calculate_beta(stock_returns, market_returns)

    for date, row in history.iterrows():
        # Calculate HPR
        P_begin = row['Open']
        P_end = row['Close']
        D = 0  # Placeholder for dividend
        hpr = (P_end + D - P_begin) / P_begin

        # Calculate portfolio return
        R_p = (row['Close'] - row['Open']) / row['Open']
        
        # Standard deviation of stock returns for Sharpe ratio
        sigma_p = stock_returns.std()

        # Calculate Sharpe Ratio
        sharpe_ratio = (R_p - risk_free_rate) / sigma_p if sigma_p != 0 else 0

        # Calculate Treynor Ratio
        treynor_ratio = (R_p - risk_free_rate) / beta_p if beta_p != 0 else 0

        # Calculate Jensen's Alpha
        jensens_alpha = R_p - (risk_free_rate + beta_p * (market_returns.mean() - risk_free_rate))

        # Fetch financial data for additional metrics
        try:
            pe_ratio = stock_data.info['forwardPE']
            roa = stock_data.info['returnOnAssets']
            roe = stock_data.info['returnOnEquity']
            gross_margin = stock_data.info['grossMargins']
            profit_margin = stock_data.info['profitMargins']
        except KeyError:
            pe_ratio = np.nan
            roa = np.nan
            roe = np.nan
            gross_margin = np.nan
            profit_margin = np.nan

        style_score = np.random.random()  # Placeholder for style score calculation


print(market_returns.head())