# PortfolioViz

July 2024 Dash experiment.

The commits from that history are by the git author "=" <redacted@example.com>.

`LoadMarketData.py` and `MarketCalculations.py` download Yahoo Finance prices for 2023 and write market-data and calculation rows to a local MySQL database named PortfolioVisualizer. The database password is not in the repo and must be supplied locally.

`MarketCalculations.py` computes beta with scipy linregress.

`app.py`, `dash.py`, and `dash_app.py` are the same one-line Dash hello world.

`MarketCalculationsTest.py` is an unfinished test sketch.

Those six Python files are in `scripts/`.
