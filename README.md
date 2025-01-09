# Stock Picking System

The **Stock Picking System** is inspired by the investment philosophy outlined in the book *"The New Tao of Warren Buffett"*. This book delves into the mindset of Warren Buffett, one of the most successful investors of all time. It emphasizes key metrics such as **Earnings Per Share (EPS)**, the **current stock price**, and **future growth potential** to evaluate companies.

To illustrate, consider a stock priced at **$100** with an **EPS of $2**. This means for every dollar invested, you make **2 cents** in earnings, which is not as attractive as the returns from fixed bonds or savings accounts. However, the real appeal of such stocks lies in their **growth potential**. This is especially true for **tech stocks**, where investors are willing to overlook lower immediate returns for the possibility of exponential future growth.

This project implements a stock-picking strategy that aims to identify companies with both:

- **High Stock Returns**: Calculated as `EPS / Stock Price`, this ratio highlights companies with strong returns relative to their stock price.
- **High Piotroski Score**: A metric that evaluates a company’s financial health. A higher Piotroski Score indicates that the stock is financially sound and has better chances of growth.

By combining these two factors, this system helps pinpoint stocks that not only offer strong returns but also have a solid foundation for future success.

---

## Installation

You can easily install the package using pip:

```bash
pip install stock-picking
```

## Usage
### Example 1: Analyze a List of Stocks by Ticker Symbols

You can input a list of stock tickers to analyze and filter based on the Piotroski Score threshold:
```bash
from stock_picking import get_top_stocks

# Example 1
tickers = ["AAPL", "MO", "CINF", "WYNN"]
get_top_stocks(tickers= tickers, exchange='NYSE', piotroski_score_threshold=5, generate_csv=True)
```

### Example 2: Analyze Stocks from a CSV File

If you have a CSV file containing a list of stock tickers, you can pass the file path to the function:
```bash
# Example 2
data_path = "./data/sp_500.csv"
get_top_stocks(tickers = data_path, exchange='NYSE', piotroski_score_threshold=5, generate_csv=True)
```

### Example 3: Analyze Stocks from a DataFrame
If you have the stock data in a DataFrame (e.g., loaded from a CSV), you can directly pass the DataFrame to the function:
```bash
# Example 3
df = pd.read_csv("./data/nifty_50.csv")
get_top_stocks(tickers = df, exchange='NSE', piotroski_score_threshold=5, generate_csv=True)

```

## Limitations

- Since this project uses [yfinance](https://pypi.org/project/yfinance/), make sure 
to adhere to the [rate limits](https://help.yahooinc.com/dsp-api/docs/rate-limits)

## Contributing
Contributions to improve the stock-picking logic or enhance the functionality of this system are welcome! Feel free to fork the repository, submit issues, or open pull requests with suggestions or improvements.

## Next Steps

### Basic
- Adding more data sources for stock financial data fetching
- Improving filtering algorithm
- Adding more test case

### Advanced
- Adding LLM model to give recent developments and details about shortlisted stocks
