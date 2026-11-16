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

import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Define the query
    query = ("SELECT * FROM TRANSACTIONS")

    # Execute the query
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the cursor and connection
    if (cnx.is_connected()):
        cursor.close()
        cnx.close()
        print("MySQL connection is closed")
