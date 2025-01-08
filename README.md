# Stock Picking System

This Stock Picking Project is inspired from the book "The New Tao of Warren Buffet". This book explains the 
mindset of the famous billionaire while making investment decisions. He stresses on the Earnings Per 
Share (EPS), current price of the Company and finally, future growth prospects. 

Let me give you an example- Let's assume a stock X is worth $100 and it's Earnings per Share is
$2, which means for every dollar you invested- you made 2 cents which is worse than the 
returns in fixed bonds or savings account interest. But the main reason why investors still
buy these shares is because see huge growth potential. You will find it most common with
Tech Stocks. 

This project focuses on identifying the stocks that have high `Stock Returns (EPS/Stock Price)` and
high `Piotroski Score`. High Piotroski Score indicates that the stock is healthy and is likely to 
grow in future

### Installation
```bash
pip install stock-picking
```

### Usage
```bash
from stock_picking import get_top_stocks

# Example 1
tickers = ["AAPL", "MO", "CINF", "WYNN"]
get_top_stocks(tickers= tickers, exchange='NYSE', piotroski_score_threshold=5, generate_csv=True)

# Example 2
data_path = "./data/sp_500.csv"
get_top_stocks(tickers = data_path, exchange='NYSE', piotroski_score_threshold=5, generate_csv=True)

# Example 3
df = pd.read_csv("./data/nifty_50.csv")
get_top_stocks(tickers = df, exchange='NSE', piotroski_score_threshold=5, generate_csv=True)

```

