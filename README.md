# PortfolioViz

The commits recorded as `=` run from 2024-06-27 through 2024-07-16. `LoadMarketData.py` and `test.py` are the June 27 commit. `MarketCalculations.py` was added on 2024-07-01, `javascript.js` on 2024-07-11, and the Dash apps on 2024-07-16. Every connection uses user `root`, database `PortfolioVisualizer`, and an empty password. The Python scripts use host `127.0.0.1`. The Express server uses host `localhost`.

`scripts/LoadMarketData.py` downloads AAPL, MSFT, and GOOG from 2023-01-01 through 2023-12-31 and inserts each close into `MARKET_DATA`. It then loads `period="1y"` of history for those three symbols. Holding-period return is (close − open) / open. The other calculation columns, including Sharpe, Treynor, Jensen, PE, ROA, ROE, and the margins, are set to that close. Those rows go into `Market_Calculations`.

`scripts/MarketCalculations.py` reads distinct symbols from `TRANSACTIONS`. The `MARKET_DATA` insert downloads each symbol with `start="2023-01-01"` and `end="2023-12-31"` and stores the close. Beta uses a different pair: that symbol's trailing `period="1y"` close-to-close returns against SPY's close-to-close returns for the same 2023 arguments, from `scipy.stats.linregress`. The rows written to `PORTFOLIO_CALCULATIONS` are the trailing year, not the 2023 download. For each of those days the dividend is 0, and the holding-period return is (close − open) / open. Sharpe divides that return minus 0.03 by the standard deviation of the trailing close-to-close returns. Treynor divides the same numerator by beta. Jensen's alpha is that return minus 0.03, minus beta times the mean of the 2023 SPY close-to-close returns minus 0.03. PE, ROA, ROE, and the margins come from `Ticker.info`, or NaN when a key is missing. Another exception is not caught. The style score is `numpy.random.random()`. Every inserted row uses account id 1. Account value is that day's close. `TMW` and `RAR` are both the holding-period return.

`scripts/app.py`, `scripts/dash.py`, and `scripts/dash_app.py` are the same Dash app. The layout text is "Hello World", and `app.run_server(debug=True)` starts it.

`scripts/MarketCalculationsTest.py` downloads AAPL, MSFT, and GOOG for 2023, then uses `cursor` and `cnx`, which this file never creates.

`scripts/javascript.js` is an Express server on port 3000. `GET /market_calculations` reads `PORTFOLIO_CALCULATIONS`. `scripts/test.py` reads `TRANSACTIONS`. `scripts/SQL.sql` lists databases and tables.
