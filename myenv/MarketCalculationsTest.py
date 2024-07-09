import mysql.connector
import numpy as np
from scipy.stats import linregress

# Function to calculate beta
def calculate_beta(stock_returns, market_returns):
    if len(stock_returns) != len(market_returns):
        raise ValueError(f"Array length mismatch: stock_returns length {len(stock_returns)}, market_returns length {len(market_returns)}")
    beta, alpha, _, _, _ = linregress(market_returns, stock_returns)
    return beta

try:
    # Database connection
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1', database='PortfolioVisualizer')
    cursor = cnx.cursor()

    # Query to get distinct symbols
    query = "SELECT DISTINCT SYMBOL FROM Transactions"
    cursor.execute(query)
    symbols = cursor.fetchall()

    # Debug: print fetched symbols
    print("Fetched symbols:", symbols)

    # Placeholder for your actual returns data
    stock_returns = np.random.randn(249)  # Replace with actual stock returns data
    market_returns = np.random.randn(251)  # Replace with actual market returns data

    # Debug: print lengths of arrays
    print("Length of stock_returns:", len(stock_returns))
    print("Length of market_returns:", len(market_returns))

    # Align the data lengths
    min_length = min(len(stock_returns), len(market_returns))
    stock_returns = stock_returns[:min_length]
    market_returns = market_returns[:min_length]

    # Debug: print lengths after alignment
    print("Length of stock_returns after alignment:", len(stock_returns))
    print("Length of market_returns after alignment:", len(market_returns))

    # Calculate beta
    beta_p = calculate_beta(stock_returns, market_returns)
    print("Beta:", beta_p)

except mysql.connector.Error as err:
    print(f"Error: {err}")
except ValueError as ve:
    print(f"ValueError: {ve}")

finally:
    cursor.close()
    cnx.close()
