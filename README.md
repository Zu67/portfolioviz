# PortfolioViz

July 2024 Dash experiment. The database password is not stored in this repository.

scripts/LoadMarketData.py and scripts/MarketCalculations.py download Yahoo Finance prices for 2023 and write market-data and calculation rows to a local MySQL database named PortfolioVisualizer. MarketCalculations.py computes beta with scipy linregress.

scripts/app.py, scripts/dash.py, and scripts/dash_app.py are the same one-line Dash hello world.

scripts/MarketCalculationsTest.py is an unfinished test sketch.

scripts/javascript.js is an Express server that reads PORTFOLIO_CALCULATIONS. scripts/test.py reads TRANSACTIONS. scripts/SQL.sql lists databases and tables.
