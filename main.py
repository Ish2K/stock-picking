from stock_picking import get_top_stocks

# Get the top stocks
get_top_stocks("./data/nifty_50.csv", exchange='NSE', piotroski_score_threshold=5)
