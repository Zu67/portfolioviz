import yfinance as yf
import mysql.connector
from datetime import datetime

# MySQL connection configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'PortfolioVisualizer'
}

# Connect to MySQL
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# Sample stock symbols
symbols = ['AAPL', 'MSFT', 'GOOG']

# Fetch market data and insert into MARKET_DATA table
for symbol in symbols:
    stock_data = yf.download(symbol, start="2023-01-01", end="2023-12-31")
    for date, row in stock_data.iterrows():
        cursor.execute("""
            INSERT INTO MARKET_DATA (DATE, SYMBOL, VALUE)
            VALUES (%s, %s, %s)
        """, (date, symbol, row['Close']))

# Commit the transaction
cnx.commit()

# Fetch market calculations and insert into Market_Calculations table
for symbol in symbols:
    stock_data = yf.Ticker(symbol)
    history = stock_data.history(period="1y")
    
    for date, row in history.iterrows():
        hpr = (row['Close'] - row['Open']) / row['Open']
        market_value = row['Close']
        tmw = row['Close']  # Simplification for TMW
        rar = row['Close']  # Simplification for RAR
        sharpe = row['Close']  # Simplification for Sharpe
        treynor = row['Close']  # Simplification for Treynor
        jensens = row['Close']  # Simplification for Jensen's Alpha
        pe_ratio = row['Close']  # Simplification for PE Ratio
        style_score = row['Close']  # Simplification for Style Score
        roa = row['Close']  # Simplification for ROA
        roe = row['Close']  # Simplification for ROE
        gross_margin = row['Close']  # Simplification for Gross Margin
        profit_margin = row['Close']  # Simplification for Profit Margin

        cursor.execute("""
            INSERT INTO Market_Calculations (HPR, MARKET_VALUE, TMW, RAR, SHARPE, TREYNOR, JENSENS, PE_RATIO, STYLE_SCORE, ROA, ROE, GROSS_MARGIN, PROFIT_MARGIN)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (hpr, market_value, tmw, rar, sharpe, treynor, jensens, pe_ratio, style_score, roa, roe, gross_margin, profit_margin))

# Commit the transaction and close the connection
cnx.commit()
cursor.close()
cnx.close()
