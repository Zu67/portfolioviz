# PortfolioViz

The commits recorded as `=` run from 2024-06-27 through 2024-07-16. `LoadMarketData.py` and `test.py` are the June 27 commit. `MarketCalculations.py` was added on 2024-07-01, `javascript.js` on 2024-07-11, and the Dash apps on 2024-07-16. The database password is not stored in this repository.

`scripts/LoadMarketData.py` downloads AAPL, MSFT, and GOOG from 2023-01-01 through 2023-12-31 and inserts each close into `MARKET_DATA`. It then loads `period="1y"` of history for those three symbols. Holding-period return is (close − open) / open. The other calculation columns, including Sharpe, Treynor, Jensen, PE, ROA, ROE, and the margins, are set to that close. Those rows go into `Market_Calculations`.

`scripts/MarketCalculations.py` reads distinct symbols from `TRANSACTIONS`, downloads that same 2023 window into `MARKET_DATA`, and estimates beta against SPY with `scipy.stats.linregress`. For each day it uses a dividend of 0 and subtracts a risk-free rate of 0.03 from the one-day open-to-close return. Sharpe, Treynor, and Jensen's alpha use that pair. PE, ROA, ROE, and the margins come from `Ticker.info`, or NaN when a key is missing. The style score is `numpy.random.random()`. Every inserted row uses account id 1. `TMW` and `RAR` are both the holding-period return. The table is `PORTFOLIO_CALCULATIONS`.

`scripts/app.py`, `scripts/dash.py`, and `scripts/dash_app.py` are the same Dash app. The layout text is "Hello World", and `app.run_server(debug=True)` starts it.

`scripts/MarketCalculationsTest.py` downloads AAPL, MSFT, and GOOG for 2023, then uses `cursor` and `cnx`, which this file never creates.

scripts/javascript.js is an Express server that reads PORTFOLIO_CALCULATIONS. scripts/test.py reads TRANSACTIONS. scripts/SQL.sql lists databases and tables.
